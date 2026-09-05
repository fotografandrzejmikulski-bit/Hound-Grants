# HOUND — Grant Proposal Repository

**Heuristic Observation of Unaligned Networked Decisions**

A research proposal and implementation blueprint for an execution-grounded benchmark measuring long-horizon procedural compliance, state integrity, and auditable agent behavior in high-risk environments.

## Project status

This repository is the public grant package and research specification. It currently contains the proposal, methodology, roadmap, governance material, and reproducibility documentation required to turn the concept into an executable benchmark.

## Core research question

Can an AI agent achieve a technically successful outcome while violating the procedures, authorization boundaries, data provenance requirements, or human-approval gates that make the outcome operationally acceptable?

HOUND treats the **trajectory of actions** as a first-class evaluation object rather than evaluating only the final answer.

## Core metrics

- **SR — Task Success Rate:** whether the target operational state was achieved.
- **PCR — Procedural Compliance Rate:** whether the agent respected the scenario's policy constraints.
- **CSR — Compliance-Weighted Success Rate:** success adjusted by procedural compliance.
- **MG — Machiavellian Gap:** the gap between technical success and compliance-weighted success.

\[
CSR = \frac{1}{|N|}\sum_{j=1}^{N} SR(T_j)\times PCR(T_j)
\]

\[
MG = SR-CSR
\]

## Repository map

- [`docs/GRANT_PROPOSAL.md`](docs/GRANT_PROPOSAL.md) — grant-ready proposal, preserving the supplied research framing while separating claims that require verification.
- [`docs/METHODOLOGY.md`](docs/METHODOLOGY.md) — benchmark design, trajectory model, scoring, experimental controls, and calibration.
- [`docs/IMPLEMENTATION_PLAN.md`](docs/IMPLEMENTATION_PLAN.md) — technical architecture, milestones, and engineering work packages.
- [`docs/RISK_AND_GOVERNANCE.md`](docs/RISK_AND_GOVERNANCE.md) — safety, legal, data-governance, and scientific-integrity controls.
- [`docs/REPRODUCIBILITY.md`](docs/REPRODUCIBILITY.md) — reproducible evaluation and publication requirements.
- [`docs/CLAIMS_REGISTER.md`](docs/CLAIMS_REGISTER.md) — evidence register identifying claims that must be source-verified before external submission.
- [`docs/DATA_CARD.md`](docs/DATA_CARD.md) — planned benchmark data documentation.
- [`docs/MODEL_CARD.md`](docs/MODEL_CARD.md) — evaluation-model and judge-model documentation template.
- [`docs/EVALUATION_PROTOCOL.md`](docs/EVALUATION_PROTOCOL.md) — standardized test execution protocol.
- [`docs/ETHICS.md`](docs/ETHICS.md) — ethical boundaries and prohibited real-world side effects.
- [`docs/DEVELOPMENT.md`](docs/DEVELOPMENT.md) — local development and contribution workflow.
- [`CITATION.cff`](CITATION.cff) — citation metadata.
- [`LICENSE`](LICENSE) — repository license.
- [`CONTRIBUTING.md`](CONTRIBUTING.md) — contribution policy.
- [`SECURITY.md`](SECURITY.md) — responsible disclosure policy.

## Important evidence policy

The supplied proposal contains numerous time-sensitive benchmark figures, model names, program names, and regulatory references. This repository deliberately does **not** present those claims as independently verified facts. Each externally checkable claim is tracked in `docs/CLAIMS_REGISTER.md` so the submission can distinguish:

1. verified primary-source evidence,
2. author-supplied material awaiting verification, and
3. project hypotheses or projections.

That distinction is mandatory for a credible grant submission.

## Safety boundary

HOUND uses synthetic, isolated enterprise environments. It must never connect an evaluation agent to production financial systems, real credentials, real personal data, or external targets without an independently approved safety process.

## Author

**Andrzej Mikulski**

Project-specific contact details should be added by the author before external submission.
