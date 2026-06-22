from capabilities.base_document_handler import (
    BaseDocumentHandler
)


class InvoiceHandler(
    BaseDocumentHandler
):

    DOCUMENT_TYPE = "invoice"

    REQUIRED_FIELDS = [

        "invoice_number",

        "vendor",

        "amount"
    ]