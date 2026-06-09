from layers.confidence_layer import (
    ConfidenceLayer
)


def test_confidence():

    validation = {

        "field_results": {

            "name": True,

            "dob": True,

            "aadhaar": True,

            "pan": False,

            "phone": False
        }
    }

    identity = {

        "name": "Aarav",

        "dob": "29/10/2005",

        "aadhaar_number":
            "503129847654"
    }

    result = (
        ConfidenceLayer.calculate(
            validation,
            identity
        )
    )

    assert result["score"] > 0