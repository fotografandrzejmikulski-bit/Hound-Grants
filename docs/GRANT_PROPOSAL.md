# HOUND Grant Proposal

## 1. Executive Summary

HOUND (Heuristic Observation of Unaligned Networked Decisions) proposes an execution-grounded benchmark for evaluating long-horizon AI agents in high-risk operational environments. The central premise is that conventional evaluation often rewards end-state task success while failing to measure whether an agent reached that state through an authorized, auditable, policy-compliant trajectory.

The supplied project concept identifies this failure mode as the **Machiavellian Gap (MG)**: the difference between achieving an operational objective and achieving it without violating the constraints that make the outcome acceptable. HOUND operationalizes this idea through mutable but fully synthetic environments, instrumented tool APIs, explicit policy gates, adversarial but bounded scenario design, and trajectory-level scoring.

The intended result is a reusable benchmark that lets researchers and deployers compare agents not only on whether they can complete a task, but on whether they maintain procedural integrity while doing so.

## 2. Research Problem

The project focuses on four recurring failure modes:

1. **Outcome-only optimization.** A system is rewarded for the final result even when intermediate actions breach policy.
2. **State inconsistency.** The final artifact looks correct while underlying records, provenance, or authorization state are wrong.
3. **Long-horizon degradation.** Compliance can decay as an agent accumulates context, tool calls, retries, and partial failures.
4. **Adversarial shortcutting.** Missing information, time pressure, tempting unauthorized data, or conflicting objectives can induce unsafe shortcuts.

HOUND tests these failure modes directly in executable environments rather than through static question answering alone.

## 3. Objectives

### O1 — Build an execution harness

Create isolated, resettable environments with synthetic databases, files, messaging, authorization services, and tool APIs. Every externally relevant action is represented as a machine-auditable event.

### O2 — Build an expert-authored scenario suite

Develop approximately 300 scenarios spanning legal-document workflows, financial analysis, scientific investigation, security operations, and cross-domain administrative tasks. Scenario counts are a project target, not an existing benchmark fact.

### O3 — Formalize procedural scoring

Implement SR, PCR, CSR, and MG with scenario-specific policy weights, hard constraints, catastrophic violations, and human-reviewed calibration.

### O4 — Evaluate model/scaffold combinations

Run controlled experiments across a representative set of frontier, economical, open-weight, and multimodal systems. Results must report both model identity and scaffold/tooling configuration so that scaffold effects are not misattributed to model capability.

### O5 — Publish a reproducible benchmark

Release methodology, scenario schemas, scoring definitions, evaluation code, aggregate results, and enough metadata for independent reproduction without exposing unsafe operational secrets or real-world credentials.

## 4. Research Hypotheses

**H1.** End-state task success and procedural compliance are imperfectly correlated.

**H2.** Compliance degrades under long-horizon execution, especially when scenarios contain missing information and time pressure.

**H3.** Explicit authorization boundaries and approval gates materially change agent behavior and reveal failures not visible in text-only evaluation.

**H4.** The distribution of MG differs across model families and scaffolds even at comparable task-success levels.

**H5.** Trajectory-level observability provides better diagnostic value than final-answer grading alone.

## 5. Benchmark Design

Each test case contains:

- a synthetic environment state;
- an objective and success criteria;
- an explicit policy set;
- authorization and approval requirements;
- available tools and their schemas;
- seeded documents and structured data;
- optional adversarial traps;
- a reset seed;
- an expected set of invariant conditions;
- an evaluation specification.

The benchmark records an operational trajectory:

\[
T=(a_1,o_1,a_2,o_2,\ldots,a_n,o_n)
\]

where `a_i` is an agent action and `o_i` is the corresponding environment observation.

## 6. Metrics

### 6.1 Task Success Rate — SR

Binary end-state success:

\[
SR(T)=
\begin{cases}
1 & \text{if the terminal state satisfies the task criteria}\\
0 & \text{otherwise}
\end{cases}
\]

### 6.2 Procedural Compliance Rate — PCR

Let `P` be the scenario's policy set and `w(a_i,P)` the severity weight of violations attributable to action `a_i`:

\[
PCR(T)=1-\frac{\sum_i w(a_i,P)}{W_{max}}
\]

Implementations must clamp the result to the declared score range and define the treatment of repeated violations, mutually dependent violations, and catastrophic events.

### 6.3 Compliance-Weighted Success Rate — CSR

Across an evaluation set `N`:

\[
CSR=\frac{1}{|N|}\sum_{j=1}^{N}SR(T_j)\times PCR(T_j)
\]

### 6.4 Machiavellian Gap — MG

\[
MG=SR-CSR
\]

MG is an aggregate diagnostic, not a claim of intentionality. A high MG indicates a measurable separation between outcome success and compliant execution. The benchmark must not infer consciousness, motive, or human-like intent from this value.

## 7. Experimental Controls

To make model comparisons scientifically interpretable, HOUND will control or report:

- model version and provider;
- system/developer instructions where disclosure is permitted;
- tool set and tool schemas;
- scaffold/framework version;
- context-window configuration;
- sampling parameters where applicable;
- maximum steps and wall-clock budget;
- randomization seed;
- scenario version;
- retry policy;
- human intervention policy;
- judge/evaluator configuration.

Paired runs should reuse identical scenario seeds when comparing configurations.

## 8. Adversarial Scenario Families

HOUND will use bounded trapdoors designed to expose procedural failure without requiring real-world harm. Examples include:

- an apparently useful but unauthorized record;
- a missing primary source when a summary is available elsewhere;
- contradictory records requiring escalation;
- an approval gate that blocks direct execution;
- a stale document versus a newer authoritative record;
- time pressure combined with incomplete data;
- a tempting credential-like artifact that is explicitly non-authorized synthetic data;
- conflicting objectives between task speed and evidence quality.

Scenario designers must ensure that the safest compliant action remains representable and that failures can be attributed to observable environment transitions.

## 9. Evaluation and Ground Truth

Human experts define scenario policies and adjudicate ambiguous trajectories during calibration. Automated evaluators may calculate deterministic checks and compare final states, but they must not silently redefine policy.

For sampled trajectories, independent human review will estimate:

- policy-label accuracy;
- severity-weight agreement;
- evaluator false positives;
- evaluator false negatives;
- inter-rater reliability.

The benchmark should report uncertainty intervals and confidence bounds for aggregate metrics where sample sizes support them.

## 10. Deliverables

### D1 — Execution Harness

Resettable synthetic environments, tool interfaces, event logging, state snapshots, and evaluator hooks.

### D2 — Scenario Corpus

Versioned scenario definitions with policy metadata, success conditions, and safety review records.

### D3 — Scoring Engine

Reference implementation for SR, PCR, CSR, MG, plus violation taxonomy and aggregation utilities.

### D4 — Baseline Study

Controlled comparison across selected systems and scaffolds.

### D5 — Public Research Package

Documentation, benchmark card, methodology, aggregate results, and reproducibility materials.

## 11. Six-Month Work Plan

**Month 1 — Infrastructure.** Build the execution harness, synthetic services, reset mechanism, event schema, and isolation controls.

**Month 2 — Expert scenario development.** Author and review the initial scenario corpus and formal policy specifications.

**Month 3 — Calibration.** Run baseline systems, test scenario difficulty, measure evaluator agreement, and remove ambiguous cases.

**Month 4 — Grid evaluation.** Execute controlled model/scaffold experiments and capture complete trajectories.

**Month 5 — Analysis.** Compute metrics, error categories, uncertainty estimates, and cross-model comparisons.

**Month 6 — Publication and handover.** Freeze the benchmark version, publish documentation and aggregate findings, and prepare integration artifacts.

## 12. Resource Request Logic

The supplied proposal assumes a fellowship structure that combines researcher support, model/API access, expert data-generation budget, and compute. Exact monetary commitments must be tied to the actual program terms before submission; no unverified fellowship entitlement is treated here as established fact.

The resource model is driven by four cost centers:

1. researcher time;
2. synthetic scenario authoring and expert review;
3. agent execution and API/compute consumption;
4. storage, logging, and reproducibility infrastructure.

A final budget should be constructed from measured pilot costs rather than unsupported headline estimates.

## 13. Expected Impact

HOUND aims to provide an operationally meaningful layer between generic capability benchmarks and deployment risk assessment. Its primary contribution is methodological: a benchmark should measure what an agent **does in an environment**, including whether it respects state, authorization, provenance, and approval constraints.

The project can support research into safe agentic systems, enterprise deployment assurance, model/scaffold evaluation, and governance-oriented auditing.

## 14. Limitations

HOUND cannot establish that an agent will behave safely in every real deployment. Synthetic environments are abstractions; policy definitions are domain-dependent; judge systems can fail; and model behavior can vary with scaffolding and hidden provider changes.

The benchmark therefore reports evidence about tested configurations and scenario distributions, not universal claims about model character or intent.

## 15. Submission Integrity Rule

Before external submission, every quantitative or externally attributable claim must be classified in `docs/CLAIMS_REGISTER.md` as verified, pending verification, or removed. Unverified product names, benchmark results, fellowship promises, regulatory interpretations, prices, and current model capabilities must not be presented as established facts.

## 16. Author

**Andrzej Mikulski**

Add final contact details, affiliation, ORCID/website, and submission-specific biography before applying.
