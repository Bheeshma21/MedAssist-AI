import json

from services.doctor_mode_service import doctor_mode_service
from backend.ai_service import ai_service


class DashboardAgent:

    def generate(self, report_text):

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

You are an experienced physician.

Analyze the following medical report.

Return ONLY valid JSON.

Do not include markdown.
Do not include explanations.
Do not include ```json.

JSON Schema:

{{
    "report_type": "",

    "patient": {{
        "name": "",
        "age": "",
        "gender": ""
    }},

    "health_score": 0,

    "risk_level": "",

    "summary": "",

    "body_systems": [
        {{
            "name": "",
            "icon": "",
            "status": "",
            "reason": ""
        }}
    ],

    "tests": [
        {{
            "name": "",
            "value": "",
            "normal_range": "",
            "status": "",
            "severity": "",
            "explanation": ""
        }}
    ],

    "possible_conditions": [],

    "recommendations": [],

    "action_plan": []
}}

Instructions:

1. Detect the report type.
2. Calculate a health score (0-100).
3. Determine the overall risk level.
4. Generate a concise summary.
5. Extract every laboratory test.
6. Identify possible conditions.
7. Generate practical recommendations.
8. Generate a 5-10 step action plan.
9. Analyze these body systems when applicable:
   - Blood System 🩸
   - Heart ❤️
   - Kidney 🫘
   - Liver 🟤
   - Respiratory 🫁
   - Nervous System 🧠
   - Digestive System 🍽️

If Patient Mode is active:
- Write the summary in simple language.
- Avoid unnecessary medical jargon.
- Make recommendations easy to understand.

If Doctor Mode is active:
- Write the summary using professional medical terminology.
- Include important clinical findings.
- Mention likely differential diagnoses when appropriate.
- Make recommendations suitable for healthcare professionals.

Medical Report:

{report_text}
"""

        response = ai_service.generate(prompt)

        try:

            return json.loads(response)

        except Exception:

            return {

                "report_type": "Unknown",

                "patient": {},

                "health_score": 0,

                "risk_level": "Unknown",

                "summary": response,

                "body_systems": [],

                "tests": [],

                "possible_conditions": [],

                "recommendations": [],

                "action_plan": []

            }


dashboard_agent = DashboardAgent()