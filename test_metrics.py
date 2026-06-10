from layers.observability_layer import (
    ObservabilityLayer
)

def test_metrics_structure():

    metrics = (
        ObservabilityLayer
        .get_metrics()
    )

    assert (
        "total_requests"
        in metrics
    )

    assert (
        "total_errors"
        in metrics
    )