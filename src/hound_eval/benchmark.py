"""Benchmark orchestration over a versioned scenario corpus."""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Any

from .runner import load_scenario
from .harness import ExecutionHarness
from .evaluator import aggregate_evaluations, evaluate_events


@dataclass(frozen=True)
class BenchmarkRecord:
    scenario_id: str
    domain: str
    run_id: str
    success: int
    pcr: float
    csr: float
    mg: float
    diagnostics: dict[str, Any]


def run_corpus(paths: list[str | Path], agent: Callable[[Any, Any], None]) -> list[BenchmarkRecord]:
    results: list[BenchmarkRecord] = []
    harness = ExecutionHarness()
    for path in paths:
        scenario = load_scenario(path)
        result = harness.run(scenario, agent)
        score_eval = evaluate_events(scenario, result.events, result.success)
        results.append(BenchmarkRecord(
            scenario_id=scenario.id,
            domain=scenario.domain,
            run_id=result.run_id,
            success=result.success,
            pcr=score_eval.score and __import__("hound_eval.metrics", fromlist=["procedural_compliance"]).procedural_compliance(score_eval.score),
            csr=score_eval.score.success * __import__("hound_eval.metrics", fromlist=["procedural_compliance"]).procedural_compliance(score_eval.score),
            mg=result.success - score_eval.score.success * __import__("hound_eval.metrics", fromlist=["procedural_compliance"]).procedural_compliance(score_eval.score),
            diagnostics=result.diagnostics,
        ))
    return results


def summarize(records: list[BenchmarkRecord]) -> dict[str, float]:
    if not records:
        raise ValueError("empty benchmark corpus")
    n = len(records)
    return {
        "SR": sum(r.success for r in records) / n,
        "PCR": sum(r.pcr for r in records) / n,
        "CSR": sum(r.csr for r in records) / n,
        "MG": sum(r.mg for r in records) / n,
    }
