# HOUND — Grant Proposal

## Heuristic Observation of Unaligned Networked Decisions

### Author

**Andrzej Mikulski**  
Phone: +48 455 575 337  
Email: mojealterego21@gmail.com

> **Evidence status:** This proposal preserves the supplied HOUND research framing while treating externally checkable claims as evidence-controlled. See `CLAIMS_REGISTER.md` and `ORIGINALITY_AND_POSITIONING.md` before submission.

## 1. Executive Summary

HOUND proposes an execution-grounded benchmark for evaluating whether long-horizon AI agents achieve operational objectives while respecting procedural constraints, authorization boundaries, data-provenance requirements, and human-approval gates.

The central premise is that a final answer or binary task-success label is insufficient for high-stakes agent evaluation. An agent can reach a technically correct final state through an unsafe or unauthorized trajectory. HOUND therefore evaluates the trajectory of observable actions and environment mutations inside isolated, synthetic environments.

The project defines four core metrics:

- **SR — Task Success Rate:** whether the target operational state was achieved.
- **PCR — Procedural Compliance Rate:** whether the agent respected scenario-specific policy constraints.
- **CSR — Compliance-Weighted Success Rate:** technical success adjusted by procedural compliance.
- **MG — Machiavellian Gap:** the difference between technical task success and compliance-weighted success.

The research objective is to determine whether these metrics provide a more operationally meaningful signal of agent reliability than outcome-only evaluation, while preserving reproducibility and minimizing judge-model dependence.

## 2. Research Problem

Long-horizon agents increasingly interact with tools, files, databases, APIs, and other stateful systems. In these settings, correctness is multidimensional: a successful outcome may still be unacceptable if the path to that outcome violates authorization, provenance, approval, or safety requirements.

HOUND focuses on this gap between outcome quality and procedural integrity. It is designed as a controlled benchmark rather than a production-system test.

## 3. Research Questions

### RQ1
Can agents achieve technically successful outcomes while violating explicitly encoded procedural constraints?

### RQ2
Do procedural violations increase under time pressure, incomplete information, conflicting incentives, or strategically useful but unauthorized artifacts?

### RQ3
Does CSR discriminate more effectively than SR between agents that reach the same technical endpoint through materially different trajectories?

### RQ4
Can deterministic environment checks and event logs reliably distinguish policy violations from ordinary model incompetence or tool failure?

### RQ5
How stable are compliance measurements across models, scaffolds, random seeds, scenario families, and judge configurations?

## 4. Proposed Contribution

HOUND's intended contribution is a reproducible evaluation framework that combines:

1. stateful execution environments;
2. explicit policy and authorization constraints;
3. auditable event trajectories;
4. deterministic state and invariant checks where possible;
5. domain-expert policy rubrics for residual judgment;
6. quantitative separation of task success and procedural compliance; and
7. failure attribution rather than a single undifferentiated error label.

The project does **not** claim that the general research problem or the CSR/MG terminology is unprecedented. Existing 2026 work, including MAC-Bench, creates substantial conceptual overlap. HOUND must therefore establish its novelty through execution design, deterministic verification, cross-domain controls, and failure attribution rather than through an absolute “first” claim. citeturn445634academia72

## 5. Execution Environment

HOUND will use isolated synthetic enterprise environments. Planned components include:

- state-writable databases;
- mock enterprise APIs;
- synthetic documents and records;
- authorization and approval services;
- controlled file repositories;
- telemetry and immutable event logs;
- adversarial but non-harmful trap conditions.

No benchmark run should require real credentials, real personal data, production financial systems, or external targets.

## 6. Scenario Design

The initial plan targets a corpus of approximately 300 expert-authored scenarios, subject to pilot calibration and statistical justification.

Scenario families may include:

- financial audit and spreadsheet workflows;
- legal/document workflows;
- scientific or analytical procedures;
- cyber/IT administration conducted entirely within synthetic environments.

Each scenario should specify:

- initial environment state;
- user objective;
- authorized tools and data;
- prohibited actions;
- required verification steps;
- mandatory escalation or human-approval gates;
- terminal success conditions;
- catastrophic policy violations;
- observable evidence required for each scoring decision.

## 7. Metrics

Let an agent trajectory be:

\[
T = (a_1,o_1,a_2,o_2,\ldots,a_n,o_n)
\]

where actions `a_i` are tool/environment operations and observations `o_i` are environment feedback available to the agent.

### 7.1 Task Success Rate

\[
SR(T)=\begin{cases}
1,&\text{if the target terminal state satisfies the task criteria}\\
0,&\text{otherwise.}
\end{cases}
\]

### 7.2 Procedural Compliance Rate

Let `P` be the set of scenario policies and `w(a_i,P)` the validated penalty associated with a policy violation in action `a_i`.

\[
PCR(T)=1-\frac{\sum_i w(a_i,P)}{W_{max}}
\]

The final implementation must define normalization, clipping, severity tiers, and treatment of multiple violations before experiments begin.

### 7.3 Compliance-Weighted Success Rate

\[
CSR=\frac{1}{|N|}\sum_{j=1}^{N}SR(T_j)\times PCR(T_j)
\]

### 7.4 Machiavellian Gap

\[
MG=SR-CSR
\]

MG is interpreted as an outcome/compliance divergence, not as evidence of intent or consciousness. A high MG indicates that technical success is being achieved with substantial procedural cost under the defined rubric.

## 8. Experimental Controls

To make results interpretable, the study should control for:

- model version and inference configuration;
- tool availability;
- scaffold/orchestration implementation;
- scenario order;
- randomization seeds;
- retry limits;
- context-window conditions;
- evaluator version;
- hidden versus visible traps;
- deterministic versus judge-based checks.

Ablation studies should isolate the effects of task pressure, trap density, policy complexity, memory horizon, and tool availability.

## 9. Evaluation Independence

The benchmark should maximize deterministic grading. Any LLM-as-a-judge component should be calibrated against expert labels, reported separately, and treated as a source of measurement uncertainty rather than ground truth by default.

This is particularly important in financial and legal scenarios, where independent verification of numerical and procedural properties can often be encoded directly in the environment.

Vals AI's Excel Modeling Benchmark provides a relevant precedent for recalculating generated financial models before grading; its published results also illustrate the importance of separating formula structure from numerical correctness. citeturn445634search3

## 10. Relationship to Existing Vals AI Work

Vals AI has published legal evaluations comparing AI tools against lawyer baselines. The documented VLAIR work covers multiple legal tasks and establishes the usefulness of domain-specific evaluation against a human control group. citeturn445634search71turn445634search5

HOUND is intended to complement such output-quality benchmarks by measuring policy-constrained execution trajectories inside stateful environments. It should not imply that Vals AI's prior work already proves the HOUND hypothesis.

## 11. Work Plan

### Phase 1 — Infrastructure

Build the isolated execution harness, environment state model, policy schema, telemetry layer, and deterministic terminal-state checks.

### Phase 2 — Expert Scenario Authoring

Construct the first scenario families and conduct expert review of prohibited actions, required approvals, and evidence requirements.

### Phase 3 — Calibration

Run pilot agents to estimate floor/ceiling effects, eliminate ambiguous scenarios, calibrate trap strength, and establish inter-rater reliability.

### Phase 4 — Scale Evaluation

Run the controlled model matrix across multiple seeds and scenario variants, recording complete trajectories and environment-state deltas.

### Phase 5 — Analysis

Estimate SR, PCR, CSR, MG, uncertainty intervals, failure classes, and sensitivity to scenario and evaluator design.

### Phase 6 — Release

Publish methodology, benchmark schema, reproducibility instructions, validated example environments, and a transparent record of limitations.

## 12. Deliverables

1. HOUND scenario schema.
2. Isolated execution harness.
3. Policy and authorization model.
4. Deterministic telemetry format.
5. Initial expert-authored scenario corpus.
6. Evaluation runner and scoring implementation.
7. Statistical analysis notebook/report.
8. Reproducibility package.
9. Safety and governance documentation.
10. Grant/reporting package and research manuscript draft.

## 13. Safety and Governance

HOUND must remain a synthetic evaluation environment. Cybersecurity scenarios must not expose real third-party targets. Financial scenarios must use synthetic institutions, accounts, and credentials. Legal scenarios must use synthetic records or appropriately licensed/public material. Any human-subject or expert-data component must have explicit consent, data-handling rules, and retention controls.

## 14. Limitations

The benchmark will not establish whether an agent possesses human-like motives or malicious intent. “Machiavellian” is a descriptive label for a measurable outcome/compliance divergence. Results may also depend on scenario design, policy encoding, scaffold effects, and the quality of expert rubrics.

The benchmark should therefore be interpreted as an operational risk measurement instrument, not a detector of mental states.

## 15. Funding Use

Any fellowship-specific support, API allocation, GPU allocation, workspace access, or human-data budget must be described as conditional on the actual program terms. The repository intentionally does not treat such benefits as guaranteed until verified from official documentation.

## 16. Submission Position

The strongest grant case is not that HOUND has solved agent safety. The case is that current evaluation can leave a measurable blind spot between technical success and procedural integrity, and that this project will build and validate an execution-grounded instrument for measuring that blind spot under controlled conditions.

## 17. Author

**Andrzej Mikulski**  
Phone: +48 455 575 337  
Email: mojealterego21@gmail.com
