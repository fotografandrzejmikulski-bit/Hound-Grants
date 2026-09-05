# HOUND Repository Readiness

_Last reviewed: 2026-09-05_

## Current state

The repository was empty at the start of this work. It now contains the grant narrative, methodology, implementation plan, protocol, governance, ethics, reproducibility, data/model documentation, claims register, contribution/security policies, license, and citation metadata.

## Readiness assessment

| Area | Status | Notes |
|---|---|---|
| Grant narrative | READY FOR EDITORIAL REVIEW | Structured and tightened from supplied material. |
| Research question | READY | Explicitly framed around trajectory-level procedural compliance. |
| Metrics | READY FOR IMPLEMENTATION | SR/PCR/CSR/MG formally defined; evaluator edge cases documented. |
| Experimental protocol | READY | Standardized pre-run, run, exclusion, and reporting rules added. |
| Safety/governance | READY FOR REVIEW | Synthetic-only boundary and evaluator isolation specified. |
| Reproducibility | READY | Versioning, seeds, artifacts, and held-out testing specified. |
| Claims | BLOCKED | Multiple original claims require primary-source verification; see CLAIMS_REGISTER.md. |
| Program fit | BLOCKED | Fellowship benefits/eligibility must be verified against official program documents. |
| Implementation | DESIGN-READY | Architecture and MVP acceptance gates specified; executable code is not yet included. |
| Author section | INCOMPLETE | Only author name is currently supplied; submission-specific bio/contact/affiliation remain to be added. |

## Critical findings

1. The original document was much stronger as a research concept than as a submission-ready evidence package.
2. Several numerical and market claims were overly specific without visible primary citations.
3. Some terminology implied intentionality. The revised package treats MG as an observable behavioral divergence and explicitly avoids inferring motive.
4. The original proposal assumed fellowship resources that are not yet independently verified here.
5. The benchmark needs a vertical-slice implementation before claiming that the full 300-scenario system exists.

## Current external verification

AISI publicly reports rapid increases in the length of cyber tasks frontier models can autonomously complete and notes a February 2026 estimate of a 4.7-month doubling time on its narrow cyber suite. citeturn153512search2

OpenAI reported in February 2026 that SWE-bench Verified had significant contamination and test-design problems, and in July 2026 reported that a material share of SWE-bench Pro tasks were problematic as well. citeturn153512search0turn153512search1

These sources support the general rationale for execution-grounded and contamination-aware evaluation, but they do not validate every numerical or program-specific statement in the original proposal.

## Remaining author inputs

Before final grant submission, add only the author's final:

- affiliation;
- professional/academic biography;
- contact details;
- optional ORCID/website;
- verified fellowship-specific details.
