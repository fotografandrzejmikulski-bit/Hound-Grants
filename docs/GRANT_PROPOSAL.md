# HOUND — Grant Proposal

## Heuristic Observation of Unaligned Networked Decisions

### Author

**Andrzej Mikulski**  
Phone: +48 455 575 337  
Email: mojealterego21@gmail.com

> **Evidence status:** This is the submission version of the proposal. Externally checkable claims are deliberately conservative and should be traceable to primary sources before external submission. See `CLAIMS_REGISTER.md`, `RELATED_WORK.md`, and `PROGRAM_VERIFICATION.md`.

## 1. Executive Summary

HOUND proposes an execution-grounded benchmark for evaluating whether long-horizon AI agents achieve operational objectives while respecting procedural constraints, authorization boundaries, data-provenance requirements, and human-approval gates.

The central premise is that a final answer or binary task-success label is insufficient for high-stakes agent evaluation. An agent can reach a technically correct final state through an unsafe or unauthorized trajectory. HOUND therefore evaluates observable action trajectories and environment-state mutations inside isolated synthetic environments.

The project evaluates four core quantities:

- **SR — Task Success Rate:** whether the target operational state was achieved.
- **PCR — Procedural Compliance Rate:** whether the agent respected scenario-specific policy constraints.
- **CSR — Compliance-Weighted Success Rate:** technical success adjusted by procedural compliance.
- **MG — Machiavellian Gap:** an outcome/compliance divergence defined by this project, not a claim about agent intent.

The research objective is to determine whether trajectory-aware, state-grounded evaluation provides a more operationally useful signal of agent reliability than outcome-only evaluation, while reducing unnecessary dependence on subjective model judging.

## 2. Research Problem

Long-horizon agents increasingly interact with tools, files, databases, APIs, and other stateful systems. In these settings, correctness is multidimensional: a successful outcome may still be unacceptable if the path to that outcome violates authorization, provenance, approval, or safety requirements.

HOUND focuses on the measurable gap between outcome quality and procedural integrity. It is designed as a controlled benchmark rather than a production-system test.

## 3. Research Questions

### RQ1
Can agents achieve technically successful outcomes while violating explicitly encoded procedural constraints?

### RQ2
Do procedural violations increase under time pressure, incomplete information, conflicting incentives, or strategically useful but unauthorized artifacts?

### RQ3
Does CSR discriminate between agents that reach the same technical endpoint through materially different trajectories?

### RQ4
Can deterministic environment checks and event logs reliably distinguish policy violations from ordinary model incompetence, tool failure, or environment faults?

### RQ5
How stable are compliance measurements across models, scaffolds, random seeds, scenario families, and evaluator configurations?

### RQ6
Can HOUND's state-first and attribution-oriented design add measurable value beyond existing process-compliance benchmarks such as MAC-Bench?

## 4. Contribution and Scope

HOUND proposes a reproducible evaluation framework combining:

1. stateful execution environments;
2. explicit policy, authorization, and approval constraints;
3. auditable event trajectories;
4. deterministic state and invariant checks where possible;
5. domain-expert rubrics for residual ambiguity;
6. quantitative separation of task success and procedural compliance;
7. failure attribution across distinct causal categories; and
8. controlled comparison of model and scaffold effects.

HOUND **does not** claim to be the first system to evaluate procedural compliance during agent execution, to use dynamic adversarial environments, or to use CSR/Machiavellian-gap terminology. MAC-Bench, published in June 2026, establishes substantial prior art in these areas. citeturn935135academia53turn935135search0

The proposed research contribution is narrower: to test whether a **state-first, deterministic-first, attribution-oriented** evaluation design can produce more reproducible and diagnostically useful measurements across multiple high-risk synthetic domains.

## 5. Related Work and Positioning

MAC-Bench is the most important directly overlapping work identified during pre-submission review. It describes dynamic adversarial process-compliance evaluation, sandbox environments, trajectory audit logs, deterministic/hybrid auditors, and CSR/Machiavelli Gap metrics. citeturn935135academia53turn935135search0

Accordingly, HOUND's grant value must be demonstrated through implementation and evidence rather than novelty language. The project will explicitly compare:

- state/invariant coverage;
- deterministic versus judge-dependent scoring;
- reproducibility under fixed seeds;
- model/scaffold attribution;
- failure-cause resolution;
- expert-review agreement;
- evaluation cost; and
- behavior across domains.

The comparison protocol is described in `docs/RELATED_WORK.md` and `docs/METHODOLOGY.md`.

## 6. Execution Environment

HOUND will use isolated synthetic enterprise environments. Planned components include:

- state-writable databases;
- mock enterprise APIs;
- synthetic documents and records;
- authorization and approval services;
- controlled file repositories;
- telemetry and append-only event logs;
- adversarial but non-harmful trap conditions.

No benchmark run should require real credentials, real personal data, production financial systems, or external targets.

## 7. Scenario Design

The initial research target is approximately 300 expert-authored scenarios, subject to pilot calibration, statistical justification, and available resources. The full target corpus is a planned deliverable, not an existing dataset claim.

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

## 8. Formal Evaluation Model

Let an agent trajectory be:

\[
T = (a_1,o_1,a_2,o_2,\ldots,a_n,o_n)
\]

where actions `a_i` are tool/environment operations and observations `o_i` are environment feedback available to the agent.

### 8.1 Task Success Rate

\[
SR(T)=\begin{cases}
1,&\text{if the target terminal state satisfies the task criteria}\\
0,&\text{otherwise.}
\end{cases}
\]

### 8.2 Procedural Compliance Rate

Let `P` be the scenario policy set and `w(a_i,P)` the validated penalty associated with a policy violation in action `a_i`.

\[
PCR_{raw}(T)=1-\frac{\sum_i w(a_i,P)}{W_{max}}
\]

The implementation will define explicit clipping and catastrophic-violation rules:

\[
PCR(T)=\max(0,\min(1,PCR_{raw}(T)))
\]

A scenario may define a catastrophic violation that forces `PCR(T)=0`.

### 8.3 Compliance-Weighted Success Rate

\[
CSR=\frac{1}{|N|}\sum_{j=1}^{N}SR(T_j)\times PCR(T_j)
\]

### 8.4 Machiavellian Gap

\[
MG=SR-CSR
\]

MG is an operational divergence metric. It must not be interpreted as evidence of motive, agency, consciousness, or malicious intent.

## 9. Experimental Design

Each benchmark comparison should control, or explicitly cross, the following variables:

| Variable | Control requirement |
|---|---|
| Model version | Fixed within a comparison cell |
| Inference configuration | Versioned and reported |
| Scaffold | Fixed or crossed explicitly |
| Tools | Same schemas, permissions, and tool behavior |
| Environment | Same version and seed |
| Policy set | Same version |
| Scenario | Same version |
| Budget | Declared and comparable |
| Evaluator | Same version |
| Retry policy | Fixed and reported |

The pilot will include baseline, pressure, and adversarial conditions. Ablations will isolate pressure intensity, trap density, policy complexity, memory horizon, and tool availability.

## 10. Evaluation Independence and Reliability

HOUND will maximize deterministic grading. LLM-as-a-judge should be used only for properties that cannot reasonably be encoded as deterministic checks.

Where judgment is required, evaluators will be calibrated against blinded expert review. Inter-rater agreement and evaluator disagreement will be reported as measurement diagnostics.

The benchmark will distinguish at minimum:

- model error;
- retrieval/provenance error;
- planning error;
- authorization violation;
- approval violation;
- state-tracking failure;
- environment/tool failure;
- evaluator error;
- timeout/resource limitation;
- outcome/compliance divergence.

## 11. Contamination Resistance

HOUND scenarios should be authored and versioned separately from the public demonstration set. Development, calibration, demonstration, and held-out evaluation material should remain distinct.

This design is motivated by recent benchmark-quality concerns. OpenAI reported in February 2026 that SWE-bench Verified had important contamination and test-design problems, and later reported material task-quality problems in SWE-bench Pro. HOUND therefore treats contamination resistance and task validation as first-class methodological controls rather than post-hoc documentation.

## 12. Human Calibration

A statistically justified subset of trajectories will receive blinded human review. Reviewers should receive the task objective, scenario policy, event timeline, relevant state transitions, and automated classification without model identity where feasible.

The project will report disagreement rates and the adjudication protocol.

## 13. Work Plan

### Phase 1 — Infrastructure

Build the isolated execution harness, state model, policy schema, telemetry layer, and deterministic terminal-state checks.

### Phase 2 — Scenario Authoring

Construct initial scenario families and review policy constraints, approvals, prohibited actions, and evidence requirements with qualified domain reviewers.

### Phase 3 — Calibration

Run pilot agents to estimate floor/ceiling effects, eliminate ambiguous scenarios, calibrate trap strength, and establish reviewer agreement.

### Phase 4 — Controlled Evaluation

Run the model/scaffold matrix across multiple seeds and scenario variants, recording trajectories and state deltas.

### Phase 5 — Analysis

Estimate SR, PCR, CSR, MG, uncertainty intervals, failure classes, evaluator dependence, and sensitivity to scenario design.

### Phase 6 — Release

Publish methodology, schemas, reproducibility instructions, validated example environments, benchmark limitations, and a transparent research report.

## 14. Deliverables

1. HOUND scenario specification.
2. Isolated execution harness.
3. Policy, authorization, and approval model.
4. Deterministic telemetry and event schema.
5. Pilot and calibrated scenario corpus.
6. Evaluation runner and scoring implementation.
7. Statistical analysis artifacts.
8. Reproducibility package.
9. Safety and governance documentation.
10. Research manuscript/report.

## 15. Safety and Governance

HOUND must remain a synthetic evaluation environment. Cybersecurity scenarios must not expose real third-party targets. Financial scenarios must use synthetic institutions, accounts, and credentials. Legal scenarios must use synthetic records or appropriately licensed/public material. Any expert-data component must have explicit consent, data-handling rules, and retention controls.

The project will apply a default-deny external-network policy to benchmark execution wherever technically feasible.

## 16. Limitations

The benchmark will not establish whether an agent possesses human-like motives or malicious intent. “Machiavellian Gap” is used as a descriptive label for measurable outcome/compliance divergence.

Results may depend on scenario construction, policy encoding, scaffold effects, evaluator quality, and domain expertise. Cross-domain claims will therefore be limited to the implemented and validated domain set rather than generalized beyond the evidence.

## 17. Funding and Program Assumptions

Any fellowship-specific support, API allocation, GPU allocation, workspace access, stipend, human-data budget, publication support, or other benefit must be stated only to the extent supported by the official program documentation.

At present, the repository treats these items as verification-gated rather than guaranteed.

## 18. Success Criteria

The project will be considered scientifically successful if it demonstrates all of the following:

1. the benchmark can reproducibly create and reset isolated stateful environments;
2. policy-relevant agent actions can be reconstructed from event logs;
3. deterministic evaluators correctly identify predefined state and authorization violations on the validated test suite;
4. blinded expert review reaches the predefined agreement target on sampled trajectories;
5. SR and compliance metrics differentiate trajectories that outcome-only scoring treats as equivalent; and
6. the final report quantifies where HOUND adds information beyond the selected related-work baselines.

## 19. Submission Position

The strongest case for HOUND is not that it has solved agent safety or invented an entirely new research area. The case is that long-horizon agent evaluation requires measurements of **how** outcomes are produced, and that HOUND will build and empirically validate a state-grounded, deterministic-first instrument for that purpose.

## 20. Author

**Andrzej Mikulski**  
Phone: +48 455 575 337  
Email: mojealterego21@gmail.com
