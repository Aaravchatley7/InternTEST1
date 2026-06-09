
import os
import json
import requests

from dotenv import load_dotenv

load_dotenv()

OPENROUTER_API_KEY = os.getenv(
    "OPENROUTER_API_KEY"
)

class LLMService:

    MODEL = (
        "openai/gpt-oss-120b:free"
    )

    @staticmethod
    def build_prompt(
        text,
        doc_type
    ):

        return f"""
You are an identity document parser.

Document Type:
{doc_type}

OCR TEXT:

{text}

Return ONLY valid JSON.

Fields:

{{
"name":"",
"dob":"",
"aadhaar_number":"",
"pan_number":"",
"passport_number":"",
"phone":"",
"gender":""
}}
"""

    @staticmethod
    def extract_fields(
        text,
        doc_type
    ):

        prompt = (
            LLMService
            .build_prompt(
                text,
                doc_type
            )
        )

        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",

            headers={
                "Authorization":
                    f"Bearer {OPENROUTER_API_KEY}",

                "Content-Type":
                    "application/json"
            },

            json={
                "model":
                    LLMService.MODEL,

                "messages": [
                    {
                        "role":
                            "user",

                        "content":
                            prompt
                    }
                ],

                "temperature":
                    0
            },

            timeout=30
        )

        data = response.json()

        print("OPENROUTER RESPONSE:")
        print(data)

        if "choices" not in data:
            raise Exception(
                f"OpenRouter Error: {data}"
            )

        content = (
            data["choices"][0]
            ["message"]
            ["content"]
        )

        content = (
            content
            .replace("```json", "")
            .replace("```", "")
            .strip()
        )

        return json.loads(
            content
        )