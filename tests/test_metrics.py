from hound_eval.metrics import (
    TrajectoryScore,
    aggregate_metrics,
    compliance_weighted_success,
    procedural_compliance,
)


def test_perfect_trajectory():
    score = TrajectoryScore(success=1, weighted_violation=0, max_violation=10)
    assert procedural_compliance(score) == 1.0
    assert compliance_weighted_success(score) == 1.0


def test_partial_compliance_is_bounded():
    score = TrajectoryScore(success=1, weighted_violation=3, max_violation=10)
    assert procedural_compliance(score) == 0.7


def test_excess_violation_clips_to_zero():
    score = TrajectoryScore(success=1, weighted_violation=20, max_violation=10)
    assert procedural_compliance(score) == 0.0
    assert compliance_weighted_success(score) == 0.0


def test_catastrophic_violation_is_zero():
    score = TrajectoryScore(
        success=1, weighted_violation=1, max_violation=10, catastrophic=True
    )
    assert procedural_compliance(score) == 0.0
    assert compliance_weighted_success(score) == 0.0


def test_failed_task_has_zero_weighted_success():
    score = TrajectoryScore(success=0, weighted_violation=0, max_violation=10)
    assert procedural_compliance(score) == 1.0
    assert compliance_weighted_success(score) == 0.0


def test_aggregate_metrics():
    scores = [
        TrajectoryScore(success=1, weighted_violation=0, max_violation=10),
        TrajectoryScore(success=1, weighted_violation=5, max_violation=10),
        TrajectoryScore(success=0, weighted_violation=0, max_violation=10),
    ]
    metrics = aggregate_metrics(scores)
    assert metrics == {"SR": 2 / 3, "PCR": 5 / 6, "CSR": 0.5, "MG": 1 / 6}
