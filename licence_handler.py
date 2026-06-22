from capabilities.base_document_handler import (
    BaseDocumentHandler
)


class DrivingLicenceHandler(
    BaseDocumentHandler
):

    DOCUMENT_TYPE = "driving_licence"

    REQUIRED_FIELDS = [

        "name",

        "licence_number",

        "dob"
    ]