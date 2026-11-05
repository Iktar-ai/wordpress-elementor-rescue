# Illustrative repair cases

These are composite teaching scenarios, not reports about real clients, and they do not record executed results. Use them as diagnostic orderings. Confirm every step against the actual site, host and versions. With only chat context, produce an assessment and a bounded next step. Use an authorised native preview for actual changes and tests.

---

## Case 1: A saved Elementor edit that visitors cannot see

**Symptoms.** The editor shows the change and Update succeeded. Logged-out visitors, or another device, still see the old version. Sometimes only one breakpoint is affected.

**Causes to distinguish:**
1. **Page caching:** host cache (for example LiteSpeed or the hPanel cache), a cache plugin, a CDN or the browser. Logged-in users often bypass the cache, which hides the problem.
2. **Stale Elementor generated CSS:** the CSS print method is set to external file, and the uploads/elementor/css files were not regenerated or cannot be written.
3. **Wrong target:** the edit went into a different template, a header or footer with other display conditions, a translation, a draft or scheduled revision, or a staging copy instead of live.
4. **Responsive overrides:** a tablet or mobile value, or a hidden-on-device copy of the widget, overrides the edited desktop value.
5. Object cache or minify/combine plugins serving old assets.

**Diagnostic order:**
- Reproduce the problem logged out in a private window. Record the route, the viewport and the response headers that show cache state, such as age, x-litespeed-cache and cf-cache-status.
- Confirm that the edit was saved. Check the Elementor revision history and the post modified time, and confirm which post or template ID the visible element comes from.
- Check the display conditions and the language for any template involved.
- Check that uploads/elementor/css can be written and its timestamps.

**Repair:**
1. Match the saved revision to the page a visitor receives. If the evidence identifies a stale cache or generated file, refresh only the relevant layer on the authorised target. Use the controls supported by the installed Elementor version.
2. If the cause was a wrong target or a responsive override, fix it in Elementor's native settings.
3. Never hand-edit generated CSS as the fix, because it will be regenerated.
4. If a cache rule persistently serves stale HTML, adjust that rule with the account holder. Do not disable caching site-wide as a workaround.

**Verification:**
- Make a test edit and save it.
- Confirm it as a logged-out visitor at each affected breakpoint, then revert it.
- Check the response headers after a fresh request.
- Record PASS, FAIL, NOT RUN or BLOCKED for each item.

**Pitfalls:**
- Purging only the plugin cache while a CDN still serves the old page.
- Reporting the fix from a logged-in view.
- Editing live when the owner expected the change to go through staging.

---

## Case 2: Icons, fonts or images missing after a move

**Symptoms.** After a migration or domain change, icons show as blank squares, custom fonts fall back to system fonts, some images 404, or hover effects that depended on an icon font break.

**Likely causes:**
- **Old domain or protocol still referenced** in Elementor data. Elementor stores its data as JSON with escaped slashes, and plain find-and-replace misses or corrupts it. Theme options can also contain serialized PHP.
- **Files missing from uploads:** the uploads folder was not fully copied, including uploads/elementor/custom-icons and custom font files.
- **Mixed content:** http asset URLs on an https site.
- **CORS refusals:** fonts loaded from another origin or CDN without the right header.
- **Server problems:** file permissions or ownership, or case-sensitive paths on the new server.
- **Dependency problems:** an icon library or add-on that is not active, not licensed or a different version on the target.
- **Old cache:** generated CSS or a CDN still pointing to the old host.

**Diagnostic order:**
- Open the browser network panel on a failing route and classify each failure: 404, 403, CORS or mixed content.
- Compare the uploads inventory and the active plugin and version list between source and target.
- Inspect the emitted wrapper for a missing icon to see whether the markup is absent (data or library problem) or present but unstyled (CSS or font file problem).

**Repair:**
1. If authorised assets were omitted, restore those files from the verified source or backup to the protected target, keeping the paths, case and permissions.
2. If the failing URL still points to the old host, preview a serialization-aware replacement with explicitly scoped tables and excluded GUIDs. Record the changed rows, apply only the reviewed change to the protected target and read it back.
3. If that dependency caused the failure, re-activate the supported, licensed icon or font dependency. Or, if only a couple of decorative icons are involved, replace them deliberately with reviewed inline SVG on the verified wrapper and keep accessible names.
4. Refresh affected generated styles or caches only when evidence identifies them as stale.

**Verification:**
- The network panel shows no 404, mixed-content or CORS errors on the affected routes.
- Before and after screenshots match at the same viewport.
- Hover and focus states work.
- Editing and saving the page in Elementor keeps the assets.

**Pitfalls:**
- Replacing URLs in a raw SQL dump.
- Installing an abandoned or paid add-on just to bring back one icon.
- Calling the move complete because the home page looks right.

---

## Case 3: A staging release after newer live orders

**Situation.** Staging was cloned from live days ago and has approved design or plugin changes. Meanwhile the live WooCommerce shop has taken new orders and registrations, and may have subscription renewals, form submissions and stock changes. The owner wants staging pushed live.

**Core rule.** Never push the older staging database over live. That would destroy newer orders, customers, accounts, subscriptions and submissions. Order data may sit in posts and postmeta, in the newer order tables, or in both. Inspect the installed subscription and scheduling integrations before choosing a reconciliation method.

**Diagnostic order:**
- Identify the actual hosting/staging product and whether its documented release operation copies files, data or both. While the host is unknown, keep the advice provider-neutral and give a conditional decision. Hostinger-specific guidance applies only after the target is verified.
- **Classify each change from evidence:** A spacing adjustment can live in a stylesheet, a theme setting or an Elementor document. Inspect the changed file, template or record before choosing a release route.
  - files: theme, child theme, plugins, custom code
  - content: pages and templates stored in the database
  - settings: options and the Elementor kit
- **List the live data written since the clone:**
  - orders
  - users
  - subscriptions and scheduled actions
  - form entries
  - stock
- **Confirm available release controls:** check whether the verified host supports selecting files or records.

**Release approach. Pick one with the owner.**
- **Files-only release:** when the fix is entirely in code or assets, release just those reviewed files and keep the live database in place. If inspection finds a template or setting stored in the database, propose a narrowly scoped migration for review and rehearse it on a protected copy first. Do not direct the operator to redo the edit in live Elementor as a shortcut.
- **Freeze and delta reconciliation:** used when database changes are unavoidable.
  1. Agree a maintenance window. Pause checkout and registrations, and pause renewal queues only if that is safe.
  2. Take and verify a fresh live backup.
  3. Apply the staging changes to live, or merge them with a scripted, dry-run-first plan.
  4. Reconcile stable identifiers, statuses, totals, stock, refunds, customer relationships, subscriptions, queues and payment events across the actual snapshot boundary. Counts alone can conceal a missing order or a duplicate charge. Resolve late writes and replay risk before reopening.
  5. Resume.

**Protections:**
- Before any direct production mutation, obtain approval for the exact change, verify backup and rollback, and document how order and customer deltas will be reconciled. Leave the staging environment intact. Refreshing, recloning or deleting it is separately scoped and can erase outstanding work.
- On staging, payment gateways stay in test mode, mail is captured and renewals and cron are disabled. A clone holding live payment tokens or schedules can otherwise charge customers or send duplicate emails.
- Do not carry staging-only guards or test keys into production.
- No cutover, DNS change or paid service without explicit owner approval of that exact release.
- **Gates before release:**
  - a fresh files-and-database backup with tested recovery before an overwrite; otherwise record RESTORE UNVERIFIED and keep that operation pending
  - an independent review at the exact SHA
  - a tested rollback

**Verification after release:**
- Record counts and spot checks of the newest orders, accounts and subscriptions.
- Check that the next scheduled renewal is still queued once and only once.
- Use the separately isolated payment test path and synthetic data. Never switch a trading store to gateway test mode for this check. Record any unverified live payment outcome.
- Check that edits made in Elementor are visible to logged-out visitors.
- Test navigation and forms.
- Hand over the evidence table and list anything still pending.

**Pitfalls:**
- Trusting a one-click push to merge data.
- Reconciling only orders and forgetting users, subscriptions or form entries.
- Re-enabling cron on staging during testing.
