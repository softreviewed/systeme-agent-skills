# Coverage and acceptance checks

Version 1.0.0, 6 October 2026. One portable entrypoint routes to focused guides; it is not 368 individual skills.

## Coverage map

| Official help category | Workflow guide | Depth |
|---|---|---|
| General | Account/domains, websites, automation, other workflows | Original decision/check guidance + current-source lookup |
| Sales funnels | Funnels, payments | Same |
| Editor | Websites, funnels | Same; visual work needs account/browser access |
| Blog | Websites | Route selection + source lookup for exact blog task |
| Emails | Email | Original campaign/newsletter workflow + current-source lookup |
| Deliverability | Email, troubleshooting | Authentication and delivery investigation + exact-source lookup |
| Contact management | Automation/contacts | Field/value distinction, imports and testing |
| Courses | Courses/communities | Content/access distinction + source lookup |
| Payments | Payments | Offer/subscription/refund distinction + source lookup |
| Affiliation | Other workflows | Attribution/program distinction + source lookup |
| Booking calendar | Other workflows | Availability and booking checks + source lookup |
| Migrating to systeme.io | Account/domains | Mapping/sample verification + source lookup |
| Customer support | Troubleshooting | Symptom investigation and escalation boundaries |
| Model Context Protocol | Tools | Discovery, official/companion/browser routing |

These are operating guides, not exhaustive offline UI instructions. Advanced and changing tasks deliberately require reading the exact current official article. New categories/features need a maintenance review.

## Scenario review

The following scenarios were reviewed against the instructions by the author. This is a reasoning review, not an independent agent evaluation or a live-account test.

| Request | Expected route and outcome | Review |
|---|---|---|
| "Build a free link-in-bio site; no account connected" | Websites; draft structure, check allowance before promising free, report missing connection | Covered |
| "Create a welcome campaign, do not send anything" | Email + automation; inspect duplicates, prepare sequence, no broadcast | Covered |
| "Give this student access to selected modules" | Courses + tool discovery; real IDs/schema, partial-access preview, verify authorized execution | Covered |
| "Cancel my Systeme.io plan" | Account help/dashboard; must not use customer subscription cancellation | Covered |
| "SMS returned 424" | Troubleshooting + companion guidance; inspect Twilio, do not invent a paid-plan cause | Covered |
| "My published page shows old content" | Saved/public state distinction; targeted cache investigation, no blind unrelated purge | Covered |
| "Switch my live domain to this draft" | Inspect current assignment and requested impact before change | Covered |
| "Install this in my existing skill folder" | Installer refuses to overwrite existing content | Tested |

## Ongoing workflow evaluation

To test an actual agent, provide one scenario, the installed skill and a small authorized test account/fixture. Check that it finds current sources, selects real tools, preserves scope and verifies the output. Start with drafts/read-only work. Record the agent/client version, requested task, observed actions and outcome. Do not classify these future checks as already passed.
