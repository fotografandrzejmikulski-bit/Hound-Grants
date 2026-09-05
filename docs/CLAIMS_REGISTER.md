# Claims Register

This register separates externally checkable factual claims from project definitions, hypotheses, and projections. It is a submission-control document, not a claim that every statement in the original proposal is independently verified.

## Status vocabulary

- **VERIFIED** — checked against a credible primary or near-primary source.
- **PARTIAL** — the general claim is supported, but the exact figure, date, model/version, or wording needs additional verification.
- **UNVERIFIED** — not yet independently verified.
- **PROJECT DEFINITION** — a term, metric, architecture, or requirement introduced by HOUND itself.
- **PROJECTION** — a future expectation or target rather than an observed fact.

## Priority claims

| Claim area | Current status | Submission action |
|---|---|---|
| Vals AI VLAIR exists and evaluates legal-AI workflows against a lawyer baseline | VERIFIED | Cite the official report in final grant materials. |
| Vals AI Excel Modeling Benchmark exists and evaluates working financial models | VERIFIED | Cite the primary Vals source; do not rely solely on social reposts. |
| Exact 2026 model names, leaderboard positions, and prices in the supplied proposal | PARTIAL/UNVERIFIED | Verify each item individually at the cited primary source and record retrieval date. |
| The original proposal's statement that HOUND is a 'pioneering' or 'unprecedented' benchmark | UNVERIFIED | Replace with a narrower novelty claim after prior-art review. |
| CSR and Machiavellian Gap as HOUND metrics | PROJECT DEFINITION | Present as HOUND's proposed metrics unless the literature review establishes prior use. |
| HOUND's six-month implementation plan | PROJECTION | Present as a proposed work plan, not an achieved capability. |
| 300 expert scenarios | PROJECTION | Present as the planned corpus size; specify sampling and power rationale during study design. |
| Unlimited API credits, GPU budget, human-data budget, office access, or other program benefits attributed to a fellowship | UNVERIFIED | Do not state as guaranteed until confirmed by the official program terms. |
| Regulatory requirements associated with GDPR/RODO, PIPL, DORA, NYDFS Part 500, ISO/IEC 42001 | PARTIAL | Verify jurisdiction, applicability, exact clause/scope, and current version before using each as a scoring rule. |
| Cybersecurity performance ratios and autonomous offensive/defensive claims from the original proposal | UNVERIFIED | Recheck against original benchmark papers/reports; omit unsupported ratios from the executive summary. |
| Scientific benchmark figures for ScienceWorld, DiscoveryWorld, Corral, CyBench/CyberBench, etc. | UNVERIFIED | Verify exact benchmark, version, model, task set, and date before publication. |
| HOUND must use synthetic isolated environments with no production credentials or real targets | PROJECT REQUIREMENT | Keep as a hard safety boundary. |

## Novelty warning

A 2026 paper titled **“Beyond Goodhart's Law: A Dynamic Benchmark for Evaluating Compliance in Multi-Agent Systems”** describes MAC-Bench and explicitly discusses procedural compliance, adversarial pressure, CSR, and the Machiavellian Gap. This materially overlaps the supplied HOUND framing. The final proposal therefore must identify the differentiating contribution of HOUND instead of claiming an unexplored problem space. citeturn445634academia72

## Evidence notes

The VLAIR record is externally corroborated as a Vals AI legal evaluation program. A primary report available through UC Berkeley's hosted copy describes four evaluated products, 200 U.S. legal research questions, weighted criteria, and the lawyer baseline. citeturn445634search71

Vals AI's Excel Modeling Benchmark is also externally corroborated: Vals AI describes the benchmark as evaluating complete, working financial models, with Excel recalculation before grading; its published results include Claude Opus 4.8 at 69.4%, Claude Sonnet 5 at 66.3%, and GPT-5.5 at 64.5%. citeturn445634search3

These verified examples do **not** automatically verify the remaining numerical claims in the original proposal. Each must be traced separately.
