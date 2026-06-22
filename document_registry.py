from capabilities.aadhaar_handler import (
    AadhaarHandler
)

from capabilities.pan_handler import (
    PANHandler
)

from capabilities.passport_handler import (
    PassportHandler
)

from capabilities.licence_handler import (
    DrivingLicenceHandler
)

from capabilities.voter_handler import (
    VoterIDHandler
)

from capabilities.certificate_handler import (
    CertificateHandler
)

from capabilities.invoice_handler import (
    InvoiceHandler
)

from capabilities.government_form_handler import (
    GovernmentFormHandler
)


class DocumentRegistry:

    DOCUMENTS = {

        "aadhaar":
            AadhaarHandler,

        "pan":
            PANHandler,

        "passport":
            PassportHandler,

        "driving_licence":
            DrivingLicenceHandler,

        "voter_id":
            VoterIDHandler,

        "certificate":
            CertificateHandler,

        "invoice":
            InvoiceHandler,

        "government_form":
            GovernmentFormHandler
    }

    @staticmethod
    def get_supported():

        return {

            key: value.get_metadata()

            for key, value

            in DocumentRegistry.DOCUMENTS.items()
        }