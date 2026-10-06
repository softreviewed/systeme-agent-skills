"""Create a skill-only ZIP with one top-level skill directory."""
import argparse
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED

ROOT = Path(__file__).resolve().parents[1]

SKILLS = ('systeme-io', 'landing-page-email-design', 'frontend-design')

def package(output, skill='systeme-io'):
    if skill not in (*SKILLS, 'bundle'): raise ValueError('Unknown skill')
    target = Path(output); target.parent.mkdir(parents=True, exist_ok=True)
    with ZipFile(target, 'w', ZIP_DEFLATED) as z:
        for name in (SKILLS if skill == 'bundle' else (skill,)):
            source = ROOT/'skills'/name
            for f in sorted(source.rglob('*')):
                if f.is_file() and '__pycache__' not in f.parts and f.suffix != '.pyc':
                    z.write(f, f.relative_to(source.parent).as_posix())
            if not (source/'LICENSE.txt').exists(): z.write(ROOT/'LICENSE', name+'/LICENSE')
    return target

if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--skill', choices=(*SKILLS, 'bundle'), default='systeme-io')
    p.add_argument('--output')
    args = p.parse_args()
    filename = 'systeme-agent-skills-bundle.zip' if args.skill == 'bundle' else args.skill+'-skill.zip'
    print('Created:', package(args.output or ROOT/'dist'/filename, args.skill))
