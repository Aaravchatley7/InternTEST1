from datetime import datetime
import uuid


class ProvenanceService:

    SCHEMA_VERSION = "v1"

    CONTRACT_VERSION = "v2"

    EVALUATION_VERSION = "v1"

    @staticmethod
    def build(
        trace_id,
        origin_source,
        confidence_source
    ):

        return {

            "trace_id":
                trace_id,

            "request_id":
                str(uuid.uuid4()),

            "schema_version":
                ProvenanceService
                .SCHEMA_VERSION,

            "contract_version":
                ProvenanceService
                .CONTRACT_VERSION,

            "evaluation_version":
                ProvenanceService
                .EVALUATION_VERSION,

            "timestamp":
                datetime.utcnow()
                .isoformat(),

            "origin_source":
                origin_source,

            "confidence_source":
                confidence_source
        }