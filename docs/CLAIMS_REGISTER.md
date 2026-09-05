# HOUND Claims Register

This register is a submission-control document. It exists because the supplied proposal contains many current or externally attributable claims that require source verification before they can be presented as established facts.

## Status codes

- **VERIFIED** — supported by a primary or authoritative source reviewed for the submission.
- **PENDING** — plausible or author-supplied but not yet sufficiently verified.
- **REMOVE/REWRITE** — unsupported, internally inconsistent, misleading, or too specific to retain without evidence.

| Claim / statement in supplied proposal | Status | Required action |
|---|---|---|
| AI cyber task horizons have recently accelerated, including a 4.7-month doubling estimate | VERIFIED | Cite AISI directly; preserve caveat that the estimate concerns a narrow cyber suite and reliability threshold. citeturn153512search2 |
| Frontier cyber systems have recently exceeded previous AISI trend projections | VERIFIED | Cite AISI and avoid generalizing from the narrow suite to all real-world cyber work. citeturn153512search2 |
| SWE-bench Verified has contamination problems | VERIFIED | OpenAI explicitly reported contamination and stopped reporting the benchmark for frontier coding capability. citeturn153512search0 |
| SWE-bench Pro is fully reliable / uncontaminated | REMOVE/REWRITE | Do not claim this. OpenAI later reported widespread task problems and estimated about 30% of tasks were broken. citeturn153512search1 |
| 'Vals AI Fellowship 2026' provides unlimited API credits, GPU budget, Human Data Budget, San Francisco workspace, or fixed weekly stipend | PENDING | Verify against the official program terms before submission. Do not represent assumptions as benefits. |
| Specific 2026 frontier model names and benchmark scores in the original proposal | PENDING | Verify each model/version and each score against a primary benchmark source, or remove. |
| 'Claude Fable 5', 'Claude Opus 4.8', 'Gemini 3.5 Flash', 'GPT-5.5', 'GLM-5.2' scores in supplied Table 1 | PENDING | Verify model existence/version, benchmark definition, date, and source. Several entries should not appear without primary citations. |
| 'Vals Legal AI Report (VLAIR)' and exact legal benchmark results | PENDING | Verify report existence, publisher, methodology, and table values against the primary publication. |
| 'Vals AI Excel Modeling Benchmark (EMB)' and exact scores/costs | PENDING | Verify primary benchmark source and public availability before citing. |
| 'Herculean' benchmark claims and results | PENDING | Verify benchmark identity, source, sample, and methodology. |
| 'DiscoveryWorld' results and exact human/AI percentages stated in the proposal | PENDING | Verify against benchmark paper/source and date. |
| 'Corral' 25,000 trajectory analysis and exact percentages | PENDING | Verify primary study and whether the percentages are correctly attributed. |
| CyberGym / CyBench exact 2026 comparative speed/cost ratios | PENDING | Verify each figure, denominator, experimental setup, and publication date. |
| Claude Opus 4.6 reproduced vulnerabilities in nearly 90% of 1,507 instances | PENDING | Verify exact benchmark, model/version, sample size, and result. |
| Locked Shields 2026 completion-time comparison | PENDING | Verify primary event/evaluation source and scope. |
| RODO/GDPR, PIPL, ISO 42001, DORA, NYDFS Part 500 implications | PENDING | Legal review required. Do not describe specific compliance consequences without jurisdiction-appropriate sourcing. |
| Fortune 500 deployment risk / commercial claims | PENDING | Rewrite as intended audience/value proposition unless backed by evidence. |
| '40% of corporate enterprise agent deployments' will be discontinued/declassified | REMOVE/REWRITE | Remove unless an authoritative forecast is identified. Present as a hypothesis or risk scenario instead. |

## Submission rule

No `PENDING` item may remain in the final public grant narrative as an unqualified factual claim. Either attach a primary citation, explicitly label it as a project hypothesis/projection, or remove it.

## Current verified evidence base

The strongest externally verified claims currently supporting the project rationale are the AISI findings on rapidly advancing autonomous cyber capability and the OpenAI disclosures about benchmark contamination and benchmark-quality failures. citeturn153512search2turn153512search0turn153512search1
