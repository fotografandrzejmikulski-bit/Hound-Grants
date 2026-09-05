# HOUND

## Heuristic Observation of Unaligned Networked Decisions

**Execution-grounded evaluation of long-horizon AI agents under procedural, authorization, provenance, and approval constraints.**

### Author

**Andrzej Mikulski**  
Phone: +48 455 575 337  
Email: mojealterego21@gmail.com

## Project at a glance

HOUND is a research benchmark concept for testing whether an AI agent can complete a stateful operational task **without violating the procedures that make the outcome acceptable**.

The benchmark evaluates observable trajectories inside isolated synthetic environments rather than judging only the final answer.

Core metrics:

- **SR — Task Success Rate**
- **PCR — Procedural Compliance Rate**
- **CSR — Compliance-Weighted Success Rate**
- **MG — Machiavellian Gap**, defined here as an outcome/compliance divergence rather than an inference about intent

## Why this matters

Outcome-only evaluation can collapse materially different behaviors into the same score. Two agents may reach the same terminal state while one respects evidence requirements, authorization boundaries, and approval gates and the other bypasses them.

HOUND is designed to make those differences observable, reproducible, and measurable.

## Research status

This repository is a **grant and research specification package**. It does not claim that the full benchmark or its 300-scenario target corpus already exists.

The implementation strategy begins with a small executable vertical slice, followed by calibration and controlled scale-up.

## Repository

| Path | Purpose |
|---|---|
| `docs/GRANT_PROPOSAL.md` | English-language grant proposal |
| `docs/METHODOLOGY.md` | Formal benchmark methodology |
| `docs/IMPLEMENTATION_PLAN.md` | Architecture and implementation work packages |
| `docs/EVALUATION_PROTOCOL.md` | Standardized execution and reporting protocol |
| `docs/RISK_AND_GOVERNANCE.md` | Safety, governance, and risk controls |
| `docs/ETHICS.md` | Ethics and dual-use boundaries |
| `docs/REPRODUCIBILITY.md` | Reproducibility and release requirements |
| `docs/DATA_CARD.md` | Benchmark data documentation |
| `docs/MODEL_CARD.md` | Evaluator/model documentation template |
| `docs/CLAIMS_REGISTER.md` | External-claim evidence register |
| `docs/ORIGINALITY_AND_POSITIONING.md` | Novelty and overlap analysis |
| `docs/PROGRAM_VERIFICATION.md` | Fellowship/program verification gate |
| `docs/SUBMISSION_CHECKLIST.md` | Pre-submission checklist |
| `docs/STATUS.md` | Current readiness state |
| `AUTHOR.md` | Author contact information |

## Evidence policy

Externally checkable claims are tracked separately from project hypotheses. Time-sensitive model names, benchmark scores, prices, program benefits, regulatory mappings, and novelty claims must not be presented as established facts without primary-source verification.

## Safety boundary

HOUND is designed for synthetic, isolated environments. It must not connect benchmark agents to production systems, real credentials, real personal data, or unauthorized external targets.

## Current release principle

A credible benchmark is more valuable than an inflated benchmark. HOUND therefore prefers:

1. deterministic evaluation where possible;
2. explicit environment state and event logging;
3. blinded expert review for residual ambiguity;
4. uncertainty reporting rather than leaderboard-only point estimates;
5. transparent limitations and contamination controls.

## Citation

See `CITATION.cff` for citation metadata.
