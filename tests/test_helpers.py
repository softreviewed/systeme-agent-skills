import importlib.util
import json
import tempfile
import unittest
import subprocess
import sys
from pathlib import Path
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parents[1]

def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec); spec.loader.exec_module(module); return module

installer = load('installer', ROOT/'scripts/install.py')
packager = load('packager', ROOT/'scripts/package.py')
finder = load('finder', ROOT/'skills/systeme-io/scripts/find_sources.py')
refresh = load('refresh', ROOT/'scripts/refresh_sources.py')
router = load('router', ROOT/'skills/systeme-io/scripts/route_task.py')

class Helpers(unittest.TestCase):
    def test_complete_install_and_readiness(self):
        with tempfile.TemporaryDirectory() as temp:
            dest = installer.install(Path(temp)/'systeme-io')
            for guide in router.ROUTES: self.assertTrue((dest/guide).exists(), guide)
            result = json.loads(subprocess.check_output([sys.executable, str(dest/'scripts/check_install.py')],text=True))
            self.assertTrue(result['files_complete'])
            self.assertEqual(result['account_connection'], 'not tested')
            (dest/'references/campaign/visual-design.md').unlink()
            run = subprocess.run([sys.executable, str(dest/'scripts/check_install.py')],capture_output=True,text=True)
            self.assertEqual(run.returncode, 1)
            self.assertIn('references/campaign/visual-design.md',json.loads(run.stdout)['missing'])
    def test_bundle_is_one_complete_skill(self):
        with tempfile.TemporaryDirectory() as temp:
            with ZipFile(packager.package(Path(temp)/'bundle.zip', 'bundle')) as z:
                self.assertEqual({p.split('/')[0] for p in z.namelist()}, {'systeme-io'})
                self.assertIn('systeme-io/references/campaign/email-campaigns.md', z.namelist())
                self.assertIn('systeme-io/LICENSE', z.namelist())
                self.assertFalse(any('__pycache__' in p or '..' in p for p in z.namelist()))
    def test_selective_task_routing(self):
        access = router.route('give a student course access')
        self.assertIn('references/courses-communities.md', access)
        self.assertFalse(any('/campaign/' in p for p in access))
        self.assertIn('references/campaign/visual-design.md', router.route('fix cramped mobile spacing'))
        self.assertIn('references/campaign/email-campaigns.md', router.route('write a welcome sequence'))
        self.assertEqual(router.route('zzznomatch'), [])
        self.assertLessEqual(len(router.route(' '.join(router.ROUTES.values()))),4)
    def test_unknown_skill_rejected(self):
        with self.assertRaises(ValueError): installer.install(ROOT/'scratch/unknown', 'unknown')
        with self.assertRaises(ValueError): packager.package(ROOT/'scratch/unknown.zip', 'unknown')
    def test_existing_install_preserved(self):
        with tempfile.TemporaryDirectory() as temp:
            dest = Path(temp)/'systeme-io';dest.mkdir(); (dest/'mine.txt').write_text('preserve')
            with self.assertRaises(FileExistsError): installer.install(dest)
            self.assertEqual((dest/'mine.txt').read_text(), 'preserve')
    def test_install_contains_references(self):
        with tempfile.TemporaryDirectory() as temp:
            dest = installer.install(Path(temp)/'systeme-io')
            self.assertTrue((dest/'SKILL.md').exists())
            self.assertTrue((dest/'references/source-index.json').exists())
            self.assertTrue((dest/'scripts/find_sources.py').exists())
            result = subprocess.check_output([sys.executable, str(dest/'scripts/find_sources.py'), 'email campaign'],text=True)
            self.assertTrue(json.loads(result)['results'])
            self.assertTrue((dest/'LICENSE').exists())
    def test_wrong_folder_rejected(self):
        with self.assertRaises(ValueError): installer.install(ROOT/'scratch/wrong-name')
    def test_symlink_not_overwritten(self):
        # The exists OR is_symlink guard also preserves broken links.
        with tempfile.TemporaryDirectory() as temp:
            target = Path(temp)/'systeme-io'
            try: target.symlink_to(Path(temp)/'missing', target_is_directory=True)
            except OSError: self.skipTest('Symlink privilege unavailable')
            with self.assertRaises(FileExistsError): installer.install(target)
    def test_archive_is_portable(self):
        with tempfile.TemporaryDirectory() as temp:
            zpath = packager.package(Path(temp)/'skill.zip')
            with ZipFile(zpath) as z:
                self.assertIn('systeme-io/SKILL.md', z.namelist())
                self.assertIn('systeme-io/references/source-index.json',z.namelist())
                self.assertTrue(all(p.startswith('systeme-io/') and '..' not in p for p in z.namelist()))
                self.assertFalse(any('__pycache__' in p for p in z.namelist()))
                self.assertIn('systeme-io/LICENSE',z.namelist())
    def test_search_real_index(self):
        index = json.loads((ROOT/'skills/systeme-io/references/source-index.json').read_text(encoding='utf-8'))
        for query in ['email campaign','domain','automation rules','website','course']:
            results = finder.search(index, query, 5)
            self.assertTrue(results,query)
            self.assertTrue(any(set(query.split()) & set(x['title'].lower().split()) for x in results),query)
        self.assertEqual(finder.search(index,'zzznomatchxyz'),[])
    def test_crawler_stays_on_official_host(self):
        self.assertIsNone(refresh.normalize('https://evil.example/article/test'))
        self.assertIsNone(refresh.normalize('http://help.systeme.io/article/test'))
        self.assertEqual(refresh.normalize('https://help.systeme.io/category/test?sort=popularity&page=2#x'),'https://help.systeme.io/category/test?page=2')
    def test_anchor_metadata(self):
        parser=refresh.Links();parser.feed('<a href="/article/test"><b>Useful</b> title</a>')
        self.assertEqual(parser.links,[('/article/test','Useful title')])

if __name__ == '__main__': unittest.main()
