from capabilities.base_document_handler import (
    BaseDocumentHandler
)


class PassportHandler(
    BaseDocumentHandler
):

    DOCUMENT_TYPE = "passport"

    REQUIRED_FIELDS = [

        "name",

        "passport_number",

        "dob"
    ]