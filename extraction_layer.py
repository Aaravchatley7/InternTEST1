from services.ocr_service import (
    OCRService
)

from services.llm_service import (
    LLMService
)


class ExtractionLayer:

    @staticmethod
    def extract_document(
        image_path,
        doc_type
    ):

        ocr_result = (
            OCRService.extract_text(
                image_path
            )
        )

        ocr_text = (
            ocr_result["text"]
        )

        fallback_fields = (
            OCRService.extract_fields(
                ocr_text
            )
        )

        extracted = (
            LLMService.extract_fields(
                ocr_text,
                doc_type
            )
        )

        if not extracted:

            extracted = {}

        regex_aadhaar = (
            fallback_fields[
                "aadhaar_number"
            ]
        )

        regex_pan = (
            fallback_fields[
                "pan_number"
            ]
        )

        regex_dob = (
            fallback_fields[
                "dob"
            ]
        )

        if regex_aadhaar:

            extracted[
                "aadhaar_number"
            ] = regex_aadhaar

        if regex_pan:

            extracted[
                "pan_number"
            ] = regex_pan

        if (
            not extracted.get(
                "dob"
            )
            and regex_dob
        ):

            extracted[
                "dob"
            ] = regex_dob

        return {

            "document_type":
                doc_type,

            "ocr_engine":
                ocr_result[
                    "engine"
                ],

            "ocr_confidence":
                ocr_result[
                    "confidence"
                ],

            "ocr_text":
                ocr_text,

            "identity":
                extracted
        }
