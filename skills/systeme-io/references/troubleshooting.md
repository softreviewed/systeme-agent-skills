# Troubleshooting

Capture the exact symptom, affected URL/record, last successful action and error/status. Separate source, saved account state, cache and public result. Reproduce with read-only checks before changing settings.

| Symptom | Inspect first |
|---|---|
| Page missing or old | Correct URL, publish state, domain assignment, saved content, then cache |
| Form submits but no follow-up | Correct form trigger, contact status, campaign subscription, email activation/delay |
| Email not arriving | Sender authentication, recipient status, delivery evidence, spam folder |
| Domain not approved | Exact account DNS values, resolution, HTTPS and relevant CAA/provider guidance |
| Course access missing | Correct student/course, access type, purchase automation and actual enrolment record |
| MCP login failure | Correct credential type, permissions, connected server and current schema |
| Extra MCP SMS 424/404 | Check documented missing Twilio integration; do not assume a paid plan is the cause |
| Customer subscription lookup empty | Required real contact ID, filters and pagination; empty data differs from request failure |
| Rate limit or timeout | Returned retry guidance; read current state before retrying a write |

Use [find_sources.py](../scripts/find_sources.py) to find the symptom-specific official article. Prefer scoped cache refreshes; do not disable security or purge unrelated assets without necessity and authorization. Never retry financial/access mutations blindly after uncertain responses.

Report: issue -> minimal change -> verified result -> remaining uncertainty. If support is needed, prepare a concise redacted diagnostic summary; do not send it without authorization. Private customer data and credentials do not belong in screenshots or public issues.

Sources: [Customer support](https://help.systeme.io/category/165-support), [Official help search](https://help.systeme.io/).
