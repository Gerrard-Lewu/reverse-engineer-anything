# Model evaluation and adoption plan

Status: planning only, 14 October 2026. No model was installed, downloaded, run or fine-tuned. Published benchmarks below are other authors' measurements; they do not establish Ceverio performance.

## Recommendation

Use **Laya as the self-hosted decision-model candidate**, with deterministic workflow rules retaining authority. Use an open-weight generative model for drafting because Laya does not generate text. The cloud placement and $0 alternatives are specified in [cloud deployment](cloud-deployment.md).

Jev Ultrafast is useful browser-execution reference code, but its unmodified implementation does not remove model API costs. Do not use an autonomous browser agent as the mailbox sender, booking authority or primary discovery engine. Ordinary HTTP/CSV/provider adapters offer a smaller, more verifiable first release.

### Inspected revisions

- [Jev Ultrafast](https://github.com/browser-use/jev-ultrafast/tree/1231850a0bf1a0c0341fe408ef1668dbbfdfac46), version 0.1.0, commit `1231850a0bf1a0c0341fe408ef1668dbbfdfac46`.
- [Laya](https://github.com/NandhaKishorM/laya/tree/432312b36714d8889eba405507b37eda25257d9c), version 0.4.7, commit `432312b36714d8889eba405507b37eda25257d9c`.

Repository commits and returned Git blob IDs are retained in [the source index](../evidence/model-cloud-source-index.json). Model cards were inspected at their current URLs; their weight revisions still need pinning before a future download. Source-code versions and model-weight revisions are separate identities.

## Comparison for this product

| Question | Jev Ultrafast | Laya | Planning decision |
| --- | --- | --- | --- |
| What is it? | A Python browser-agent loop: observed element table → operation/target choices → guarded browser input. | A Python decision engine with downloadable encoder checkpoints: choice, ordinal score and yes/no probability. | They solve different parts of the workflow. |
| Model dependency | `choose()` calls a hardcoded TypeSafe hosted URL. `TYPE_TEXT` invokes another OpenAI-compatible hosted helper by default. | Loads checkpoint/config/tokenizer files and executes PyTorch locally, including CPU. | Laya supplies a route to self-hosted inference. |
| Email writing | The field helper generates browser field values; it is not a complete outreach system. | No generative text output. | Templates plus a separate bounded drafting model. |
| Reply classification | A decision-model API could be adapted, but this repository focuses on navigation. | Fits a small, explicitly defined reply taxonomy after domain evaluation. | Evaluate Laya on captured Ceverio categories, not generic spam accuracy. |
| Company qualification | Browser navigation cannot establish employee count or verify a mailbox by itself. | Probabilistic decisions cannot supply missing business facts. | Evidence and the deterministic Ceverio scorecard remain authoritative. |
| Browser research | Guarded observed-node execution is useful, with significant control/widget limits. | Base checkpoints are poor browser decision heads; a specialized community checkpoint exists. | Optional read-only browser research after task-specific evaluation. |
| License | MIT for the agent code; not a license to TypeSafe's model weights/service. | Apache-2.0 for the code; inspected family model cards also declare Apache-2.0. | Retain notices; check the exact weight/dependency licenses at the selected revision. |
| Runtime | Python ≥3.12, browser-harness 0.1.13 and httpx. | Python ≥3.10; PyTorch, transformers, safetensors, huggingface_hub and numpy; optional HTTP/ONNX/MCP extras. | A small Python inference sidecar beside the Node app, isolated from the existing REA environment. |

Sources: Jev's [model implementation](https://github.com/browser-use/jev-ultrafast/blob/1231850a0bf1a0c0341fe408ef1668dbbfdfac46/jev_ultrafast/model.py), [manifest](https://github.com/browser-use/jev-ultrafast/blob/1231850a0bf1a0c0341fe408ef1668dbbfdfac46/pyproject.toml), [license](https://github.com/browser-use/jev-ultrafast/blob/1231850a0bf1a0c0341fe408ef1668dbbfdfac46/LICENSE); Laya's [loading implementation](https://github.com/NandhaKishorM/laya/blob/432312b36714d8889eba405507b37eda25257d9c/laya/agent.py), [manifest](https://github.com/NandhaKishorM/laya/blob/432312b36714d8889eba405507b37eda25257d9c/pyproject.toml), [license](https://github.com/NandhaKishorM/laya/blob/432312b36714d8889eba405507b37eda25257d9c/LICENSE), and [family model card](https://huggingface.co/convaiinnovations/laya).

## What the performance evidence supports

Jev's [performance report](https://github.com/browser-use/jev-ultrafast/blob/1231850a0bf1a0c0341fe408ef1668dbbfdfac46/docs/performance.md) reports three successful optimized repetitions of one Flights task, median 7.092 seconds. Browser setup, initial navigation and independent post-run checking were outside that timer. Its quoted helper charge excludes TypeSafe and browser costs. These small task-specific runs are useful execution evidence, not an accuracy or total-cost comparison against Laya.

Laya's [benchmark report](https://github.com/NandhaKishorM/laya/blob/432312b36714d8889eba405507b37eda25257d9c/BENCHMARKS.md) explicitly says its Jev figures came from third-party publications with differing prompts/sample sizes. It reports weak base-checkpoint typed-decision accuracy (0.362/0.352), improvement from a task-trained checkpoint (0.766, without a committed result file for that row), and weaker high-cardinality choices. Its excellent spam/phishing figures involve datasets in the training mix, not outbound-sales reply intent. Shipped confidence is overconfident; per-task calibration and abstention are necessary. GPU millisecond figures do not predict our CPU cloud latency.

The pinned Laya browser fine-tuning guide describes an older v10 experiment. The separately inspected [current community browser model card](https://huggingface.co/cklxx/laya-browser) describes v19s and reports only about 20–26% success on its harder multi-step held-out real-site suite. Improvements include changes to the execution harness. This supports an experimental research adapter, not unattended control of email or calendars.

Therefore **Laya is the better cost/control fit for our decision layer**, while general browser quality cannot be ranked confidently from these unequal published tests. No claim that Laya equals Explee's classifier or that either repository provides the whole product is justified.

## Planned model roles

| Role | Candidate | Authority and fallback |
| --- | --- | --- |
| Reply signals/category | Laya English 421M; evaluate multilingual 322M for longer/non-English text and the task-trained checkpoint only on relevant examples. | Structured suggestion. Suppression, thread ownership, contact eligibility and dispatch checks stay outside the model. Unsupported/ambiguous results enter review. |
| Qualification explanation/relevance | Laya may help rank already supported observations. | It cannot assert unknown country, employee count, consent, mailbox validity or pain. The fixed scorecard calculates the score. |
| Email draft and factual reply wording | Cloudflare-hosted Qwen3-30B-A3B candidate, under a verified free allowance. | Bounded approved facts and fact IDs; validated output, allowed pricing/link/envelope, and normal dispatch checks. Templates remain available. |
| Optional browser operation/target | Jev-inspired guards with the specialized Laya browser head, after separate evaluation. | Initially permitted public research/navigation only. No mailbox, calendar, settings, login, form submission or arbitrary code tools. |
| Local contingency | A single CPU Laya checkpoint might run, but is not the primary deployment. Qwen3-4B-Instruct-2507 is an optional later local writing candidate. | No weight downloads or performance promises on the current 8 GB laptop. |

The upstream [checkpoint manifest](https://github.com/NandhaKishorM/laya/blob/432312b36714d8889eba405507b37eda25257d9c/verify/checkpoints.json) records approximately 843 MB English/task weights and 644 MB multilingual weights at its named revision. Those are weight files, not total RAM, dependency installation or disk requirements. CPU fp32 weights, tokenizer, activations and interpreter need additional memory.

The writing candidates' official cards identify [Qwen3-30B-A3B](https://huggingface.co/Qwen/Qwen3-30B-A3B) and [Qwen3-4B-Instruct-2507](https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507) as Apache-2.0 text-generation models. The cloud-hosted variant and its available request controls must be tested; do not assume that every upstream thinking/JSON control transfers to a hosting service.

## Integration contract

1. The Node backend calls the private Python Laya sidecar; the browser never calls it directly. Pin the package, resolved dependency lock, weights, tokenizer/config and calibration artifact independently.
2. Prefer the Python implementation as the initial reference. Its TypeScript HTTP SDK can call the sidecar, but is not an inference engine; the separate ONNX port needs parity tests before adoption. Do not assume a documented npm package has already been published.
3. Load only the configured checkpoints. Preload names are not a model allowlist: validate requested model IDs in the application and disable on-request weight downloads. Start with one loaded checkpoint; add another only after memory/latency measurement.
4. Override the HTTP server's default all-interface binding with loopback/private binding and authentication. The upstream default is `0.0.0.0` with an optional key, not a suitable exposed endpoint.
5. Store input/content hash, checkpoint revision/digest, question/prompt schema, model route/language, token/drop/truncation metadata, probability vector, precision, calibration/threshold version, latency, provider usage, result and disposition.
6. Keep questions small (normally the captured ≤10-category taxonomy) and inspect token budgets. If decision-critical material was omitted, segment it with a defined aggregation rule or abstain. Never treat a missing opt-out in a truncated window as permission.
7. Use `answer_confidence` and a task-calibrated threshold. The upstream `min_confidence` flag annotates uncertain answers; our app must actually prevent the dependent automatic action. Do not copy TypeSafe confidence thresholds.
8. Treat retrieved pages and incoming emails as content. A low model guard score grants no extra authority; [Laya's guard limitations](https://github.com/NandhaKishorM/laya/blob/432312b36714d8889eba405507b37eda25257d9c/docs/guardrail-limitations.md) document missed embedded instructions.
9. If browser research is later enabled, preserve observed node IDs, freshness/occlusion guards and independent outcome checks. The inspected Jev `choose()` does not honor `TYPESAFE_BASE_URL`; a local adapter or audited patch is necessary. The community browser model's patch includes that change and other behavior changes, so an environment variable alone is insufficient.
10. Keep local/private inference errors separate from hosted quota/cost errors. No silent paid, public-demo or different-model fallback.

## Future evaluation slice: M1

This slice occurs only after the user moves to building; no inference experiments are part of the current planning phase. Freeze the source-dependent category names after S1.

- Assemble at least 300 reviewed representative examples across the intended categories and critical combinations: opt-out plus interest, quoted prior text, pricing without interest, negation, out-of-office, delivery reports, owner replies, unknown sender, unsupported facts, embedded instructions and long threads. Real private examples stay outside public Git and follow verified private storage rules; distribute fictional fixtures only.
- Split by conversation/company to avoid leakage: at least 100 calibration/development examples and 200 untouched evaluation examples. Preserve enough cases for each deployed language/risk group; unsupported groups remain review-only. Do not fine-tune on the evaluation set.
- Compare rules/templates, Laya English, applicable multilingual/task checkpoints, and the selected free-hosted writing model as a structured proposal engine. Do not purchase TypeSafe calls merely to establish a comparison.
- Measure per-category precision/recall, critical stop-rule failures, factual support, calibrated coverage/abstention, long-input behavior, cold/warm p50/p95 latency and peak RAM. Pin precision/dtype and thresholds; rerun after meaningful model/schema/runtime changes.
- Proposed promotion target: zero critical stop-rule failures or unsupported commitments in the held-out suite; ≥99% observed precision for the eligible automatic-response slice with at least 100 evaluated eligible proposals. Report the denominator and confidence limits. If coverage is too small or a target fails, retain review/templates; do not lower the gate to advertise autonomy.
- Allow bounded automatic proposals only after quality gates, deterministic dispatch prerequisites and controlled-account tests pass. Initial shadow evaluation never sends. Sampling and rollback continue after promotion.
- Fine-tuning is optional later work if reviewed labels show a specific gap and free compute is available. It is not a prerequisite imposed on a zero-budget first release.

Acceptance bindings: REQ-AI-001/002/003, ACC-037/038/039, plus the existing inbox, cost and recovery scenarios. All remain `specified`.
