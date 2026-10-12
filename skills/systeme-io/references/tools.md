# Choose tools by observed capability

Skill -> current documentation -> connected tool or browser -> verification.

| Route | Use | Boundary |
|---|---|---|
| Official Systeme.io integration | Discover available account, contact, funnel, page, email, product, calendar and automation tools | Inventory varies by client and version; do not assume all dashboard actions are exposed |
| Systeme.io Extra MCP | The whole documented public API: 22 tool groups, 152 actions (contacts, tags, funnels, page content, newsletters, campaigns, email stats, courses, enrolments, communities, products, coupons, subscriptions, booking, webhooks, SMS templates) | Only what the public API offers (no refunds, no single SMS sending). Every write is previewed, then confirmed; `high_impact` actions flagged in help |
| Authenticated browser | Dashboard-only creation/editing, account settings and rendered inspections | Requires actual signed-in access and supported browser controls |
| Public help browsing | Research and explain workflows | Supplies no private account access |

Discover tools through the current connector or Docker Gateway; inspect action help before choosing one. For Extra MCP, read its installed schema or [repository](https://github.com/softreviewed/systeme-extra-mcp). A public API key and an official MCP key are separate credentials, both under **Settings → MCP & API keys** in separate lists. Extra MCP needs the **Public API key**; given the MCP key it returns HTTP 401 "Invalid API Key." A skill installation creates neither.

To build or replace page content through Extra MCP: `pages.schema` (read the page model) → `pages.template` (get a starting template) → preview `pages.save` or `pages.apply_template` with `dry_run:true` → user approval → `confirm:true` → open the public URL to check. Both writes overwrite the page, so export the current content first.

If no account connection exists, produce a plan, copy or step-by-step guidance. Never claim changes were made. If a tool is missing, use an available supported route; describe the concrete missing access only when it blocks completion.

For Extra MCP writes, preview with `dry_run:true`; execute with `confirm:true` only inside the authorized scope. That flag is not proof of human permission. Re-read state after a timeout before retrying. Help/previews work without a key; account requests need one. Customer subscription cancellation is not cancellation of the owner's platform plan.

Official starting point: https://help.systeme.io/category/11216-model-context-protocol-mcp

Official API reference: https://developer.systeme.io/llms.txt
