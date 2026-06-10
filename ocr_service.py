import cv2
import easyocr
import pytesseract
import re

reader = easyocr.Reader(
    ['en'],
    gpu=False
)


class OCRService:

    @staticmethod
    def preprocess(image_path):

        image = cv2.imread(image_path)

        if image is None:
            raise ValueError(
                f"Cannot read image: {image_path}"
            )

        gray = cv2.cvtColor(
            image,
            cv2.COLOR_BGR2GRAY
        )

        gray = cv2.GaussianBlur(
            gray,
            (3, 3),
            0
        )

        gray = cv2.fastNlMeansDenoising(
            gray
        )

        thresh = cv2.adaptiveThreshold(
            gray,
            255,
            cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
            cv2.THRESH_BINARY,
            11,
            2
        )

        return thresh

    @staticmethod
    def easyocr_extract(image_path):

        results = reader.readtext(
            image_path,
            detail=1
        )

        text = "\n".join(
            [r[1] for r in results]
        )

        confidence = 0

        if results:

            confidence = sum(
                r[2] for r in results
            ) / len(results)

        return {

            "engine":
                "easyocr",

            "text":
                text,

            "confidence":
                round(
                    confidence,
                    2
                )
        }

    @staticmethod
    def tesseract_extract(image_path):

        processed = OCRService.preprocess(
            image_path
        )

        text = pytesseract.image_to_string(

            processed,

            config=
            "--oem 3 --psm 6"
        )

        return {

            "engine":
                "tesseract",

            "text":
                text,

            "confidence":
                0.50
        }

    @staticmethod
    def extract_text(image_path):

        easy = OCRService.easyocr_extract(
            image_path
        )

        tess = OCRService.tesseract_extract(
            image_path
        )

        if easy["confidence"] >= 0.50:

            return easy

        if len(easy["text"]) >= len(tess["text"]):

            return easy

        return tess

    @staticmethod
    def extract_aadhaar(text):

        matches = re.findall(
            r"\d{4}[\s\-\.]?\d{4}[\s\-\.]?\d{4}",
            text
        )

        if matches:

            return re.sub(
                r"\D",
                "",
                matches[0]
            )

        return ""

    @staticmethod
    def extract_pan(text):

        matches = re.findall(
            r"[A-Z]{5}[0-9]{4}[A-Z]",
            text.upper()
        )

        if matches:

            return matches[0]

        return ""

    @staticmethod
    def extract_dob(text):

        patterns = [

            r"\d{2}/\d{2}/\d{4}",

            r"\d{2}-\d{2}-\d{4}",

            r"\d{4}-\d{2}-\d{2}"
        ]

        for pattern in patterns:

            match = re.search(
                pattern,
                text
            )

            if match:

                return match.group()

        return ""

    @staticmethod
    def extract_fields(text):

        return {

            "aadhaar_number":

                OCRService.extract_aadhaar(
                    text
                ),

            "pan_number":

                OCRService.extract_pan(
                    text
                ),

            "dob":

                OCRService.extract_dob(
                    text
                )
        }
