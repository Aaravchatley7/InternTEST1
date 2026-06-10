from services.ocr_service import (
    OCRService
)

def test_pan_regex():

    text = (
        "ABCDE1234F"
    )

    result = (
        OCRService.extract_pan(
            text
        )
    )

    assert (
        result ==
        "ABCDE1234F"
    )