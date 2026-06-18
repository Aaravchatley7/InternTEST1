import os
import json


class EvidenceLedger:

    LEDGER_DIR = "ledger"

    @staticmethod
    def initialize():

        os.makedirs(
            EvidenceLedger.LEDGER_DIR,
            exist_ok=True
        )

    @staticmethod
    def store(

        trace_id,

        request_snapshot,

        extraction_snapshot,

        validation_snapshot,

        confidence_snapshot,

        evidence_snapshot,

        response_snapshot

    ):

        EvidenceLedger.initialize()

        ledger_file = (

            f"{EvidenceLedger.LEDGER_DIR}/"

            f"{trace_id}.json"
        )

        with open(
            ledger_file,
            "w"
        ) as f:

            json.dump(

                {

                    "trace_id":
                        trace_id,

                    "request":
                        request_snapshot,

                    "extraction":
                        extraction_snapshot,

                    "validation":
                        validation_snapshot,

                    "confidence":
                        confidence_snapshot,

                    "evidence":
                        evidence_snapshot,

                    "output":
                        response_snapshot

                },

                f,

                indent=4
            )

    @staticmethod
    def load(trace_id):

        ledger_file = (

            f"{EvidenceLedger.LEDGER_DIR}/"

            f"{trace_id}.json"
        )

        with open(
            ledger_file,
            "r"
        ) as f:

            return json.load(f)