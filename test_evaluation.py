import json

from evaluation.run_evaluation import (
    evaluate
)


def test_evaluation_runs():

    evaluate()

    with open(
        "evaluation/evaluation_results.json",
        "r"
    ) as f:

        results = json.load(f)

    assert (
        "accuracy"
        in results
    )

    assert (
        "precision"
        in results
    )

    assert (
        "recall"
        in results
    )

    assert (
        "f1_score"
        in results
    )