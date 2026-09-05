# HOUND Risk, Governance and Safety Framework

## 1. Principle

HOUND evaluates agent behavior in environments designed to look operationally meaningful while remaining fully synthetic and isolated. The benchmark's scientific goal does not require real credentials, real customer records, real financial systems, or live attack targets.

## 2. Threat Model

The benchmark must assume that an evaluated agent may:

- follow unexpected tool paths;
- attempt privilege escalation inside the sandbox;
- mutate state outside the intended workflow;
- exploit implementation bugs;
- exfiltrate synthetic secrets;
- attempt to alter logs or evaluator state;
- consume excessive compute or storage;
- exploit scaffold or tool behavior rather than the intended task.

## 3. Isolation Controls

Default execution should provide:

- no production credentials;
- no access to personal data;
- no unrestricted network egress;
- dedicated disposable environments;
- resource quotas;
- process and filesystem isolation;
- immutable audit/event storage outside the agent-controlled namespace;
- environment reset between runs;
- explicit allowlists for tools and destinations.

## 4. Evaluator Integrity

The agent must not be able to modify the authoritative event log, scenario policy, scoring code, or reference state. Evaluation should occur outside the trust boundary of the agent runtime.

## 5. Cybersecurity Boundary

Cyber scenarios are limited to synthetic targets. The benchmark must not provide instructions, credentials, or infrastructure that facilitate unauthorized attacks on real systems. Any network-like behavior is simulated inside the controlled environment.

## 6. Data Governance

Scenario data must be synthetic or appropriately licensed. Any expert annotations should be stripped of personal identifiers before release. If external expert datasets are used, licensing and redistribution restrictions must be documented.

## 7. Human Oversight

Human reviewers are used to calibrate policy labels and resolve ambiguity. Human intervention must be logged and must never silently alter a run's score. A run with intervention should be separately classified from fully autonomous runs.

## 8. Intent Inference

HOUND measures observable behavior. It must not claim that an agent "wanted" to violate a policy unless a separate study specifically establishes a defensible definition and evidence standard. The term *Machiavellian Gap* is a behavioral metric describing outcome/compliance divergence, not a psychological diagnosis.

## 9. Legal/Regulatory Claims

The benchmark may model controls inspired by legal or industry requirements, but a scenario is not itself proof of regulatory compliance. Jurisdiction-specific claims require legal review and primary sources.

## 10. Incident Handling

Any discovery of a sandbox escape, data leakage, evaluator manipulation, or unsafe external interaction triggers:

1. immediate run termination;
2. preservation of logs;
3. isolation of the affected environment;
4. root-cause analysis;
5. evaluator-impact assessment;
6. remediation before further scale testing.

## 11. Release Tiers

**Tier A — Public methodology.** Schemas, metrics, documentation, and aggregate findings.

**Tier B — Reproducibility package.** Safe synthetic scenarios and evaluation code.

**Tier C — Held-out evaluation assets.** Restricted access where premature publication would compromise contamination controls.

Unsafe secrets, production credentials, or exploitable external targets are never released.

## 12. Review Cadence

The safety review should run at three gates:

- before the first agent execution;
- before large-scale evaluation;
- before public release.

Each gate must have an explicit pass/fail record.
