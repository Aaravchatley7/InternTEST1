class ConfidenceLayer:

    @staticmethod
    def calculate(
        validation_result,
        identity
    ):

        score = 0.0

        reasons = []

        field_results = (
            validation_result[
                "field_results"
            ]
        )

        # Name

        if field_results["name"]:
            score += 0.35

            reasons.append(
                "Name matched"
            )

        # DOB

        if field_results["dob"]:
            score += 0.20

            reasons.append(
                "DOB matched"
            )

        # Aadhaar

        if field_results["aadhaar"]:
            score += 0.25

            reasons.append(
                "Aadhaar matched"
            )

        # PAN

        if field_results["pan"]:
            score += 0.15

            reasons.append(
                "PAN matched"
            )

        # Phone

        if field_results["phone"]:
            score += 0.05

            reasons.append(
                "Phone matched"
            )

        # Extraction Completeness

        extracted_fields = 0

        total_fields = 0

        for key, value in identity.items():

            total_fields += 1

            if value:
                extracted_fields += 1

        completeness = (
            extracted_fields
            / total_fields
        )

        score += (
            completeness * 0.10
        )

        reasons.append(
            f"Extraction completeness: "
            f"{round(completeness*100,1)}%"
        )

        score = min(
            score,
            1.0
        )

        if score >= 0.85:

            level = "HIGH"

        elif score >= 0.65:

            level = "MEDIUM"

        else:

            level = "LOW"

        return {

            "score":
                round(score, 2),

            "level":
                level,

            "reasoning":
                reasons,

            "weights": {

                "name":
                    0.35,

                "dob":
                    0.20,

                "aadhaar":
                    0.25,

                "pan":
                    0.15,

                "phone":
                    0.05,

                "completeness":
                    round(
                        completeness * 0.10,
                        2
                    )
            }
        }
