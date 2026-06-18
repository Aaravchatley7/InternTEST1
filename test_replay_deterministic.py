import uuid

from services.evidence_ledger import (
    EvidenceLedger
)

from services.replay_service import (
    ReplayService
)


def test_replay_is_deterministic():

    trace_id = str(
        uuid.uuid4()
    )

    payload = {

        "field":
            "deterministic"
    }

    EvidenceLedger.store(

        trace_id,

        payload,

        payload,

        payload,

        payload,

        payload,

        payload
    )

    first = (
        ReplayService
        .replay(
            trace_id
        )
    )

    for _ in range(10):

        current = (
            ReplayService
            .replay(
                trace_id
            )
        )

        assert (
            current == first
        )