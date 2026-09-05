# Originality and Positioning

## Why this document exists

The supplied grant narrative presents HOUND as a new benchmark for procedural compliance under execution pressure. A 2026 paper, *Beyond Goodhart's Law: A Dynamic Benchmark for Evaluating Compliance in Multi-Agent Systems*, introduces MAC-Bench and explicitly uses closely overlapping problem framing and terminology, including procedural compliance, dynamic/adversarial environments, Compliance-Weighted Success Rate (CSR), and Machiavellian Gap (MG). citeturn445634academia72

The HOUND submission must therefore avoid an absolute novelty claim until a formal prior-art review is complete.

## Defensible positioning

HOUND can be differentiated by specifying a narrower and testable contribution, for example:

1. **Execution-grounded state verification:** scoring observable environment mutations and authorization events rather than relying primarily on generated text.
2. **Cross-domain policy execution:** one benchmark framework covering synthetic legal, financial, scientific, and cyber/IT workflows with domain-specific policy sets.
3. **Independent deterministic controls:** using environment invariants and event logs wherever possible, minimizing dependence on an LLM judge for consequential compliance decisions.
4. **Failure attribution:** distinguishing incompetence, uncertainty, tool failure, policy violation, and strategic shortcutting rather than collapsing them into one score.
5. **Reproducible trap calibration:** publishing scenario generators, policy schemas, seed management, and evaluation controls so adversarial pressure can be reproduced.

These are positioning hypotheses, not claims that the literature already proves HOUND is unique.

## Required before submission

Complete a structured literature review covering dynamic agent benchmarks, policy-compliance evaluation, tool-use safety, reward hacking/Goodhart evaluation, long-horizon agent evaluation, and the specific MAC-Bench lineage. Record competing systems, publication dates, overlapping metrics, environment design, and the exact differentiator HOUND adds.

## Language rule

Avoid phrases such as “unprecedented,” “first,” “only,” “unique,” or “new standard” unless supported by a documented systematic review. Prefer measurable language such as “we propose,” “we evaluate,” “we operationalize,” and “we test whether.”
