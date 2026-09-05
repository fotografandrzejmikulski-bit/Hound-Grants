# Reproduce the HOUND demonstration

## Scope

This command path validates the dependency-light metric layer and synthetic stateful environment. It does not claim to reproduce the full future 300-scenario study.

## Requirements

- Python 3.10+
- pip

## Commands

```bash
python -m pip install -e .
python -m pytest
```

Expected result: all repository tests pass.

## Reproducibility contract

A published experiment must record:

- repository commit SHA;
- Python/runtime version;
- model and scaffold identifiers;
- scenario manifest and individual scenario versions;
- evaluator version;
- random seeds;
- step and cost budgets;
- tool schemas and permissions;
- final aggregate metrics and uncertainty intervals.

## Safety contract

Demonstration scenarios are synthetic. Do not replace their service layer with production credentials, production endpoints, or real third-party targets.
