from services.ocr_service import (
    OCRService
)

def test_aadhaar_regex():

    text = (
        "Aadhaar 1234 5678 9012"
    )

    result = (
        OCRService.extract_aadhaar(
            text
        )
    )

    assert (
        result ==
        "123456789012"
    )