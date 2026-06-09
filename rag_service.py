import os
import requests

from dotenv import load_dotenv

load_dotenv()

OPENROUTER_API_KEY = os.getenv(
    "OPENROUTER_API_KEY"
)


class RAGService:

    MODEL = (
        "openai/gpt-oss-120b:free"
    )

    @staticmethod
    def generate_answer(
        question,
        context
    ):

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
                    RAGService.MODEL,

                "messages": [

                    {
                        "role":
                            "system",

                        "content":
                            "Answer ONLY from context."
                    },

                    {
                        "role":
                            "user",

                        "content":
                            f"""
Context:

{context}

Question:

{question}
"""
                    }
                ],

                "temperature":
                    0
            }

        )

        data = response.json()

        print("OPENROUTER RAG RESPONSE:")
        print(data)

        if "choices" not in data:
            raise Exception(
                f"OpenRouter Error: {data}"
            )

        return (
            data["choices"][0]
            ["message"]
            ["content"]
        )