"""Copy one portable skill to an explicitly chosen directory. Never overwrite an existing skill."""
import argparse
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ('systeme-io',)
SOURCE = ROOT/'skills/systeme-io'

def install(destination, skill='systeme-io'):
    if skill not in SKILLS: raise ValueError('Unknown skill')
    source = ROOT/'skills'/skill
    target = Path(destination).expanduser().absolute()
    if target.name != skill: raise ValueError('Destination must end with '+skill)
    if target.exists() or target.is_symlink(): raise FileExistsError('Existing destination preserved: '+str(target))
    if target.resolve().is_relative_to((ROOT/'skills').resolve()): raise ValueError('Cannot install inside the source skills')
    shutil.copytree(source, target, ignore=shutil.ignore_patterns('__pycache__', '*.pyc'))
    if not (target/'LICENSE.txt').exists(): shutil.copy2(ROOT/'LICENSE', target/'LICENSE')
    return target

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--skill', choices=SKILLS, default='systeme-io')
    p.add_argument('--destination', required=True, help='Full destination folder, ending with the selected skill name')
    p.add_argument('--dry-run', action='store_true')
    args = p.parse_args()
    if args.dry_run:
        print('Preview only:', ROOT/'skills'/args.skill, '->', Path(args.destination).expanduser().absolute()); return
    try: print('Installed:', install(args.destination, args.skill))
    except (ValueError, FileExistsError) as e: p.exit(1, str(e)+'\n')
    print('Complete toolkit installed. Reload the agent and use systeme-io for your first task. Read references/getting-started.md for readiness checks. No account connection or credentials were changed.')

if __name__ == '__main__': main()
