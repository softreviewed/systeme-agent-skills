# Automation and contacts

Write the behavior before configuring it: exact event -> filters/conditions -> actions -> delays -> exit condition. Distinguish funnel-form and website-form events; use the schema and actual form ID from the chosen builder. A tag-based action may affect more than one campaign.

Inspect existing rules/workflows first to avoid duplicate sends, circular tag triggers and repeated enrolments. Name each rule for its purpose. Prefer one small change and a single authorized test record to modifying all contacts.

For imports, inspect mapping, duplicates, consent, suppressions and import automation behavior. Do not activate campaigns for an imported list without authorization. For contact fields, distinguish creating a field definition from assigning values on a contact. Deleting definitions may affect forms or automation; inspect usage first.

Use official tools for available contact-value/tag/rule operations; Extra MCP provides field-definition operations, not a complete CRM. Search help for the exact rule, workflow, tag or contact task.

Verify both the saved rule and observable result: correct contact, expected tag/campaign/access, no unexpected action. If the connector cannot expose execution history, say so and use dashboard evidence when available. Configuration success alone is not a completed automation test.

Sources: [Contact management](https://help.systeme.io/category/537-contacts-management), [General automation articles](https://help.systeme.io/category/131-general), [Official MCP help](https://help.systeme.io/category/11216-model-context-protocol-mcp).
