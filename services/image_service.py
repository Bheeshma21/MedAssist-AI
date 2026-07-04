from PIL import Image

from services.doctor_mode_service import doctor_mode_service
from backend.ai_service import ai_service
from memory.session_memory import session_memory


class ImageService:

    def analyze(self, question):

        image_path = session_memory.get_image()

        if not image_path:

            return {
                "analysis": "Please upload a medical image first."
            }

        image = Image.open(image_path)

        # =====================================================
        # Doctor Mode
        # =====================================================

        doctor_instruction = (
            doctor_mode_service.instruction()
        )

        # =====================================================
        # Prompt
        # =====================================================

        prompt = f"""
You are MedAssist AI.

{doctor_instruction}

You are an experienced physician and radiologist.

Analyze the uploaded medical image.

User Question:

{question}

Instructions:

- Answer the user's specific question first.
- Describe all visible findings.
- Mention possible abnormalities.
- Mention possible medical conditions.
- Explain the limitations of image-based analysis.
- Recommend further investigations when appropriate.
- Never provide a definitive diagnosis.

If Patient Mode is active:
- Explain findings in simple language.
- Avoid unnecessary medical jargon.
- Reassure the user when appropriate.

If Doctor Mode is active:
- Use professional medical terminology.
- Include differential diagnosis.
- Discuss radiological findings.
- Recommend appropriate investigations.
- Mention clinically relevant red flags when applicable.
"""

        answer = ai_service.generate_with_image(
            prompt,
            image
        )

        return {
            "analysis": answer
        }


image_service = ImageService()