import uuid

from services.evidence_ledger import (
    EvidenceLedger
)

from services.replay_service import (
    ReplayService
)


def test_replay_returns_same_output():

    trace_id = str(
        uuid.uuid4()
    )

    payload = {

        "value":
            "replay-test"
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

    replay = (
        ReplayService
        .replay(
            trace_id
        )
    )

    assert (
        replay["trace_id"]
        == trace_id
    )

    assert (
        replay["request"]
        == payload
    )