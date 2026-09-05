# HOUND Data Card

## Dataset purpose

The HOUND scenario corpus is intended to evaluate long-horizon agent execution under explicit procedural, authorization, provenance, and approval constraints.

## Composition target

The proposal targets approximately 300 scenarios. This is a development target, not an existing dataset size.

Planned domains:

- finance;
- legal/document workflows;
- scientific investigation;
- cybersecurity in synthetic ranges;
- cross-domain enterprise administration.

## Scenario properties

Each scenario should specify:

- objective;
- initial state;
- allowed tools;
- authorization scope;
- approval gates;
- policies;
- success invariants;
- adversarial elements;
- seed;
- evaluator version;
- safety classification.

## Data generation

Scenarios should be authored by researchers and, where domain-specific rules are material, reviewed by relevant subject-matter experts. Public release should avoid copying sensitive or proprietary operational data.

## Intended use

The corpus is intended for benchmark research, agent-evaluation calibration, safety analysis, and reproducibility studies.

## Out-of-scope use

The corpus must not be connected to live production systems or used to authorize real-world actions merely because a system performs well on HOUND.

## Known limitations

Synthetic environments cannot capture every property of production systems. Policies may be simplified, tool interfaces may be cleaner than real systems, and the scenario distribution may bias measured behavior.

## Contamination controls

Public demonstrations and held-out evaluation scenarios should be separated. Scenario releases should carry version identifiers so that results can be traced to the exact corpus version.
