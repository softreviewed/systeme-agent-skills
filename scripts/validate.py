"""Check skill identity, local references, source metadata, encoding and obvious credential patterns."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT/'skills/systeme-io'

def validate():
    errors = []
    entry = (SKILL/'SKILL.md').read_text(encoding='utf-8')
    if not entry.startswith('---\n'): errors.append('Missing frontmatter')
    name = re.search(r'^name: (.+)$', entry, re.M)
    if not name or name.group(1) != SKILL.name: errors.append('Name must match skill folder')
    description = re.search(r'^description: (.+)$', entry, re.M)
    if not description or not 1 <= len(description.group(1)) <= 1024: errors.append('Invalid description')
    if len(entry.splitlines()) >= 500: errors.append('Entrypoint too long')
    sources = json.loads((SKILL/'references/source-index.json').read_text(encoding='utf-8'))
    urls = [a['url'] for a in sources['articles']]
    if len(urls) != len(set(urls)): errors.append('Duplicate source URLs')
    if not urls or any(not u.startswith('https://help.systeme.io/article/') for u in urls): errors.append('Unexpected source host/path')
    if sources['article_bodies_copied']: errors.append('Unexpected copied article bodies')
    patterns = [r'gh[pousr]_[A-Za-z0-9]{30,}', r'github_pat_[A-Za-z0-9_]{30,}', r'AccountKey=[A-Za-z0-9+/]{30,}', r'-----BEGIN [A-Z ]*PRIVATE KEY-----']
    for f in ROOT.rglob('*'):
        if not f.is_file() or any(x in f.parts for x in ('.git','dist','__pycache__','scratch')): continue
        if f.suffix not in ('.md','.py','.json','.txt','.yaml','.yml') and f.name not in ('.gitignore','LICENSE'): continue
        text = f.read_text(encoding='utf-8')
        if '\ufffd' in text or '\u00e2\u2020' in text: errors.append(str(f.relative_to(ROOT))+' encoding')
        if any(re.search(p, text) for p in patterns): errors.append(str(f.relative_to(ROOT))+' possible credential')
        if f.suffix == '.md':
            for link in re.findall(r'\]\(([^)]+)\)',text):
                if '://' in link or link.startswith('#'): continue
                target = (f.parent/link.split('#')[0]).resolve()
                if not target.exists(): errors.append(str(f.relative_to(ROOT))+' missing reference '+link)
    return errors

if __name__ == '__main__':
    errors = validate()
    if errors: raise SystemExit('\n'.join(errors))
    print('Validated skill metadata, local links, source index, encoding and credential scan.')
