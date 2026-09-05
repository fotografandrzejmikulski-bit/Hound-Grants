"""Deterministic synthetic stateful environment used by HOUND."""
from __future__ import annotations

from copy import deepcopy
from dataclasses import dataclass
from typing import Any

from .core import Event, content_hash


@dataclass
class Environment:
    state: dict[str, Any]

    def snapshot(self) -> dict[str, Any]:
        return deepcopy(self.state)

    def read(self, path: str) -> Any:
        value: Any = self.state
        for key in path.split("."):
            if not isinstance(value, dict) or key not in value:
                raise KeyError(path)
            value = value[key]
        return deepcopy(value)

    def write(self, path: str, value: Any) -> None:
        parts = path.split(".")
        cursor = self.state
        for key in parts[:-1]:
            child = cursor.get(key)
            if not isinstance(child, dict):
                child = {}
                cursor[key] = child
            cursor = child
        cursor[parts[-1]] = deepcopy(value)


class StatefulServiceHub:
    """Small service surface with a single authoritative synthetic state."""

    def __init__(self, initial_state: dict[str, Any]):
        self.env = Environment(deepcopy(initial_state))
        self._events: list[Event] = []

    def execute(self, run_id: str, step: int, actor: str, tool: str,
                arguments: dict[str, Any], authorization_context: dict[str, Any]) -> Any:
        before = self.env.snapshot()
        if tool == "records.get":
            observation = self.env.read(arguments["path"])
        elif tool == "records.set":
            self.env.write(arguments["path"], arguments["value"])
            observation = {"ok": True}
        elif tool == "approval.request":
            request_id = arguments["request_id"]
            self.env.write(f"approvals.{request_id}", {"status": "pending"})
            observation = {"request_id": request_id, "status": "pending"}
        elif tool == "approval.grant":
            request_id = arguments["request_id"]
            self.env.write(f"approvals.{request_id}", {"status": "approved"})
            observation = {"request_id": request_id, "status": "approved"}
        elif tool == "audit.append":
            item = arguments["entry"]
            audit = self.env.state.setdefault("audit_log", [])
            audit.append(deepcopy(item))
            observation = {"ok": True, "index": len(audit) - 1}
        else:
            raise ValueError(f"unsupported tool: {tool}")

        after = self.env.snapshot()
        self._events.append(Event(
            run_id=run_id,
            step=step,
            actor=actor,
            tool=tool,
            arguments_hash=content_hash(arguments),
            authorization_context=deepcopy(authorization_context),
            observation_hash=content_hash(observation),
            state_before=content_hash(before),
            state_after=content_hash(after),
        ))
        return observation

    def events(self) -> list[Event]:
        return list(self._events)
