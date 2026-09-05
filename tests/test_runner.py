from pathlib import Path

from hound_eval.runner import load_scenario


ROOT = Path(__file__).resolve().parents[1]


def test_public_scenarios_load():
    scenario_dir = ROOT / "scenarios" / "public"
    files = sorted(scenario_dir.glob("*.yaml"))
    assert len(files) >= 8
    scenarios = [load_scenario(path) for path in files]
    assert len({s.id for s in scenarios}) == len(scenarios)
    assert {s.domain for s in scenarios} >= {"finance", "legal", "science", "cyber"}
