import os


class SDKConfig:

    VERSION = "1.0.0"

    CAPABILITY_NAME = (
        "BHIV Multi-Input Intelligence Platform"
    )

    OPENROUTER_API_KEY = (
        os.getenv(
            "OPENROUTER_API_KEY"
        )
    )