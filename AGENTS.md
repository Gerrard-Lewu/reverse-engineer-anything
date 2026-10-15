# Working agreement

## Current authority and phase

The user wants spec-driven reverse engineering of Explee for a reusable, privately hosted Ceverio lead-to-meeting tool. **Planning/source investigation only. The application build phase has not started.** Do not scaffold the app, install/run inference weights, provision infrastructure, change DNS, send outreach or create meetings until a later instruction authorizes that phase.

Read [START-HERE.md](START-HERE.md), [the local handover](docs/local-handover.md), [current checkpoint](docs/handover-checkpoint.md), [source completion plan](specs/reverse-engineering-completion.md) and [specification index](specs/README.md) before work. The user's latest answers override older project material.

## GitHub is the source of truth

The user explicitly requires all durable project work to be pushed to GitHub wherever possible. Do not leave a deliverable or the latest checkpoint only on a laptop or cloud workspace.

- Public planning/code repository: `Gerrard-Lewu/reverse-engineer-anything`. It was verified **public** on 15 October 2026; verify again before publishing.
- Proposed private capture repository: `Gerrard-Lewu/explee-private-evidence`. It is a proposed destination, **not a repository created or verified by this handover**. Before collecting authenticated captures, verify it exists and is private, or create it private using the intended Gerrard-Lewu account where authorized access permits. If unavailable, hold private capture collection and record the dependency on GitHub; never substitute the public repo.
- Commit/push reviewed plans, requirements, reusable scripts, sanitized source findings and checkpoint updates at each meaningful completed unit. Pushes within this scope are already authorized; do not ask for routine confirmation again.
- Retain full reviewed private capture bundles/screenshots/source assets in the verified private destination. Check for secrets before any upload, even to a private repository. Credentials, cookies, browser profiles, tokens, private keys and credential stores are never project artifacts to upload.
- Every accepted capture needs a durable private commit or asset reference, file hashes, REA Evidence IDs, scope/limitations and an acceptance record. The public checkpoint contains only sanitized state IDs, coverage, hashes and non-secret references.
- Private data remains private on **every branch**, PR, release and Git LFS object of a public repository. A branch name is not an access boundary.
- Use small commits for text/small evidence; use verified private release assets for larger archives where account limits permit. Do not enable paid storage or Git LFS automatically. GitHub Actions artifacts with expiry are not the only durable copy.
- Stage an explicit reviewed file list, inspect the diff and excluded paths, then push without force. Preserve unrelated user changes. Verify the returned remote commit/ref; for evidence, verify retrievable artifact bytes/hashes.
- If a push/upload fails, preserve the unbacked-up working copy, state the failure, and resume publication when access is restored. Do not report it saved or delete its only copy.

## Local files are temporary working material

Git, browsers, Python/npm and screenshot tools necessarily use disk. The requirement means no **local-only durable project deliverables**. Use a disposable checkout/staging directory; avoid Desktop/Documents downloads as handover outputs. Dependencies, caches and browser runtime state stay outside Git.

Do not delete a staging artifact until its reviewed remote copy and hash have been verified. Never delete user-created files, an existing checkout, or a signed-in browser profile merely to clean up. The owner's browser/credential stores remain machine-managed runtime state; they must not be pushed.

## Source inspection

- Start from the user's signed-in Codex Explee browser. Use Product Design's capture-first guidance and the actual available Browser tools; a visible URL is only context.
- Run real REA MCP beside the reachable browser. The existing helper pins REA 6.4.0; use connected schemas, exact origin/URL/target and an actual literal-loopback endpoint. Do not guess endpoints, expose debugging publicly, or treat cloud localhost as the Windows machine.
- If the native browser does not expose a REA-compatible endpoint, record that fact. Use the dedicated local Chromium profile route only when needed; any required login occurs in the browser, never in chat or copied cookies.
- Existing records/read-only previews are in scope. Do not use source Save/Start/Stop/Send/enrichment purchases or booking creation to manufacture evidence.
- Inspect saved screenshots, DOM/style/layout/asset evidence and responsive states before acceptance. Keep observed, documented, inferred, proposed and unverified facts distinct.
- Synthetic tests establish tooling behavior, not Explee capture or Windows execution. Required missing source evidence blocks faithful UI scaffolding.

## Handover/reporting

Before ending a substantive work session, update the checkpoint and publish all eligible completed work. Report repository/branch, remote commit, verification and the next unresolved action. Prefer GitHub links over local file paths. Never claim publication or capture from an unverified attempt.
