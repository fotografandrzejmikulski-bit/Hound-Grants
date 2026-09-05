# HOUND Implementation Plan

## Architecture

```text
                +-----------------------+
                |   Scenario Registry   |
                +-----------+-----------+
                            |
                            v
+-----------+      +--------+---------+      +----------------+
| Model     |----->| Execution       |----->| Event Store    |
| Adapter   |      | Harness         |      | / State Log    |
+-----------+      +---+----------+---+      +--------+-------+
                       |          |                    |
                       v          v                    v
                +----------+  +----------+      +-----------+
                | Tool/API |  | Synthetic|      | Evaluator |
                | Services |  | State DB |      | Pipeline  |
                +----------+  +----------+      +-----+-----+
                                                      |
                                                      v
                                           +----------+----------+
                                           | SR/PCR/CSR/MG + QA  |
                                           +---------------------+
```

## Components

### Scenario Registry

Version-controlled declarative scenario definitions. Each scenario references an environment seed, policies, tool permissions, success invariants, and evaluator version.

### Execution Harness

Responsible for process isolation, timeouts, reset semantics, tool mediation, event capture, and deterministic replay where practical.

### Synthetic Services

Initial services should include:

- SQL/ERP-like transactional service;
- document repository;
- synthetic email/messaging service;
- role/authorization service;
- approval workflow service;
- evidence/provenance service;
- synthetic market/document retrieval service;
- terminal or code-execution service restricted to the sandbox.

### Event Store

Append-only event records should make every state mutation reconstructable. The public release should expose schemas and aggregate artifacts without exposing secrets or unsafe execution surfaces.

### Evaluator Pipeline

Use deterministic checks for final state and invariants. Use policy rules for authorization, provenance, approval, and integrity. Use human review only where deterministic evaluation cannot resolve an ambiguity.

## Minimum Viable Benchmark

The first executable milestone should not attempt all 300 scenarios. Build a vertical slice with:

- 12 scenarios;
- 4 domains;
- 3 difficulty levels;
- 2 scaffold configurations;
- 3 random seeds per configuration;
- full event logs;
- deterministic SR/PCR calculation;
- blinded human review of sampled trajectories.

A successful vertical slice validates the architecture before expensive scale-up.

## Work Packages

### WP1 — Harness

Environment lifecycle, isolation, reset, event schema, action mediation.

### WP2 — Scenario authoring

Scenario specification, policy taxonomy, expert review, acceptance criteria.

### WP3 — Evaluation engine

Invariant checks, violation detection, metric computation, aggregation, statistical reporting.

### WP4 — Baseline adapters

Standardized adapters for supported model APIs and agent scaffolds.

### WP5 — Analysis

Failure clustering, model/scaffold decomposition, sensitivity analysis, uncertainty estimation.

### WP6 — Packaging

Benchmark release, documentation, reproducibility package, publication artifacts.

## Acceptance Gates

**Gate A — Isolation:** no benchmark action can reach real external targets by default.

**Gate B — Reproducibility:** same seed and versions reproduce the initial state and evaluator outcome.

**Gate C — Auditability:** all policy-relevant state transitions are observable in the event record.

**Gate D — Evaluator validity:** sampled automated labels reach the predefined agreement target with blinded reviewers.

**Gate E — Comparative fairness:** model comparisons use identical environment, policy, and budget controls.

**Gate F — Release readiness:** all public scenarios, scoring code, documentation, and claims have versioned provenance.

## Grant-facing milestone matrix

| Milestone | Evidence produced | Decision gate |
|---|---|---|
| M1 | Working isolated harness + event schema | Isolation and replay pass |
| M2 | 12-scenario vertical slice | Scenario validity and evaluator agreement |
| M3 | Calibrated difficulty/trap suite | No material floor/ceiling effect in pilot |
| M4 | Controlled model/scaffold runs | Fair-comparison audit passed |
| M5 | Statistical analysis package | Metrics reproducible from raw run artifacts |
| M6 | Release candidate | Documentation, provenance, and safety review passed |

## No overclaiming rule

The repository must not describe the 300-scenario benchmark, broad model matrix, or production integration as completed until the relevant artifacts actually exist and are versioned. The six-month schedule in the proposal is a plan, not evidence of completion.
