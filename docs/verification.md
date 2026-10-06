# Verification and limits

Checked 6 October 2026.

| Check | Observed result |
|---|---|
| Official help metadata | 368 unique article URLs, 14 categories, 25 category pages; public English category traversal completed |
| Article reproduction | No full article bodies distributed; original guides and a title/URL index |
| Skill-creator validator | Passed |
| Portable package | ZIP build/extraction structure and complete reference installation tested |
| Safe installation | Existing destinations and symlinks preserved; no settings/credentials changed |
| Source search | Website, email, domain, automation and course queries returned relevant indexed sources |
| Host boundaries | Index URL normalization rejects unrelated hosts and non-HTTPS URLs |
| Text checks | Local references, metadata, encoding and obvious credential patterns checked |
| Live Systeme.io mutations | None performed to test this skill |
| Client installation | Isolated folder installation tested; not installed/activated in every named application |
| Workflow scenarios | Author reasoning review; no independent model evaluation |

The existing Extra MCP has its own separate test record. Its tests do not establish that this skill or every workflow has been tested live.

## Selected primary sources consulted

- [Website builder](https://help.systeme.io/article/4526-how-to-create-a-website)
- [Alternative website routes](https://help.systeme.io/article/1596-what-are-the-different-methods-to-create-a-website)
- [Funnel setup](https://help.systeme.io/article/147-how-to-create-a-funnel)
- [Opt-in page](https://help.systeme.io/article/152-how-to-create-a-opt-in-page)
- [Email campaign](https://help.systeme.io/article/367-how-to-set-up-an-email-campaign)
- [Email sequence automation](https://help.systeme.io/article/284-how-to-automate-the-sending-of-a-series-of-emails-campaign)
- [Email domain authentication](https://help.systeme.io/article/316-how-to-authenticate-your-personal-domain-name)
- [Official MCP overview](https://help.systeme.io/article/9489-how-to-use-systeme-ios-mcp)

The larger index contains discovered links, not a claim of individual article review. Reopen current help and inspect account/tool behavior before execution.

## Maintenance

Refresh metadata manually with `python scripts/refresh_sources.py`, review any changed claims in the guides, then validate/test and publish a new version. No automatic freshness guarantee or scheduled job is installed. Index discovery is bounded and fails without replacing the old index if pages cannot be fetched.
