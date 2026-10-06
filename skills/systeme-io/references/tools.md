# Choose tools by observed capability

Skill -> current documentation -> connected tool or browser -> verification.

| Route | Use | Boundary |
|---|---|---|
| Official Systeme.io integration | Discover available account, contact, funnel, page, email, product, calendar and automation tools | Inventory varies by client and version; do not assume all dashboard actions are exposed |
| Systeme.io Extra MCP | Course enrolments, community membership, contact-field definitions, customer subscription cancellation, webhooks and Twilio configuration reads | Six tools/20 operations in the companion release; no email sending, funnel building, refunds or SMS sending |
| Authenticated browser | Dashboard-only creation/editing, account settings and rendered inspections | Requires actual signed-in access and supported browser controls |
| Public help browsing | Research and explain workflows | Supplies no private account access |

Discover tools through the current connector or Docker Gateway; inspect action help before choosing one. For Extra MCP, read its installed schema or [repository](https://github.com/softreviewed/systeme-extra-mcp). A public API key and an official MCP key are separate credentials. A skill installation creates neither.

If no account connection exists, produce a plan, copy or step-by-step guidance. Never claim changes were made. If a tool is missing, use an available supported route; describe the concrete missing access only when it blocks completion.

For Extra MCP writes, preview with `dry_run:true`; execute with `confirm:true` only inside the authorized scope. That flag is not proof of human permission. Re-read state after a timeout before retrying. Help/previews work without a key; account requests need one. Customer subscription cancellation is not cancellation of the owner's platform plan.

Official starting point: https://help.systeme.io/category/11216-model-context-protocol-mcp

Official API reference: https://developer.systeme.io/llms.txt
