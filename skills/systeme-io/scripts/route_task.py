"""Return relevant guide paths without loading guide bodies or account data."""
import argparse
import json
import re

ROUTES = {
 'references/account-domains.md': 'domain dns migration allowance plan limits account setup',
 'references/websites.md': 'website blog bio sitemap indexing canonical',
 'references/funnels.md': 'funnel landing optin webinar checkout selling',
 'references/email.md': 'email campaign newsletter sender deliverability authenticate sending',
 'references/automation-contacts.md': 'automation workflow trigger tag contact field',
 'references/courses-communities.md': 'course student enrolment enrollment access community membership',
 'references/payments.md': 'payment gateway subscription cancellation coupon refund price',
 'references/other-workflows.md': 'affiliate calendar booking physical product',
 'references/troubleshooting.md': 'failure broken error troubleshooting failed',
 'references/campaign/visual-design.md': 'design visual layout spacing cramped mobile typography button hover colors',
 'references/campaign/audience-copy.md': 'copy headline audience objection promise cta seo message persuasive',
 'references/campaign/email-campaigns.md': 'write welcome nurture onboarding sequence subject draft',
 'references/campaign/quality-experiments.md': 'review quality test conversion experiment performance accessibility',
 'references/getting-started.md': 'install installation readiness started setup connect',
}

def route(task, limit=4):
    words = set(re.findall(r'[a-z]+', task.lower()))
    scored = [(len(words & set(terms.split())), path) for path, terms in ROUTES.items()]
    return [path for score, path in sorted(scored, key=lambda x: (-x[0], x[1])) if score][:max(1, min(limit, 4))]

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('task')
    args = parser.parse_args()
    paths = route(args.task)
    print(json.dumps({'guides': paths, 'fallback': None if paths else 'Use the task table in SKILL.md; clarify the requested outcome.'}, indent=2))
