# HOUND Repository Readiness

_Last reviewed: 2026-09-05_

## Current state

The repository started empty and has been rebuilt as an English-language grant and research package. It now contains the proposal, formal methodology, implementation plan, evaluation protocol, governance, ethics, reproducibility, data/model documentation, claims register, related-work analysis, program verification, author/contact data, and submission checklist.

## Readiness assessment

| Area | Status | Notes |
|---|---|---|
| Grant narrative | READY | English-language proposal revised for precision and evidence discipline. |
| Research questions | READY | Falsifiable trajectory-level questions defined. |
| Metrics | READY FOR IMPLEMENTATION | SR/PCR/CSR/MG formally defined with bounded PCR semantics. |
| Experimental protocol | READY | Controls, seeds, evaluator independence, and reporting specified. |
| Safety/governance | READY FOR REVIEW | Synthetic-only boundary and default-deny external execution specified. |
| Reproducibility | READY | Versioning, seeds, artifacts, replay, and held-out testing specified. |
| Related work | REVIEWED | MAC-Bench overlap explicitly disclosed and positioning narrowed. |
| Program information | DATE-QUALIFIED | Public 2026 fellowship information verified; advertised June 30, 2026 deadline has passed. |
| Author/contact | READY | Name, phone, and email recorded. |
| Implementation | DESIGN-READY | Architecture and MVP acceptance gates specified; executable code is not yet part of this grant package. |
| Evidence closure | PENDING | Some externally checkable claims still require primary-source verification before submission. |

## Critical findings

1. The strongest version of HOUND is a state-grounded, deterministic-first, attribution-oriented evaluation proposal—not an originality claim based on CSR/MG alone.
2. MAC-Bench materially overlaps with the original framing and terminology. This is disclosed rather than hidden.
3. The full benchmark should not be described as already implemented; the plan starts with a vertical slice and scales after calibration.
4. Program-specific benefits are now treated with date and evidence discipline.
5. Remaining uncertainty is explicitly surfaced in `CLAIMS_REGISTER.md` and `SUBMISSION_CHECKLIST.md`.

## Final readiness statement

The repository is **grant-package ready for editorial and application-form work**, but it should only be treated as **submission-locked** after the remaining evidence and current fellowship-status checks are closed.
