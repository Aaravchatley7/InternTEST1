from layers.observability_layer import (
    ObservabilityLayer
)


def test_trace():

    trace = (
        ObservabilityLayer
        .create_trace()
    )

    assert trace is not None