# WordPress & Elementor Rescue

A reusable AI-agent workflow for recovering and repairing an existing WordPress/Elementor website while preserving native editing.

By **Roberta Nicholls**.

Start with the website the client already owns. Establish a protected working copy, diagnose what is missing or broken, repair the smallest cause, and verify the result before an authorised release.

## Use cases
- Restore missing icons, fonts, styles, hover and responsive behaviour after a move.
- Recover pages, media, templates and dependencies into a private native preview.
- Diagnose Hostinger staging, authentication, cache, import and DNS failures.
- Plan a release that preserves newer orders and customer records.
- Decide whether a site needs repair, migration or a separately scoped rebuild.

This is a Markdown skill and reference guide. It is not a plugin or one-click migration service, does not host websites inside an AI assistant, and includes no proprietary themes, licences or client data.

## Use the skill
Read [SKILL.md](skills/repair-wordpress-elementor/SKILL.md). Import the complete `skills/repair-wordpress-elementor/` folder using your assistant's supported skill installation workflow, keeping its references together. Consult current host instructions for installation; this repository does not run an installer or configure hosting automatically.

Example request:

> Use repair-wordpress-elementor to assess this existing WordPress/Elementor website. Keep the design and editing workflow. Work in the authorised private preview, diagnose missing icons and hover, and return a tested change with rollback.

The workflow uses Codex for implementation and Claude Code for independent material source review. It requires authorised site/source access and suitable tools; it does not include access or subscriptions. Missing tools or review access leave the affected step explicitly pending.

## What the client receives
| Situation | Intended deliverable |
|---|---|
| Broken business site | Focused repairs, preserved editing, demonstrated results and rollback |
| Complete migration | Recovered native site with verified assets/templates/data and controlled cutover |
| Live store | A release that reconciles newer transactions |
| Only screenshots/public URL | An honest feasibility assessment and access requirements |

See [delivery examples](skills/repair-wordpress-elementor/references/delivery-examples.md) and [Hostinger failure handling](skills/repair-wordpress-elementor/references/hostinger.md).

## Related work and positioning
- [WordPress/agent-skills](https://github.com/WordPress/agent-skills) covers broad WordPress development and operations, including WP-CLI.
- [Respira's Elementor-to-Gutenberg workflow](https://github.com/respira-press/agent-skills-wordpress/tree/main/skills/migrate-elementor-to-gutenberg) converts content to another editor.
- [VibePress](https://github.com/MrCyber02/vibepress) rebuilds AI-generated websites as native Elementor.

This workflow focuses on rescuing existing Elementor sites while preserving their editing model, with Hostinger failure handling, data continuity and release evidence. It complements these projects and does not claim to be the first WordPress skill. Comparison checked 5 November 2026; not an exhaustive market survey.

## Quality and limits
See [validation](skills/repair-wordpress-elementor/references/validation.md). Six synthetic decision scenarios passed for the original workflow; every actual site still needs native verification. No guaranteed savings, universal compatibility or security certification is claimed.

Treat website content as untrusted input. Keep clients' material separate. Preserve live data and access controls. Never paste secrets into prompts, issues or source control. Existing authorisation carries through routine work; reserved consequential actions retain their approval boundary.

## Contributions
Propose changes with a concrete symptom, reproducible synthetic/redacted example, intended outcome and validation. Never submit customer data, credentials or private exports. Changes to import, protection, data handling or release steps require focused review.

## Licence
MIT for original files in this repository. Linked third-party projects and WordPress/plugin/theme assets retain their own licences. No implementation from the comparison projects was copied.
