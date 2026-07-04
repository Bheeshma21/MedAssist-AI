from agents.rag_agent import retrieve_medical_context
from backend.ai_service import ai_service
from memory.session_memory import session_memory
from services.language_service import language_service
from services.response_style_service import response_style_service
from services.doctor_mode_service import doctor_mode_service


class QAService:

    def answer(self, question: str):

        # ----------------------------------
        # Detect Language Preference
        # ----------------------------------

        language_service.detect_language_request(
            question
        )

        language_instruction = (
            language_service.language_instruction()
        )
        response_style_service.detect_style(
             question
        )
        style_instruction = (
            response_style_service.instruction()
        )
        doctor_instruction = (
            doctor_mode_service.instruction()
            )

        # ----------------------------------
        # Retrieve RAG Context
        # ----------------------------------

        context = retrieve_medical_context(question)

        # ----------------------------------
        # Conversation Memory
        # ----------------------------------

        conversation = session_memory.get_conversation()

        conversation_text = ""

        if conversation:

            for msg in conversation:

                conversation_text += (
                    f"{msg['role'].capitalize()}: "
                    f"{msg['content']}\n"
                )
        # ----------------------------------
        # Uploaded Report
        # ----------------------------------

        report_text = session_memory.get_report_text()

        # ----------------------------------
        # Build Prompt
        # ----------------------------------

        if context["has_context"]:

            prompt = f"""
            You are MedAssist AI.
            {language_instruction}
            {style_instruction}
            {doctor_instruction}
You are MedAssist AI.

You are an experienced physician.

Answer the user's medical question.

Use the following information in this priority:

1. Previous Conversation
2. Uploaded Medical Report (if available)
3. Retrieved Medical Documents (RAG)
4. Your medical knowledge

-----------------------------------
Conversation History
-----------------------------------

{conversation_text}

-----------------------------------
Uploaded Medical Report
-----------------------------------

{report_text if report_text else "No report uploaded."}

-----------------------------------
Retrieved Medical Context
-----------------------------------

{context["medical_context"]}

-----------------------------------
User Question
-----------------------------------

{question}

Instructions:

- Answer directly.
- Be medically accurate.
- If the report contains relevant values,
  mention them.
- If RAG contains useful information,
  use it.
- If neither contains the answer,
  use your medical knowledge.
- Never invent patient-specific values.
- Explain in simple language.
- Recommend consulting a healthcare
  professional whenever appropriate.
"""

        else:

            prompt = f"""
            You are MedAssist AI.
            {language_instruction}
            {style_instruction}
You are MedAssist AI.

You are an experienced physician.

No relevant medical documents were retrieved.

Use:

1. Previous Conversation
2. Uploaded Medical Report (if available)
3. Your medical knowledge

-----------------------------------
Conversation History
-----------------------------------

{conversation_text}

-----------------------------------
Uploaded Medical Report
-----------------------------------

{report_text if report_text else "No report uploaded."}

-----------------------------------
User Question
-----------------------------------

{question}

Instructions:

- Answer clearly.
- Explain in simple language.
- If the uploaded report helps,
  use it.
- If needed, use your medical knowledge.
- Never invent patient-specific values.
- Recommend consulting a healthcare
  professional whenever appropriate.
"""

        # ----------------------------------
        # Generate Response
        # ----------------------------------

        answer = ai_service.generate(prompt)

        return {

            "answer": answer,

            "sources": context["sources"]

        }


qa_service = QAService()