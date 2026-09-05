# Contributing to HOUND

Contributions are welcome when they improve benchmark validity, reproducibility, safety, or documentation.

## Before contributing

Please ensure that changes are:

- scoped to the documented research objective;
- reproducible or accompanied by a test plan;
- safe to run in isolation;
- explicit about changes to scores or evaluator semantics;
- accompanied by updated documentation when public claims change.

## Scenario contributions

A scenario contribution should include:

1. objective;
2. initial state;
3. policies;
4. authorization rules;
5. success invariants;
6. adversarial element description, if any;
7. evaluator logic;
8. safety review;
9. version identifier.

## Scientific integrity

Do not tune a scenario solely to improve or worsen a particular model's ranking. Do not alter evaluator logic after seeing results without recording the change and rerunning affected configurations.

## Pull requests

A pull request should explain the motivation, affected files, validation performed, and any change in benchmark semantics or reported results.
