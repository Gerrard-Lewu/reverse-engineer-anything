# Explee investigation and internal-tool blueprint

This repository contains a source-backed product and technical blueprint, a spec-driven build plan for a reusable personal lead-to-meeting tool, and a tested REA capture kit. The first business profile is Ceverio. The application has not been built.

Current phase: **planning**. Application implementation has not started; the build sequence is a proposal for the later build phase.

**Continuing locally:** read [START-HERE.md](START-HERE.md), [the Windows/Codex handover](docs/local-handover.md) and [current checkpoint](docs/handover-checkpoint.md). [AGENTS.md](AGENTS.md) records the user's GitHub-first requirement: push eligible completed work and checkpoints; use a verified private destination for authenticated evidence. Local checkouts/staging are temporary, not the durable project archive.

**Source coverage is partial.** Official product material and selected public API contracts were retrieved. The signed-in Explee application on the owner's computer has not been captured, so visual fidelity, private requests, and interactive behavior remain unverified.

## Read the result

- [Current build specification](specs/README.md), [execution sequence](specs/build-plan.md), and [user decisions/dependencies](specs/decisions.md).
- [Jev/Laya comparison and model evaluation](specs/model-evaluation.md), [whole-cloud deployment plan](specs/cloud-deployment.md), and [retained source pointers](evidence/model-cloud-source-index.json).
- [Explee reverse-engineering completion plan](specs/reverse-engineering-completion.md), [remaining layers](specs/remaining-layers.md), and [current DNS status and steps](specs/dns-cutover.md).
- [Current read-only DNS comparison](evidence/dns-followup-source-index.json) and [historical infrastructure findings](evidence/remaining-layers-source-index.json).
- [Traceable requirements](specs/requirements.md) and [Given/When/Then acceptance scenarios](specs/acceptance.feature).
- [Product blueprint and feature coverage](docs/blueprint.md).
- [Official source inventory](docs/source-inventory.md).
- [Proposed architecture and data model](docs/internal-tool-architecture.md).
- [Implementation roadmap and acceptance checks](docs/implementation-roadmap.md).
- [Local REA capture instructions](docs/local-capture.md).
- [Source capture checklist](docs/source-capture-checklist.md).
- [Verification results](docs/verification.md).
- [Evidence index](evidence/index.json) and [documented public operations](evidence/public/documented-operations.json).

The current release target is private cloud operation: proposed Oracle Always Free app/worker and Laya inference, Cloudflare drafting/private access subject to free-plan verification, and the selected Explee REA Supabase project. REA Org access and that project's Free plan/metadata are now confirmed; app schema/host connectivity remain future work. Published cloud limits do not establish other account entitlements. Source capture and live provider prerequisites remain pending; no cloud resource was created.

The user reports an Oracle Free Tier account in Ashburn. On 15 October, native Cloudflare MCP confirms ceverio.com is active and all seven mail records plus two CNAMEs match the supplied GoDaddy export. DNSSEC is pending; the user has not yet added the Cloudflare DS at GoDaddy. The export's symbolic WebsiteBuilder Site A value prevents literal website-IP parity. Parent-chain/live website/mail checks remain outstanding. Access was not enabled at the 14 October inspection. This work made no infrastructure changes or app build.

## Capture the signed-in reference

The helper runs on the same computer as a Chromium-family browser with a loopback debugging endpoint. It starts its own REA 6.4.0 MCP connection; no persistent Codex configuration changes are needed. It selects the exact requested URL, observes passively, saves the screenshot and complete REA records, and exports retained session evidence even when a capture fails.

Use an existing Python 3.11+ and a supported Node.js/npm installation. REA supports Node 22.19+, 24.11+, or 26+ within its declared release ranges.

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
npx -y rea-agents@6.4.0 --version
.venv/bin/python scripts/capture_explee.py --cdp-endpoint http://127.0.0.1:9222 --output evidence/captures/01-project-desktop --analyze-bundle
```

On Windows use `.venv\Scripts\python.exe` for the Python commands. See [local capture](docs/local-capture.md) for browser startup and state-by-state collection.

The saved `receipt.json` distinguishes `captured`, `partial`, and `failed`. `captured` means the selected artifacts were collected within their stated scope; it does not mean every Explee feature, prior request, or same-URL UI state was observed. REA's full completeness records remain attached.

## Verify the kit

```bash
python3 -m unittest discover -s tests -v
python3 tests/verify_capture_integration.py
```

The second command is a POSIX-only integration harness using real Chromium and REA against a synthetic local page. It verifies the capture machinery, not Explee. Raw private captures and runtime verification artifacts are excluded from this public repository by default; the handover requires verified private evidence publication and sanitized public checkpoints.
