# Hostinger: native WordPress recovery and failure handling

Load this reference only for a verified Hostinger target. It supplements the main workflow; it does not authorise a hosting connection, purchase, overwrite or release.

## Contents
- [Bind the target](#bind-the-target)
- [Choose a supported route](#choose-a-supported-route)
- [Prepare the private target](#prepare-the-private-target)
- [Diagnose failures](#diagnose-failures)
- [Verify and release](#verify-and-release)
- [Current provider references](#current-provider-references)

## Bind the target

Before a write, record the authorised account, hosting product/plan, source and destination domain, document root, WordPress installation identity, database identity (no secret values), current PR/head, and permitted action. Reconfirm the selected site after navigation. A similarly named subdomain is not sufficient identification.

Distinguish shared/cloud WordPress hosting, Agency hosting, VPS, and Website Builder/Horizons. Native WordPress recovery requires PHP plus a database; uploading HTML to a static destination does not preserve Elementor editing. A missing Hostinger response header is not evidence of another provider: proxies/CDNs may remove it. Use account/site records.

Inventory disk and inode capacity, database size, backup availability/retention, PHP compatibility and effective limits, SSH/SFTP availability, DNS authority, TLS, plugin licences and integrations. Preserve the current live routing while preparing the preview.

## Choose a supported route

1. Discover available connector operations and read their current schema. Bind product-specific identifiers from observed account data. Hosted and local connector capabilities can differ. A missing operation can mean unavailable capability, a product mismatch or access scope; it does not by itself prove the product is disabled.
2. Prefer the authorised native WordPress staging/migration route where its data effects meet scope. Use hPanel for supported operations absent from the connector; use an already authorised CLI/SSH route where appropriate. Do not use another route to bypass a policy denial.
3. Determine whether an operation copies files, database, both, or only a theme/plugin. Verify what already exists at the destination and what the operation overwrites. Do not feed an arbitrary archive into a full-site deployment endpoint.
4. Treat upload completion, migration-job completion, native site health and release acceptance as separate facts. Record job IDs and inspect actual status before retrying. Resuming an upload or overwriting a file is not proof that a database import or installer is idempotent.
5. Keep API credentials, signed upload URLs and SSH details in approved secret channels. Do not place them in commands that will be logged, screenshots, GitHub, this skill or a public troubleshooting service.

Provider constraints checked 2026-11-04; recheck the current account and official pages at execution:
- Native staging currently requires Business or above, uses a different Agency flow, and excludes Multisite. Subdomain sources need a manual staging route. External DNS may need a preview record in the authoritative zone.
- “Publish” replaces the live files and database; later live changes can be lost.
- “Copy Website” is separate from staging. It overwrites the target, works within one plan, and targets domains/subdomains rather than folders. Mailboxes, FTP accounts and SSH keys are not included.
- If the plan cannot meet the requirement, use an authorised isolated alternative or return the exact plan/access decision. Never purchase an upgrade automatically.

## Prepare the private target

Use this order; preserve isolation even if a provider defaults to immediately running a clone.

1. **Backup:** Verify a coherent files/database snapshot, restore method, retention and authorised private storage. A listed backup or downloaded archive alone is not a restoration test. Keep a manifest with identifiers, timestamps and checksums where available; exclude secret content.
2. **Containment before execution:** Provision a separate target and database. Establish access restriction and prevent outbound mail, payments, webhooks, CRM writes and scheduled work before imported code can execute. If one-click cloning cannot provide this, choose a supported method that stages data with containment before enabling the runtime. Apply the data mode in step 3; isolation does not require deleting customer records. Do not run the clone first and disable integrations afterwards.
3. **Credentials/data:** Bind the data mode explicitly. A sanitised development preview uses a separate test copy with synthetic users/content and no production secrets. An authorised full-migration destination preserves required real users, orders, submissions and content intact inside the approved private boundary, with access control and outbound isolation; do not sanitise away those required records. Never substitute a sanitised/synthetic database at production cutover. Deliberately migrate or re-provision necessary secrets through approved channels. Never infer an unknown secret from a masked value or replace an environment-variable set with masked placeholders.
4. **TLS and access:** Verify the real host and certificate, document root and relevant aliases. Keep TLS verification enabled. Check preview root, known child routes and assets anonymously and with authorised authentication. Verify sensitive-file denials without fetching their bodies.
5. **Native recovery:** Import only the agreed source; verify media, Elementor kits/templates, display conditions, fonts/icons and supported dependencies. Perform any required URL repair with serialization-aware tooling and a scoped dry run. Confirm affected rows and repeatability before applying.
6. **Readback:** Verify the applied file/configuration identity and WordPress/PHP runtime. Do not infer success from a saved editor, a completed upload, an HTTP status alone or a visible screenshot.
7. **Cache:** Identify Elementor-generated assets, WordPress/LiteSpeed, provider/CDN and browser caches. Purge only the authorised target layers when justified; confirm the served revision. Verify private responses cannot be served from a shared public cache.

## Diagnose failures

For each symptom capture the route, timestamp, environment, exact version and a redacted observation. Choose the smallest discriminating check. Stop a failing method after repeated identical failures; reconcile state before trying a different supported method.

| Symptom | Check first | Bounded repair and proof |
|---|---|---|
| Password prompt repeats or appears twice | Actual host/realm, HTTP-to-HTTPS or alias redirects, parent/child directory protection, document root and existing owner login | Preserve working credentials. Inspect only the relevant protection configuration through admitted administration. Resolve overlapping protection or target mismatch with a rollback. Verify both anonymous denial and authenticated rendering separately. Do not remove protection, reset passwords unnecessarily, or bypass a protected-browser denial. |
| Preview root is private but child/asset/alias is public | Authentication inheritance, alternate document roots and cached public responses | Protect every applicable route at the appropriate boundary, invalidate affected public cache, then retest exact paths/aliases. Noindex and an obscure URL are not substitutes. Preserve unrelated provider rules. |
| 403, WAF challenge, or denied admin/API request | Distinguish intentional sensitive-file denial, server permissions, WAF and platform policy; use redacted request ID/logs | Keep expected denials. For a false positive, use a narrow supported exception within scope or provider support. Never globally disable WAF, grant 777 permissions, expose configuration, or evade a platform denial. |
| Blank page/500 after a code edit | Exact changed file, PHP syntax/version, plugin/theme compatibility and bounded error logs | Roll back the known change through the admitted admin/file route; lint on compatible PHP and test isolated runtime before reapplying. A must-use plugin parse error can fail before its environment guard executes. Do not reset all plugins or overwrite the database to repair one file. |
| Database connection error | Correct target database/user binding, grants, prefixes and host documented for this runtime | Correct only verified configuration through the secret channel; validate connectivity without printing credentials. Do not substitute an external database hostname based on guesswork or share wp-config contents. |
| Import hangs, times out, or returns 413/5xx | Job state, partial tables/files, archive integrity, effective PHP/upload/time limits, disk and inodes | Reconcile what actually completed; use a compatible supported transfer/import route. Adjust only justified target limits within scope. Never blindly replay the installer or assume a retry cannot duplicate content. |
| Broken icons, fonts, templates or editor-only styling | Network responses; custom-font/icon files; Elementor/Pro/add-on versions and licences; generated CSS; URL origin; template conditions | Restore the needed supported assets/settings, regenerate target assets where appropriate and verify native editor plus frontend. Trace CORS precisely; do not add wildcard access or disable TLS as a generic fix. |
| Hover is absent or layout shifts | Computed selectors, overlays, omitted motion scripts, transform conflicts, source settings, touch and reduced-motion state | Repair the narrow source cause; provide focus/touch behavior and reduced-motion handling. Compare matched viewports and test actual interactions, not just a screenshot. |
| Saved fix does not appear | Correct site/path, applied bytes/revision, cache headers, generated asset dependencies | Read back source and served revision; purge only the affected target caches. Do not reinstall/reimport the site to clear a stale asset. |
| Redirect loop, mixed content or old domain appears | WordPress home/site URLs, scoped serialized references, TLS, proxy HTTPS signaling, root/folder mismatch and redirect rules | Repair the specific mismatch; preserve GUID policy and provider rules. Test canonical paths and login through the intended TLS endpoint. Do not publish hosts-file workarounds or use curl -k. |
| Preview sends mail, renews subscriptions or updates CRM | Runtime services, production credentials, scheduler and callback routes | Contain outbound effects immediately inside existing authority; record actual events without claiming recall/undo. Reconcile with the project owner and test using synthetic services before resuming. A disabled form is not sufficient. |
| Wrong site changes or target data disappears | Selected account/domain/root and operation scope | Stop mutations; preserve logs and state. Restore only the verified affected target under its recovery authority. Do not continue a broad restore against a guessed database or overwrite newer live transactions. |
| DNS change breaks website or email | Authoritative zone, A/AAAA, CDN/proxy, TLS, MX, SPF, DKIM, DMARC and verification records | Compare against the recorded zone; apply/roll back only authorised records. Verify web and mail separately. Do not replace the whole zone just to point a website. |
| Staging works but publishing loses live updates | Staging snapshot time, current live orders/users/content and actual publish semantics | Avoid full database replacement unless the approved freeze/delta process reconciles all intervening changes. Prefer a tested bounded code/config release when that is the actual scope. Reconcile external payment events too. |
| Login/connector/SSH is unavailable | Exact account, permission scope, session state and the observed error | State the smallest required reconnection or owner action. Continue permitted source work; keep runtime acceptance pending. Do not turn an access error into an instruction to buy hosting or repeatedly reset working credentials. |

## Verify and release

Collect these separately:
- **Source:** reviewed commit, deployment diff, licences/dependencies and rollback identity.
- **Runtime:** relevant PHP checks; WordPress and Elementor editing/save behavior; affected routes/assets and integration boundary.
- **Access:** unauthenticated denial, authenticated rendering, TLS, sensitive-file denial and cache privacy. An authenticated admin page does not prove frontend acceptance.
- **Experience:** screenshots at matched viewports; mobile overflow, keyboard/focus, touch, hover and reduced motion; actual agreed-browser results.
- **Data:** copied/sanitised scope, matched backups and any live delta reconciliation. Never claim customer-data continuity from page appearance.
- **Release:** exact approved target/actions, DNS/redirect/mail impact, tested recovery, final live smoke checks and owner handover.

Publish only after the relevant checks and existing owner release authority cover the concrete action. Adapt preview-only guards deliberately. Do not blindly carry disabled integrations into production or accidentally enable them during preview. If a check is blocked, return the precise evidence gap and finish independent authorised work.

## Current provider references

Use current official guidance and the actual installed/account versions. Provider instructions explain mechanisms; they do not override the site's protection or authorised scope.

- [WordPress staging](https://www.hostinger.com/support/5720286-how-to-create-a-wordpress-staging-environment-in-hostinger/) — eligibility, target limits and destructive publish semantics.
- [Copy Website](https://www.hostinger.com/support/6601521-how-to-copy-a-wordpress-website-to-another-domain-name-in-hostinger/) — copy/overwrite scope and omitted hosting services.
- [Directory protection](https://www.hostinger.com/support/1583470-how-to-password-protect-a-website-in-hostinger/) — current hPanel feature. Some troubleshooting steps remove protection; do not apply those steps to expose a private preview.
- Discover API/connector documentation from the current installed integration or Hostinger's official documentation links; do not invent endpoint names or assume every account exposes every operation.
