"""Refresh public help-page metadata, not article bodies. No account credentials used."""
import argparse
import json
import time
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin, urlsplit, parse_qsl, urlencode, urlunsplit
from urllib.request import Request, urlopen
from urllib.robotparser import RobotFileParser

BASE = 'https://help.systeme.io'
AGENT = 'SoftReviewedSkillsIndex/1.0'
ROOT = Path(__file__).resolve().parents[1]

class Links(HTMLParser):
    def __init__(self):
        super().__init__(); self.links = []; self.href = None; self.text = []
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            self.href = dict(attrs).get('href'); self.text = []
    def handle_data(self, data):
        if self.href is not None: self.text.append(data)
    def handle_endtag(self, tag):
        if tag == 'a' and self.href is not None:
            self.links.append((self.href, ' '.join(' '.join(self.text).split())))
            self.href = None

def normalize(url):
    p = urlsplit(url)
    if p.scheme != 'https' or p.netloc != 'help.systeme.io': return None
    query = dict(parse_qsl(p.query))
    page = query.get('page')
    q = urlencode({'page': page}) if page and page != '1' else ''
    return urlunsplit((p.scheme, p.netloc, p.path, q, ''))

def fetch(url, robots):
    if not robots.can_fetch(AGENT, url): raise RuntimeError('robots.txt disallows '+url)
    with urlopen(Request(url, headers={'User-Agent': AGENT}), timeout=30) as r:
        if urlsplit(r.url).netloc != 'help.systeme.io': raise RuntimeError('Unexpected redirect')
        data = r.read(5_000_001)
        if len(data) > 5_000_000: raise RuntimeError('Page too large')
        parser = Links(); parser.feed(data.decode('utf-8')); return parser.links

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--max-pages', type=int, default=80)
    p.add_argument('--delay', type=float, default=0.6)
    args = p.parse_args()
    if args.max_pages < 1 or args.delay < 0.2: p.error('Use positive bounds and delay >= 0.2 seconds')
    robots = RobotFileParser(BASE+'/robots.txt'); robots.read()
    home = fetch(BASE+'/', robots)
    categories = {}
    for href, title in home:
        u = normalize(urljoin(BASE, href))
        if u and '/category/' in u:
            categories[u] = title.rstrip('› ').strip()
    queue = list(categories); seen = set(); articles = {}; failures = []
    while queue and len(seen) < args.max_pages:
        url = queue.pop(0)
        if url in seen: continue
        seen.add(url); time.sleep(args.delay)
        try: links = fetch(url, robots)
        except Exception as e:
            failures.append({'url': url, 'error': str(e)}); continue
        category_url = url.split('?')[0]
        for href, title in links:
            u = normalize(urljoin(url, href))
            if not u: continue
            if '/article/' in u:
                if not title:
                    title = u.rsplit('/', 1)[-1].split('-', 1)[-1].replace('-', ' ')
                    inferred = True
                else: inferred = False
                row = articles.setdefault(u, {'url': u, 'title': title, 'title_from_slug': inferred, 'categories': []})
                if row['title_from_slug'] and not inferred: row.update(title=title, title_from_slug=False)
                cat = categories.get(category_url, category_url)
                if cat not in row['categories']: row['categories'].append(cat)
            elif u.split('?')[0] == category_url and u not in seen and u not in queue:
                queue.append(u)
    # A failed/incomplete refresh must not overwrite the known-good published index.
    if failures or queue:
        raise RuntimeError('Incomplete refresh; index unchanged. '+json.dumps({'failures': failures, 'remaining_pages': len(queue)}))
    if not articles: raise RuntimeError('No articles discovered; index unchanged')
    result = {'checked_at': datetime.now(timezone.utc).isoformat(),
              'scope': 'English help category pages and their observed pagination',
              'article_bodies_copied': False, 'categories': categories,
              'category_pages_checked': len(seen),
              'articles': sorted(articles.values(), key=lambda x: x['title'].lower())}
    target = ROOT/'skills/systeme-io/references/source-index.json'
    temporary = target.with_suffix('.tmp'); temporary.write_text(json.dumps(result, indent=2, ensure_ascii=False)+'\n', encoding='utf-8'); temporary.replace(target)
    print(f'Indexed {len(articles)} help links across {len(categories)} categories and {len(seen)} category pages.')

if __name__ == '__main__': main()
