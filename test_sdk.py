from sdk.config import (
    SDKConfig
)


def test_sdk_exists():

    assert (

        SDKConfig
        .CAPABILITY_NAME

        ==

        "BHIV Multi-Input Intelligence Platform"
    )