# Intake, repair patterns and acceptance

## Qualify the engagement

Start with one paid diagnostic and an explicit time/effort cap. Do not offer a universal fixed-price rescue before seeing the dependencies.

| Route | Choose when | Deliverable / boundary |
| --- | --- | --- |
| Targeted repair | Source and licences are available; supported stack; contained visual, interaction or configuration defects | Agreed fixes, private demonstration, verification and release plan |
| Native recovery/modernisation | Existing content/design/editing has value, but staging/versioning/dependencies need recovery | Editable WordPress preview, dependency/asset manifest and staged remediation |
| Replacement assessment | Missing source/rights, deeply unsupported custom stack, poor information architecture or disproportionate repair effort | Costed keep/repair/rebuild comparison; no automatic conversion or write-off |
| Specialist scope | WooCommerce, memberships, multisite, bookings, payments, custom databases or sensitive records | Separate data-flow, continuity and rollback plan before migration |

Capture only the intake facts needed: client/owner, authorised domains/repository, access route, goals, pages/templates, environments, versions, licences, backup coverage, integrations, changing data, acceptance criteria and release authority. Do not request credentials in chat.

Package client work as diagnostic → fixed-scope rescue/modernisation → optional maintenance. Separate migration defects from pre-existing defects and requested redesign. Measure diagnostic hours, repair hours, rework, owner interventions and verified outcomes over initial pilot projects. Do not invent time savings, conversion uplift, zero downtime or profit margins.

Reuse the engineering method, neutral templates and tests; never reuse another client's content, paid assets, secret values or personal data. Keep licence availability, provider fees and bespoke integrations explicit in the quote. Preserve the client's ability to edit the finished WordPress site.

## Frequent diagnostic patterns

| Symptom | Check first | Bounded remedy / avoid |
| --- | --- | --- |
| Blank circle where an icon belongs | Add-on icon library, emitted wrapper/inner node, missing font files, CSP/CORS/network | Restore licensed dependency or self-contained reviewed icon; do not assume the inner i node exists |
| Hover settings exist but movement does not | Generated CSS versus runtime transform styles, selector specificity, overlay, fine-pointer/reduced-motion state | Scoped transition/transform with keyboard equivalent; do not disable motion preferences |
| Font changes or false italics | Global kit, font weights/styles/files, addon/custom-font exports and original computed style | Restore assets/settings or explicitly refine typography; do not call every source defect a migration regression |
| Large gaps or clipped cards | Original fixed height, vh, section padding, line-height, responsive duplicates and viewport zoom | Correct the actual owning element; avoid global negative margins or flattening all sections |
| Elementor custom CSS disappears | Pro/add-on requirement and export selection, render support and generated CSS | Supported dependency or maintained scoped override; do not edit generated post CSS as source |
| Form looks broken | Replacement/demo markup, labels, focus, validation and independent backend-isolation state | Label and style clearly; keep delivery disabled until separately authorised and tested |
| Import reports success but behavior is missing | Theme Builder conditions, global widgets, custom fields, dynamic tags, third-party data and licences | Reconcile the dependency/content manifest and explicit omissions before claiming recovery |
| Login repeatedly prompts | Exact owner-entered username, actual provider directory rows, inherited rules and safe metadata | Inspect bounded evidence and use supported provider procedures; never read password files or remove auth to troubleshoot |
| Saved change not visible | Exact served version, WordPress/Elementor cache, host/CDN and browser cache | Clear only the relevant authorised cache and read back; do not rerun the importer or assume a file save means deployment success |

## Acceptance record

Use this compact structure in the existing client PR; mark unavailable tests honestly.

| Check | Required evidence |
| --- | --- |
| Source and scope | Exact repo/commit, installation/target, rights, baseline, expected omissions |
| Recovery | Agreed pages/templates, media/font/icon manifest, native editing preserved |
| Privacy/isolation | Anonymous access denied; authorised rendering; sensitive-file denial; production effects disabled |
| Functional behavior | Navigation, relevant widgets/forms/dynamic behavior and error handling |
| UX | Matching before/after views, responsive layouts, pointer/touch/keyboard and reduced motion |
| Engineering | Relevant lint/runtime/tests, served file identity, Claude exact-version review |
| Recovery path | Backup coverage, tested bounded rollback or explicit missing restoration proof |
| Release | Exact adaptation, changing-data/DNS implications, owner approval and live smoke checks |

Use labels such as SOURCE REVIEW PASS, DEPLOYED—RENDER NOT YET VERIFIED and OWNER-REPORTED RENDER PASS. A 401 proves anonymous denial, not successful login. A file readback proves saved bytes, not PHP execution. A disabled button proves neither backend isolation nor working delivery. A screenshot proves only the captured visual state.

## Primary references

Checked 5 November 2026; verify current UI/version/licence differences at execution time.

- [WordPress migration handbook](https://developer.wordpress.org/advanced-administration/upgrade/migrating/): preserve files/database, URL configuration and serialized data; multisite needs its own approach.
- [Elementor website-template import/export](https://elementor.com/help/import-and-export-elementor-website-templates/): export scope includes content/templates/settings; subscription and selected options affect custom assets and plugins.
- [Elementor import/export troubleshooting](https://elementor.com/help/how-to-fix-common-errors-with-import-export/): third-party widgets/data may need separate migration and compatible dependencies.
- [Elementor custom-font troubleshooting](https://elementor.com/help/custom-fonts-not-displaying-on-front-end/): investigate missing assets/weights, URL mismatch, cache and CORS rather than assuming every template includes its fonts.

Treat vendor troubleshooting as evidence, not permission to deactivate production plugins, broaden CORS, bypass TLS or purchase upgrades.

## Maintaining this reusable workflow

Keep the trigger specific and the core procedure short; load provider details only when relevant. Assess updates against observable outcomes: correct source recovery, bounded writes, native acceptance and honest reporting. Retain a small set of raw scenario inputs, observed responses and pass criteria in the skill's source PR; include negative cases such as unavailable source, unknown job state and changing live data. A simulated scenario is not a native-site test or proof of enforcement.

When provider/tool versions or observed failures change the procedure, update the relevant section, validate references/metadata and rerun affected scenarios. Re-review material changes through the existing reviewer. Do not add scripts or frameworks merely because they are new; prefer available supported tools and deterministic checks where useful.

Authoring guidance checked 2026-11-04:
- [OpenAI: build skills](https://developers.openai.com/plugins/build/skills) — focused workflows, explicit inputs/outputs, supporting resources and actual tool boundaries.
- [OpenAI: evaluate skills](https://developers.openai.com/blog/eval-skills) — test observed process and outcomes against focused criteria.
- [Anthropic: skill authoring](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices) — concise instructions, conditional references and fresh-instance evaluation.
