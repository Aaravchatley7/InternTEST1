class BaseDocumentHandler:

    DOCUMENT_TYPE = "generic"

    REQUIRED_FIELDS = []

    @classmethod
    def get_metadata(cls):

        return {

            "document_type":
                cls.DOCUMENT_TYPE,

            "required_fields":
                cls.REQUIRED_FIELDS
        }