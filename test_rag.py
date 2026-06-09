from layers.rag_layer import (
    RAGLayer
)


def test_rag_exists():

    assert (
        hasattr(
            RAGLayer,
            "ask"
        )
    )