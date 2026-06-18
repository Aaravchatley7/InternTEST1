from fastapi.testclient import (
    TestClient
)

from app import app


client = TestClient(
    app
)


def test_replay_endpoint_exists():

    response = (
        client.get(
            "/replay/non-existent"
        )
    )

    assert (
        response.status_code
        in [200, 500]
    )