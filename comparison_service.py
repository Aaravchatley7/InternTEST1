import re


class ComparisonService:

    @staticmethod
    def clean_name(name):

        return re.sub(
            r"\s+",
            " ",
            re.sub(
                r"[^A-Za-z\s]",
                "",
                str(name or "")
            ).strip().upper()
        )

    @staticmethod
    def normalize_aadhaar(value):

        return re.sub(
            r"\D",
            "",
            str(value or "")
        )

    @staticmethod
    def normalize_pan(value):

        return str(
            value or ""
        ).strip().upper()

    @staticmethod
    def normalize_phone(value):

        digits = re.sub(
            r"\D",
            "",
            str(value or "")
        )

        return (
            digits[-10:]
            if len(digits) >= 10
            else digits
        )

    @staticmethod
    def normalize_dob(value):

        if not value:
            return ""

        return str(value).strip()

    @staticmethod
    def name_match(
        submitted,
        extracted
    ):

        s = ComparisonService.clean_name(
            submitted
        )

        e = ComparisonService.clean_name(
            extracted
        )

        if not s or not e:
            return False

        if s == e:
            return True

        if s in e or e in s:
            return True

        s_words = set(
            s.split()
        )

        e_words = set(
            e.split()
        )

        if not s_words:
            return False

        overlap = (
            len(
                s_words & e_words
            )
            / len(s_words)
        )

        return overlap >= 0.75
    
    @staticmethod
    def compare(
        form_data,
        identity
    ):

        result = {}

        # NAME

        result["name"] = (

            ComparisonService.name_match(

                form_data.get("name"),

                identity.get("name")

            )

        )

        # DOB

        result["dob"] = (

            ComparisonService.normalize_dob(

                form_data.get("dob")

            )

            ==

            ComparisonService.normalize_dob(

                identity.get("dob")

            )

        )

        # AADHAAR

        result["aadhaar"] = (

            ComparisonService.normalize_aadhaar(

                form_data.get(
                    "aadhaar_number"
                )

            )

            ==

            ComparisonService.normalize_aadhaar(

                identity.get(
                    "aadhaar_number"
                )

            )

        )

        # PAN

        result["pan"] = (

            ComparisonService.normalize_pan(

                form_data.get(
                    "pan_number"
                )

            )

            ==

            ComparisonService.normalize_pan(

                identity.get(
                    "pan_number"
                )

            )

        )

        # PHONE

        result["phone"] = (

            ComparisonService.normalize_phone(

                form_data.get(
                    "phone"
                )

            )

            ==

            ComparisonService.normalize_phone(

                identity.get(
                    "phone"
                )

            )

        )

        return result
