"""Core data structures for the HOUND execution-grounded benchmark."""
from __future__ import annotations

from dataclasses import dataclass, field
from hashlib import sha256
from typing import Any
import json
from datetime import datetime, timezone


def canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def content_hash(value: Any) -> str:
    return sha256(canonical_json(value).encode("utf-8")).hexdigest()


@dataclass(frozen=True)
class PolicyRule:
    id: str
    rule: str
    severity: float = 1.0
    catastrophic: bool = False
    tags: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        if not self.id:
            raise ValueError("policy id is required")
        if self.severity < 0:
            raise ValueError("policy severity must be non-negative")


@dataclass(frozen=True)
class Scenario:
    id: str
    version: str
    domain: str
    objective: str
    initial_state: dict[str, Any]
    allowed_tools: tuple[str, ...] = ()
    approval_gates: tuple[str, ...] = ()
    policies: tuple[PolicyRule, ...] = ()
    success_conditions: tuple[dict[str, Any], ...] = ()
    invariants: tuple[dict[str, Any], ...] = ()
    adversarial_elements: tuple[str, ...] = ()
    seed: int = 0


@dataclass
class Event:
    run_id: str
    step: int
    actor: str
    tool: str
    arguments_hash: str
    authorization_context: dict[str, Any]
    observation_hash: str
    state_before: str
    state_after: str
    policy_events: list[dict[str, Any]] = field(default_factory=list)
    success_relevant: bool = True
    timestamp: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())


@dataclass
class RunResult:
    run_id: str
    success: int
    weighted_violation: float
    max_violation: float
    catastrophic: bool
    events: list[Event]
    final_state: dict[str, Any]
    diagnostics: dict[str, Any]
