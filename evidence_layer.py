class EvidenceLayer:

    @staticmethod
    def build(
        form_data,
        identity,
        validation_result
    ):

        evidence = []

        field_results = (
            validation_result[
                "field_results"
            ]
        )

        mappings = {

            "name":
                "name",

            "dob":
                "dob",

            "aadhaar":
                "aadhaar_number",

            "pan":
                "pan_number",

            "phone":
                "phone"
        }

        for result_key, id_key in mappings.items():

            evidence.append({

                "field":
                    result_key,

                "submitted":
                    form_data.get(
                        id_key,
                        ""
                    ),

                "extracted":
                    identity.get(
                        id_key,
                        ""
                    ),

                "status":
                    (
                        "MATCH"
                        if field_results[
                            result_key
                        ]
                        else "MISMATCH"
                    )
            })

        return evidence