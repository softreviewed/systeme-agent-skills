"""Create a skill-only ZIP with one top-level skill directory."""
import argparse
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED

ROOT = Path(__file__).resolve().parents[1]

def package(output):
    source = ROOT/'skills/systeme-io'
    target = Path(output); target.parent.mkdir(parents=True, exist_ok=True)
    with ZipFile(target, 'w', ZIP_DEFLATED) as z:
        for f in sorted(source.rglob('*')):
            if f.is_file() and '__pycache__' not in f.parts and f.suffix != '.pyc':
                z.write(f, f.relative_to(source.parent).as_posix())
        z.write(ROOT/'LICENSE', 'systeme-io/LICENSE')
    return target

if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--output', default=str(ROOT/'dist/systeme-io-skill.zip'))
    print('Created:', package(p.parse_args().output))
