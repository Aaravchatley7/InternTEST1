from services.evidence_ledger import (
    EvidenceLedger
)

class ReplayService:

    @staticmethod
    def replay(trace_id):

        try:

            return (
                EvidenceLedger.load(
                    trace_id
                )
            )

        except FileNotFoundError:

            return {

                "status":
                    "not_found",

                "trace_id":
                    trace_id
            }