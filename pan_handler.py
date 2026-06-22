from capabilities.base_document_handler import (
    BaseDocumentHandler
)


class PANHandler(
    BaseDocumentHandler
):

    DOCUMENT_TYPE = "pan"

    REQUIRED_FIELDS = [

        "name",

        "dob",

        "pan_number"
    ]