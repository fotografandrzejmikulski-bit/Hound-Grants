# Related Work and Competitive Positioning

_Last updated: 2026-09-05_

## Purpose

HOUND should be evaluated against existing work rather than presented as an isolated invention. This document records the most material overlap identified during pre-submission review.

## MAC-Bench

The June 2026 paper *Beyond Goodhart's Law: A Dynamic Benchmark for Evaluating Compliance in Multi-Agent Systems* introduces MAC-Bench, a dynamic adversarial benchmark for process compliance in multi-agent systems. The associated public repository describes sandbox execution, unified trajectory audit logs, deterministic/hybrid auditing, and the use of SR, CR, CSR, and Machiavelli Gap metrics. citeturn935135academia53turn935135search0

### Direct overlap

| Dimension | HOUND | MAC-Bench | Positioning consequence |
|---|---|---|---|
| Process-level compliance | Yes | Yes | Not novel by itself |
| Dynamic/adversarial scenarios | Yes | Yes | Not novel by itself |
| Stateful sandbox | Yes | Yes | Different implementation must be demonstrated |
| Trajectory logging | Yes | Yes | Not novel by itself |
| CSR | Yes | Yes | Not a novelty claim |
| Machiavellian/Machiavelli Gap | Yes | Yes | Not a novelty claim |
| Deterministic state verification | Central design goal | Present in framework | HOUND should quantify depth/coverage |
| Explicit approval/authorization state | Central design goal | Present in scenarios | HOUND should make state-machine semantics explicit |
| Failure attribution | Central design goal | Less central in available description | Candidate differentiator |
| Cross-domain controlled comparison | Central design goal | Multi-agent/process focus | Candidate differentiator |
| Model/scaffold crossed design | Central design goal | Architecture-sensitive evaluation reported | Candidate differentiator if implemented rigorously |

## Grant strategy

Do not compete on vocabulary. Compete on measurable implementation quality and evidence:

1. deterministic state/invariant coverage;
2. explicit authorization and approval state machines;
3. reproducibility under fixed seeds;
4. model/scaffold attribution;
5. calibrated expert adjudication;
6. failure-cause taxonomy;
7. cost and judge-dependence reporting;
8. transparent comparison against relevant baselines.

## Claim discipline

Until a systematic literature review is completed, the proposal must not say that HOUND is the first, unique, unprecedented, or only benchmark of its kind.

## Key conclusion

The existence of MAC-Bench does not invalidate HOUND. It changes the burden of proof. HOUND now needs to demonstrate a specific, technically measurable contribution beyond general process-compliance benchmarking and the already-published CSR/MG framework.
