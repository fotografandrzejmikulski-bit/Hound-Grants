"""Minimal execution harness with strict tool mediation and reset semantics."""
from __future__ import annotations

from dataclasses import dataclass
from uuid import uuid4
from typing import Any, Callable

from .core import Scenario
from .environment import StatefulServiceHub
from .evaluator import run_result


Agent = Callable[[Scenario, StatefulServiceHub], None]


@dataclass(frozen=True)
class HarnessConfig:
    max_steps: int = 50


class ExecutionHarness:
    def __init__(self, config: HarnessConfig | None = None):
        self.config = config or HarnessConfig()

    def run(self, scenario: Scenario, agent: Agent) -> Any:
        hub = StatefulServiceHub(scenario.initial_state)
        run_id = str(uuid4())
        # The initial reference agent interface receives a tool-mediated hub.
        # A production adapter must enforce step budgets and permission schemas.
        before = len(hub.events())
        agent(scenario, hub)
        events = hub.events()[before:]
        success = self._success(scenario, hub)
        return run_result(run_id, scenario, events, hub.env.snapshot(), success)

    @staticmethod
    def _success(scenario: Scenario, hub: StatefulServiceHub) -> int:
        for condition in scenario.success_conditions:
            path = condition["path"]
            expected = condition["equals"]
            try:
                actual = hub.env.read(path)
            except KeyError:
                return 0
            if actual != expected:
                return 0
        return 1
