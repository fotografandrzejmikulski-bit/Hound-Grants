from hound_eval.environment import StatefulServiceHub
from hound_eval.services import ServiceContext, SyntheticServices


def test_synthetic_services_mutate_authoritative_state_and_emit_events():
    hub = StatefulServiceHub({"records": {"amount": 10}, "audit_log": []})
    svc = SyntheticServices(hub, ServiceContext("run-1", "agent", 1, {"authorized": True}))
    assert svc.records_get("records.amount") == 10
    svc.records_set("records.amount", 25)
    svc.audit_append({"event": "adjusted"})
    assert hub.env.read("records.amount") == 25
    assert hub.env.read("audit_log") == [{"event": "adjusted"}]
    assert len(hub.events()) == 3
