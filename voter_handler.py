from capabilities.base_document_handler import (
    BaseDocumentHandler
)


class VoterIDHandler(
    BaseDocumentHandler
):

    DOCUMENT_TYPE = "voter_id"

    REQUIRED_FIELDS = [

        "name",

        "voter_id_number"
    ]