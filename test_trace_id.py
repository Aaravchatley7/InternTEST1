from layers.observability_layer import (
    ObservabilityLayer
)

def test_trace_id_created():

    trace = (
        ObservabilityLayer
        .create_trace()
    )

    assert trace is not None

    assert len(trace) > 10