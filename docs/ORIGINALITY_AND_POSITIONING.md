# Originality and Positioning

## 1. Purpose

This document defines how HOUND should be positioned against related work. It is intentionally conservative: novelty is treated as a claim that must be demonstrated, not assumed.

## 2. Material Prior Work

A June 2026 paper, *Beyond Goodhart's Law: A Dynamic Benchmark for Evaluating Compliance in Multi-Agent Systems*, introduces MAC-Bench. Its public repository describes a dynamic adversarial framework for process compliance with sandbox environments, trajectory audit logs, deterministic/hybrid auditing, and metrics including SR, CR, CSR, and Machiavelli Gap. citeturn935135academia53turn935135search0

This creates direct conceptual overlap with the original HOUND proposal. In particular, HOUND must not claim to be the first benchmark to:

- evaluate procedural compliance during agent execution;
- use dynamic or adversarial sandbox environments;
- use trajectory-level auditing;
- use Compliance-Weighted Success Rate (CSR); or
- use Machiavellian/Machiavelli Gap terminology.

## 3. Defensible HOUND Contribution

HOUND should instead make a narrower, experimentally falsifiable claim:

> HOUND proposes a benchmark architecture centered on independently verifiable environment-state mutations, explicit authorization and approval state, deterministic invariants, and cross-domain failure attribution, with CSR/MG used as summary diagnostics rather than as the novelty claim itself.

The proposed differentiators are:

1. **State-first verification.** Policy-relevant claims should be grounded in explicit state transitions, authorization events, approval state, and provenance records.
2. **Deterministic-first evaluation.** Consequential scoring should be deterministic wherever the environment can make the property machine-checkable.
3. **Attribution.** Failures should be classified across incompetence, retrieval/provenance error, tool failure, environment fault, authorization violation, approval violation, and outcome/compliance divergence.
4. **Cross-domain experimental controls.** The same evaluator architecture should be tested across synthetic finance, legal/document, science/analysis, and cyber/IT workflows while keeping domain policies explicit and versioned.
5. **Model/scaffold separation.** Experimental design should cross model and scaffold variables so benchmark results do not accidentally become a measure of orchestration quality alone.
6. **Contamination-aware release.** Development, calibration, demonstration, and held-out evaluation sets should be separated and versioned.

These differentiators remain hypotheses until implemented and compared empirically with relevant baselines.

## 4. What HOUND Must Demonstrate

A strong originality case requires an implemented vertical slice and an empirical comparison against at least one established process-compliance benchmark or reproduction of its core evaluation setup. The comparison should report:

- task-success measurement;
- compliance measurement;
- state/invariant coverage;
- judge dependence;
- seed/replay reproducibility;
- model/scaffold sensitivity;
- failure attribution resolution;
- evaluation cost.

## 5. Language Rule

Do not use “first,” “unprecedented,” “only,” “unique,” “new standard,” or similar absolute novelty language without a systematic literature review and documented comparative evidence.

Prefer:

- “we propose”;
- “we operationalize”;
- “we measure”;
- “we test whether”;
- “we compare”; and
- “we evaluate the extent to which.”

## 6. Strategic Grant Position

The grant case should not depend on winning a novelty contest against MAC-Bench. The stronger case is that HOUND addresses a concrete evaluation need with a state-verifiable, reproducible, cross-domain experimental design and that its claims will be validated rather than asserted.
