import cv2
import easyocr
import pytesseract
import numpy as np
from PIL import Image

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

        _, thresh = cv2.threshold(
            gray,
            0,
            255,
            cv2.THRESH_BINARY +
            cv2.THRESH_OTSU
        )

        return thresh

    @staticmethod
    def easyocr_extract(image_path):

        result = reader.readtext(
            image_path,
            detail=0
        )

        return "\n".join(result)

    @staticmethod
    def tesseract_extract(image_path):

        img = OCRService.preprocess(
            image_path
        )

        text = pytesseract.image_to_string(
            img,
            config="--oem 3 --psm 6"
        )

        return text

    @staticmethod
    def extract_text(image_path):

        easy_text = OCRService.easyocr_extract(
            image_path
        )

        tess_text = OCRService.tesseract_extract(
            image_path
        )

        if len(easy_text) >= len(tess_text):
            return {
                "ocr_engine":
                    "easyocr",

                "text":
                    easy_text
            }

        return {
            "ocr_engine":
                "tesseract",

            "text":
                tess_text
        }