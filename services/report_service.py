from agents.dashboard_agent import dashboard_agent

from backend.ai_service import ai_service
from memory.session_memory import session_memory
from services.doctor_mode_service import doctor_mode_service


class ReportService:

    def analyze(self, question):

        report_text = session_memory.get_report_text()

        if not report_text:

            return {

                "analysis": "Please upload a medical report first.",

                "dashboard": None

            }

        # =====================================================
        # Doctor Mode
        # =====================================================

        doctor_instruction = (
            doctor_mode_service.instruction()
        )

        # =====================================================
        # Generate Dashboard ONLY ONCE
        # =====================================================

        dashboard = session_memory.get_dashboard()

        if dashboard is None:

            print("Generating Dashboard...")

            dashboard = dashboard_agent.generate(
                report_text
            )

            session_memory.save_dashboard(
                dashboard
            )

        else:

            print("Using Cached Dashboard")

        # =====================================================
        # Chat Answer
        # =====================================================

        prompt = f"""
You are MedAssist AI.

{doctor_instruction}

The user has uploaded the following medical report.

Medical Report:

{report_text}

User Question:

{question}

Instructions:

- Answer ONLY the user's question.
- Do NOT repeat the complete report.
- If Patient Mode is active:
    • Explain in simple language.
    • Avoid unnecessary medical jargon.
    • Give practical advice.
- If Doctor Mode is active:
    • Use professional medical terminology.
    • Include clinical reasoning when appropriate.
    • Mention differential diagnosis if relevant.
    • Recommend investigations if needed.
- Never invent laboratory values.
- Keep the response medically accurate.
"""

        answer = ai_service.generate(prompt)

        return {

            "analysis": answer,

            "dashboard": dashboard,

            "raw_text": report_text

        }


report_service = ReportService()