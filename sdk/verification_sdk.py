from layers.extraction_layer import (
    ExtractionLayer
)

from layers.validation_layer import (
    ValidationLayer
)

from layers.confidence_layer import (
    ConfidenceLayer
)

from layers.evidence_layer import (
    EvidenceLayer
)


class VerificationSDK:

    def verify(

        self,

        form_data,

        document_path,

        document_type

    ):

        extraction = (

            ExtractionLayer
            .extract_document(

                document_path,

                document_type
            )
        )

        identity = (

            extraction[
                "identity"
            ]
        )

        validation = (

            ValidationLayer
            .validate(

                form_data,

                identity
            )
        )

        confidence = (

            ConfidenceLayer
            .calculate(

                validation,

                identity
            )
        )

        evidence = (

            EvidenceLayer
            .build(

                form_data,

                identity,

                validation
            )
        )

        return {

            "extraction":
                extraction,

            "validation":
                validation,

            "confidence":
                confidence,

            "evidence":
                evidence
        }