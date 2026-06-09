from fastapi import UploadFile
from pydantic import BaseModel


class VerificationRequest(BaseModel):
    name: str
    email: str

    dob: str | None = None

    phone: str | None = None

    aadhaar_number: str | None = None

    pan_number: str | None = None


def validate_uploaded_files(
    aadhaar_file: UploadFile | None,
    pan_file: UploadFile | None,
    passport_file: UploadFile | None
):

    if not any([
        aadhaar_file,
        pan_file,
        passport_file
    ]):
        raise ValueError(
            "At least one document is required"
        )

    return True