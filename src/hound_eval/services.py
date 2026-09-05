"""Explicit synthetic stateful services for HOUND scenarios.

All services operate on an in-memory environment owned by the harness. They do
not access the external network, real credentials, or production systems.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from .environment import StatefulServiceHub


@dataclass(frozen=True)
class ServiceContext:
    run_id: str
    actor: str
    step: int
    authorization: dict[str, Any]


class SyntheticServices:
    def __init__(self, hub: StatefulServiceHub, context: ServiceContext):
        self.hub = hub
        self.context = context

    def records_get(self, path: str) -> Any:
        return self.hub.execute(self.context.run_id, self.context.step, self.context.actor, "records.get", {"path": path}, self.context.authorization)

    def records_set(self, path: str, value: Any) -> Any:
        return self.hub.execute(self.context.run_id, self.context.step, self.context.actor, "records.set", {"path": path, "value": value}, self.context.authorization)

    def request_approval(self, request_id: str) -> Any:
        return self.hub.execute(self.context.run_id, self.context.step, self.context.actor, "approval.request", {"request_id": request_id}, self.context.authorization)

    def grant_approval(self, request_id: str) -> Any:
        return self.hub.execute(self.context.run_id, self.context.step, self.context.actor, "approval.grant", {"request_id": request_id}, self.context.authorization)

    def audit_append(self, entry: dict[str, Any]) -> Any:
        return self.hub.execute(self.context.run_id, self.context.step, self.context.actor, "audit.append", {"entry": entry}, self.context.authorization)
