from capabilities.base_document_handler import (
    BaseDocumentHandler
)


class AadhaarHandler(
    BaseDocumentHandler
):

    DOCUMENT_TYPE = "aadhaar"

    REQUIRED_FIELDS = [

        "name",

        "dob",

        "aadhaar_number"
    ]