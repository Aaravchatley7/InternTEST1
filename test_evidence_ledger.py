import uuid

from services.evidence_ledger import (
    EvidenceLedger
)


def test_ledger_store_and_load():

    trace_id = str(
        uuid.uuid4()
    )

    sample = {

        "test": True
    }

    EvidenceLedger.store(

        trace_id,

        sample,

        sample,

        sample,

        sample,

        sample,

        sample
    )

    loaded = (
        EvidenceLedger.load(
            trace_id
        )
    )

    assert (
        loaded["trace_id"]
        == trace_id
    )

    assert (
        loaded["request"]
        == sample
    )