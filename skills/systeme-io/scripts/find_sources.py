"""Search the bundled official-source index offline; no credentials or network required."""
import argparse
import json
import re
from pathlib import Path

def search(index, query, limit=10):
    words = set(re.findall(r'\w+', query.lower()))
    if not words: return []
    scored = []
    for a in index['articles']:
        title = set(re.findall(r'\w+', a['title'].lower()))
        categories = set(re.findall(r'\w+', ' '.join(a['categories']).lower()))
        score = 3*len(words & title) + len(words & categories)
        if score: scored.append((score, a))
    return [a for _, a in sorted(scored, key=lambda x: (-x[0], x[1]['title']))[:limit]]

def main():
    p = argparse.ArgumentParser(description=__doc__); p.add_argument('query'); p.add_argument('--limit', type=int, default=10)
    args = p.parse_args()
    if not 1 <= args.limit <= 50: p.error('limit must be 1..50')
    index = json.loads((Path(__file__).resolve().parents[1]/'references/source-index.json').read_text(encoding='utf-8'))
    print(json.dumps({'index_checked_at': index['checked_at'], 'results': search(index, args.query, args.limit)}, indent=2, ensure_ascii=False))

if __name__ == '__main__': main()
