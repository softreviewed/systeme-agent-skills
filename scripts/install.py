"""Copy one portable skill to an explicitly chosen directory. Never overwrite an existing skill."""
import argparse
import shutil
from pathlib import Path

SOURCE = Path(__file__).resolve().parents[1]/'skills/systeme-io'

def install(destination):
    target = Path(destination).expanduser().absolute()
    if target.name != 'systeme-io': raise ValueError('Destination must end with systeme-io')
    if target.exists() or target.is_symlink(): raise FileExistsError('Existing destination preserved: '+str(target))
    if target.resolve().is_relative_to(SOURCE.resolve()): raise ValueError('Cannot install inside the source skill')
    shutil.copytree(SOURCE, target, ignore=shutil.ignore_patterns('__pycache__', '*.pyc'))
    shutil.copy2(SOURCE.parents[1]/'LICENSE', target/'LICENSE')
    return target

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--destination', required=True, help='Full destination skill folder, ending with systeme-io')
    p.add_argument('--dry-run', action='store_true')
    args = p.parse_args()
    if args.dry_run:
        print('Preview only:', SOURCE, '->', Path(args.destination).expanduser().absolute()); return
    try: print('Installed:', install(args.destination))
    except (ValueError, FileExistsError) as e: p.exit(1, str(e)+'\n')
    print('Reload the agent and confirm it discovers systeme-io. No account connection or credentials were changed.')

if __name__ == '__main__': main()
