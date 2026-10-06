"""Check local skill files only; never connect accounts or inspect credentials."""
import json
from pathlib import Path
from route_task import ROUTES

def check(root):
    required = ('SKILL.md', 'LICENSE', 'scripts/find_sources.py', 'scripts/route_task.py',
                'references/source-index.json', 'references/tools.md', 'assets/campaign-worksheet.md', *ROUTES)
    missing = [path for path in required if not (root/path).is_file()]
    return {'files_complete': not missing, 'missing': missing,
            'planning': 'ready' if not missing else 'incomplete',
            'account_connection': 'not tested', 'publication_and_sending': 'not tested'}

if __name__ == '__main__':
    result = check(Path(__file__).resolve().parents[1])
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result['files_complete'] else 1)
