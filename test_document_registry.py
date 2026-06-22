from capabilities.document_registry import (
    DocumentRegistry
)


def test_document_registry():

    docs = (

        DocumentRegistry
        .get_supported()
    )

    assert "aadhaar" in docs

    assert "pan" in docs

    assert "passport" in docs

    assert "invoice" in docs