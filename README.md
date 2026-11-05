# WordPress & Elementor Rescue

**A free skill for Codex and Claude, by Roberta Nicholls.** Use it when a client wants to keep editing the WordPress site they already own, but a page, a migration or a staging release has gone wrong.

The skill guides your assistant through a repair in a protected copy. It helps you trace the symptom, check what a visitor actually sees and prepare a change you can roll back.

[Download the Claude skill ZIP](dist/repair-wordpress-elementor-claude.zip?raw=1) · [Browse the Claude instructions](claude/skills/repair-wordpress-elementor/SKILL.md) · [Browse the Codex instructions](skills/repair-wordpress-elementor/SKILL.md)

## Choose your edition

| Where you work | How to install | Try it |
| --- | --- | --- |
| Codex | Copy the complete `skills/repair-wordpress-elementor/` folder into your project's `.agents/skills/` directory. Keep its reference files alongside `SKILL.md`. | In Codex CLI or the IDE, select `$repair-wordpress-elementor` and describe the symptom. [Codex skill guide](https://developers.openai.com/codex/skills/) |
| Claude with custom skill uploads | In **Customize → Skills**, use the upload option to add the Claude skill ZIP linked above, then enable it. Upload the ZIP as supplied. Custom skills require code execution to be enabled and your workspace to allow them. | Start a chat and ask Claude to use `repair-wordpress-elementor` with one of the examples below. [Claude upload guide](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills) |
| Claude Code on your machine | Unzip the Claude download. Place its complete `repair-wordpress-elementor/` directory inside your project's `.claude/skills/`, or in `~/.claude/skills/` for personal use. | In that project, enter `/repair-wordpress-elementor` followed by your request. [Claude Code skill locations](https://code.claude.com/docs/en/skills#where-skills-live) |

Both editions use the same skill name. Choose the edition written for your assistant. The download contains instructions and guides. Hosting, assistant subscriptions, site permissions and commercial plugin licences are separate.

## Three requests to try

| Situation | Example prompt |
| --- | --- |
| **You saved an Elementor edit. Visitors still see the old page.** | “In Elementor the event starts at 18:00, but the visitor page says 17:00. Help me compare the URL, active template and cached version. Tell me how to verify the fix outside the editor.” |
| **The site moved. The icons and fonts disappeared.** | “A service link has lost its icon after a hosting move. Trace one missing asset from its widget to the requested file, then check the repaired link on mobile and desktop in our private preview.” |
| **The staging fix is ready. Orders have kept coming in.** | “We changed the layout in staging and the live shop has newer orders. Determine whether a file-only release is enough. If data must move, identify the records to reconcile and the rollback before proposing cutover.” |

These are illustrative prompts. You can also use the skill to assess a client handover, identify incomplete Elementor exports or investigate a protected Hostinger preview. With only a public URL and screenshots, start with an assessment and a list of the source and licences required to proceed. [Delivery examples](skills/repair-wordpress-elementor/references/delivery-examples.md) · [Hostinger guide](skills/repair-wordpress-elementor/references/hostinger.md)

## Before asking for a change

For a repair, provide the affected route, the expected and observed behaviour, and authorised access to the relevant source and protected preview. For a migration, confirm both files and database backup coverage and the restore route. Keep outgoing mail, payments and other live integrations isolated in the preview. Keep credentials, customer records and raw backups inside the client's approved private systems.

Ask for the changed source, matching before-and-after views, a native Elementor edit/save check, test results and rollback steps. The Codex edition calls for independent Claude Code review of material changes at the exact commit. A person or session that implements a change needs a separate reviewer. If access, review or site tests are missing, the handover should say exactly which checks remain open.

## What has been verified

The original Codex workflow was exercised against six synthetic decision scenarios, including one with orders received after staging was copied. These evaluate the assistant's choices. Each real site still needs its own version checks, protected-preview tests and release decision. [Original validation record](skills/repair-wordpress-elementor/references/validation.md)

## Contributing and reporting problems

For a documentation or workflow issue, include the edition, revision, symptom, a minimal synthetic example, what you expected and how to check the result. For changes involving imports, private previews or live data, include a case where the assistant should stop.

Keep vulnerabilities, client exports, personal data and credentials out of public issues and pull requests. For a security concern, use GitHub private vulnerability reporting if the repository offers it. Otherwise contact the maintainer through an established private channel before sharing sensitive details.

## Related projects

[WordPress Agent Skills](https://github.com/WordPress/agent-skills) covers broader WordPress development and operations. [Respira's Elementor-to-Gutenberg skill](https://github.com/respira-press/agent-skills-wordpress/tree/main/skills/migrate-elementor-to-gutenberg) focuses on editor conversion. [VibePress](https://github.com/MrCyber02/vibepress) focuses on rebuilding sites in Elementor. This project focuses on repair and recovery while preserving native editing.

## Licence

Copyright © 2026 Roberta Nicholls. The original skill files are available under the [MIT licence](LICENSE). Third-party WordPress components, themes, plugins, fonts and client assets retain their own licences.
