from pydantic import BaseModel
from typing import Optional


class IdentityModel(BaseModel):
    name: Optional[str] = None
    dob: Optional[str] = None

    aadhaar_number: Optional[str] = None
    pan_number: Optional[str] = None
    passport_number: Optional[str] = None

    phone: Optional[str] = None
    gender: Optional[str] = None