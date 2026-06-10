from services.comparison_service import (
    ComparisonService
)


class ValidationLayer:

    @staticmethod
    def calculate_score(
        comparison_results
    ):

        score = 0

        if comparison_results["name"]:
            score += 35

        if comparison_results["dob"]:
            score += 20

        if comparison_results["aadhaar"]:
            score += 25

        if comparison_results["pan"]:
            score += 15

        if comparison_results["phone"]:
            score += 5

        return score
    
    @staticmethod
    def validate(
        form_data,
        identity
    ):

        comparison = (
            ComparisonService.compare(
                form_data,
                identity
            )
        )

        validation_score = (
            ValidationLayer
            .calculate_score(
                comparison
            )
        )

        validation_result = (
            "VERIFIED"
            if validation_score >= 60
            else "FAILED"
        )

        return {

            "validation_result":
                validation_result,

            "validation_score":
                validation_score,

            "field_results":
                comparison
        }
