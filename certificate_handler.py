from capabilities.base_document_handler import (
    BaseDocumentHandler
)


class CertificateHandler(
    BaseDocumentHandler
):

    DOCUMENT_TYPE = "certificate"

    REQUIRED_FIELDS = [

        "student_name",

        "institution",

        "certificate_id"
    ]