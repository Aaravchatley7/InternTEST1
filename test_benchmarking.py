from benchmarking.benchmark_runner import (
    generate_report
)


def test_benchmark_report():

    report = (
        generate_report()
    )

    assert (
        "accuracy"
        in report
    )

    assert (
        "precision"
        in report
    )

    assert (
        "recall"
        in report
    )