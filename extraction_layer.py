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

        extracted = (
            LLMService.extract_fields(
                ocr_result["text"],
                doc_type
            )
        )

        return {

            "document_type":
                doc_type,

            "ocr_engine":
                ocr_result[
                    "ocr_engine"
                ],

            "ocr_text":
                ocr_result[
                    "text"
                ],

            "identity":
                extracted
        }