"""Scenario loader and deterministic benchmark runner."""
from __future__ import annotations

from pathlib import Path
from typing import Callable, Any

from .core import PolicyRule, Scenario
from .harness import ExecutionHarness


def load_scenario(path: str | Path) -> Scenario:
    import yaml
    raw = yaml.safe_load(Path(path).read_text(encoding="utf-8"))
    policies = tuple(PolicyRule(
        id=p["id"], rule=p["rule"], severity=float(p.get("severity", 1.0)),
        catastrophic=bool(p.get("catastrophic", False)), tags=tuple(p.get("tags", []))
    ) for p in raw.get("policies", []))
    return Scenario(
        id=raw["id"], version=str(raw["version"]), domain=raw["domain"], objective=raw["objective"],
        initial_state=raw["initial_state"], allowed_tools=tuple(raw.get("allowed_tools", [])),
        approval_gates=tuple(raw.get("approval_gates", [])), policies=policies,
        success_conditions=tuple(raw.get("success_conditions", [])),
        invariants=tuple(raw.get("invariants", [])),
        adversarial_elements=tuple(raw.get("adversarial_elements", [])), seed=int(raw.get("seed", 0)),
    )


def run_scenario(path: str | Path, agent: Callable[[Scenario, Any], None]) -> Any:
    return ExecutionHarness().run(load_scenario(path), agent)
