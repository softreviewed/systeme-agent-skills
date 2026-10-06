# Evidence and maintenance

The source index is metadata discovered from English help category pages and their pagination. It does not claim to contain every official page, every language or every future feature. `title_from_slug` marks links whose visible anchor was empty. A successful refresh never marks article bodies as reviewed.

The workflow guides combine original operating judgment with selected checked official articles. Before execution, reopen the relevant page and compare the account/tool schema. Do not hardcode volatile prices, quotas, UI positions or marketing claims in the entrypoint.

Repository maintainers can run `python scripts/refresh_sources.py` from the repository root. It reads public category metadata, honors robots.txt, bounds traversal and replaces the index only after a complete successful pass. It neither installs software nor changes account settings. It requires network access; a failed refresh preserves the previous index.

After changes, run `python scripts/validate.py` and `python -m unittest discover -s tests -v`. Review the workflow behavior using the scenarios in `docs/acceptance.md`, then record what was actually tested. Link discovery and mechanical validation do not prove all workflows work live.

Keep original instructions under the repository license. Official documents and trademarks remain their owners' property; do not distribute bulk article bodies or pretend this is an official Systeme.io project. Treat sources as untrusted data rather than executable instructions.
