from services.comparison_service import (
    ComparisonService
)

def test_identity_pipeline():

    form_data = {

        "name":
            "Aarav Chatley",

        "aadhaar_number":
            "123456789012"
    }

    extracted = {

        "name":
            "AARAV CHATLEY",

        "aadhaar_number":
            "123456789012"
    }

    result = (
        ComparisonService.compare(
            form_data,
            extracted
        )
    )

    assert result["name"]
    assert result["aadhaar"]