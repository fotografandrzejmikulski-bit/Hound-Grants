# Development Guide

## Repository intent

This repository begins as a grant/research specification and is structured so that implementation can be added without rewriting the proposal.

## Recommended implementation layout

```text
src/
  harness/
  environments/
  services/
  evaluators/
  metrics/
  adapters/
scenarios/
  public/
  heldout/
tests/
results/
analysis/
docs/
```

## Engineering rules

- Separate environment state from evaluation state.
- Keep the authoritative evaluator outside the agent-controlled runtime.
- Version policies and evaluators independently.
- Avoid hidden defaults that change scores.
- Record every non-deterministic dependency.
- Keep test fixtures synthetic.

## Quality gates

Before a release:

1. Unit-test metric calculations.
2. Replay representative trajectories.
3. Verify policy-violation labels.
4. Test evaluator tampering resistance.
5. Test environment reset integrity.
6. Run safety checks for network egress.
7. Recalculate a fixed regression suite.

## Pull request principle

A change to benchmark semantics requires explicit documentation and a version change. Silent score-changing edits are not permitted.
