import os
import time

from dotenv import load_dotenv
from google import genai
from google.genai.errors import ServerError, ClientError


load_dotenv()


class AIService:

    def __init__(self):

        self.client = None

        api_key = os.getenv("GEMINI_API_KEY")

        if api_key:
            self.client = genai.Client(api_key=api_key)

    def _get_client(self):

        if self.client is None:

            raise RuntimeError(
                "GEMINI_API_KEY is not configured. Set it in the environment before using AI generation."
            )

        return self.client

    # =====================================================
    # Text Generation
    # =====================================================

    def generate(
        self,
        prompt: str
    ) -> str:

        client = self._get_client()

        retries = 3

        for attempt in range(retries):

            try:

                response = client.models.generate_content(

                    model="gemini-2.5-flash",

                    contents=prompt

                )

                return response.text

            except ClientError as e:

                if getattr(e, "code", None) == 429:

                    return """
⚠️ Gemini API quota reached.

The daily free-tier request limit has been exceeded.

Please try again later or update your Gemini API key.

No issue was found with the application.
"""

                raise

            except ServerError:

                if attempt == retries - 1:
                    raise

                print(
                    f"Gemini server busy. Retrying ({attempt + 1}/{retries})..."
                )

                time.sleep(3)

        return "Sorry, the AI service is temporarily unavailable."

    # =====================================================
    # Image + Text Generation
    # =====================================================

    def generate_with_image(
        self,
        prompt: str,
        image
    ) -> str:

        client = self._get_client()

        retries = 3

        for attempt in range(retries):

            try:

                response = client.models.generate_content(

                    model="gemini-2.5-flash",

                    contents=[
                        prompt,
                        image
                    ]

                )

                return response.text

            except ClientError as e:

                if getattr(e, "code", None) == 429:

                    return """
⚠️ Gemini API quota reached.

The daily free-tier request limit has been exceeded.

Please try again later or update your Gemini API key.

No issue was found with the application.
"""

                raise

            except ServerError:

                if attempt == retries - 1:
                    raise

                print(
                    f"Gemini Vision server busy. Retrying ({attempt + 1}/{retries})..."
                )

                time.sleep(3)

        return "Sorry, the AI service is temporarily unavailable."

    # =====================================================
    # Translation
    # =====================================================

    def translate(
        self,
        text: str,
        language: str
    ) -> str:

        prompt = f"""
Translate the following medical text into {language}.

Return only the translated text.

Text:

{text}
"""

        return self.generate(prompt)


ai_service = AIService()