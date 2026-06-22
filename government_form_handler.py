from capabilities.base_document_handler import (
    BaseDocumentHandler
)


class GovernmentFormHandler(
    BaseDocumentHandler
):

    DOCUMENT_TYPE = "government_form"

    REQUIRED_FIELDS = [

        "reference_number"
    ]