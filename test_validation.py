from layers.validation_layer import (
    ValidationLayer
)


def test_validation_pass():

    form_data = {

        "name": "Aarav Chatley",

        "dob": "29/10/2005",

        "aadhaar_number":
            "503129847654"
    }

    identity = {

        "name": "Aarav Chatley",

        "dob": "29/10/2005",

        "aadhaar_number":
            "503129847654"
    }

    result = (
        ValidationLayer.validate(
            form_data,
            identity
        )
    )

    assert (
        result["validation_result"]
        ==
        "VERIFIED"
    )