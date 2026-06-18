from layers.confidence_layer import (
    ConfidenceLayer
)


def test_confidence_explanation():

    validation = {

        "field_results": {

            "name": True,

            "dob": True,

            "aadhaar": True,

            "pan": True,

            "phone": False
        }
    }

    identity = {

        "name": "Aarav",

        "dob": "29/10/2005",

        "aadhaar_number":
            "123456789012",

        "pan_number":
            "ABCDE1234F"
    }

    result = (
        ConfidenceLayer
        .calculate(
            validation,
            identity
        )
    )

    assert (
        "reasoning"
        in result
    )

    assert (
        len(
            result[
                "reasoning"
            ]
        ) > 0
    )

    assert (
        "weights"
        in result
    )