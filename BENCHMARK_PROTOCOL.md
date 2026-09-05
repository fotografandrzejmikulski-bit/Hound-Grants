# HOUND Benchmark Protocol

## Purpose

This protocol defines the minimum reproducible execution procedure for HOUND. It prevents benchmark claims from being made from a single run, uncontrolled scaffold, or non-versioned scenario.

## Mandatory run manifest

Every evaluation must record:

- HOUND version/commit;
- model identifier and provider;
- scaffold/orchestrator identifier and version;
- scenario ID/version;
- scenario seed;
- tool schema version;
- evaluator version;
- maximum steps and timeout;
- deterministic/random configuration;
- execution cost when measurable;
- final-state hash;
- event-log hash;
- reviewer status for sampled human adjudication.

## Evaluation splits

1. **Development:** freely inspectable scenarios used for engineering.
2. **Calibration:** scenarios used to tune difficulty and adjudicator agreement.
3. **Public test:** frozen scenarios released with the benchmark version.
4. **Held-out test:** withheld scenarios used for final claims and not used for tuning.

## Baseline requirements

At minimum, final comparative studies should include:

- outcome-only grading;
- HOUND deterministic grading;
- identical tool permissions;
- identical environment versions;
- crossed model/scaffold controls where feasible;
- multiple seeds.

## Statistical reporting

Every headline result must state sample size, scenario count, seed count, aggregation rule, and uncertainty interval. Results from exploratory pilots must not be presented as confirmatory evidence.

## Reproducibility requirement

A released result is reproducible only when the public artifacts are sufficient to reconstruct scenario versions, environment state, evaluator version, and scoring configuration, subject to legitimate safety and confidentiality restrictions.

## Safety rule

The benchmark is synthetic by default. Network egress is denied unless a test explicitly requires an approved mock service. No real credentials, production systems, personal records, or unauthorized external targets are permitted.
