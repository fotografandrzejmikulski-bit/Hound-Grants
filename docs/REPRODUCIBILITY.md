# Reproducibility Standard

## Immutable experiment identity

Each run is identified by:

`project / benchmark_version / scenario_version / environment_version / evaluator_version / model_id / scaffold_id / seed`

Any change to a component creates a new version.

## Determinism

Where the provider permits deterministic settings, use them for calibration and regression tests. Where stochasticity is intrinsic, repeat runs across predefined seeds and report the distribution rather than a single run.

## Artifacts

A reproducible release should contain:

- scenario manifests;
- policy definitions;
- evaluator source;
- environment version identifiers;
- run metadata;
- aggregate result files;
- analysis scripts;
- documentation;
- changelog.

## Held-out evaluation

The benchmark should maintain a held-out set unavailable to model developers during routine development. Public examples may use a demonstration subset, but leaderboard evaluation should use a controlled test set whenever contamination resistance is a research objective.

## Result integrity

Never overwrite historical benchmark results. Publish immutable releases and record corrections as new versions.

## Minimum publication package

The first research release should include:

1. benchmark card;
2. methodology paper/preprint;
3. scoring specification;
4. scenario metadata;
5. reference evaluator;
6. baseline results;
7. limitations;
8. claims/evidence register.
