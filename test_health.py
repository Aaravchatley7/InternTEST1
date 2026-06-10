from layers.observability_layer import (
    ObservabilityLayer
)

def test_health_status():

    health = (
        ObservabilityLayer
        .get_health()
    )

    assert (
        health["status"]
        ==
        "healthy"
    )