import re
import streamlit as st


class ResponseStyleService:

    def __init__(self):

        if "response_style" not in st.session_state:
            st.session_state.response_style = "normal"

    def detect_style(self, message: str):

        message = message.lower()

        styles = {

            "simple": [
                r"simple",
                r"easy",
                r"easy words",
                r"like i'm 10",
                r"like i am 10",
                r"child",
                r"explain simply"
            ],

            "doctor": [
                r"doctor",
                r"technical",
                r"clinical",
                r"professional",
                r"medical terms"
            ],

            "brief": [
                r"brief",
                r"short",
                r"summary",
                r"in points",
                r"bullet points"
            ],

            "detailed": [
                r"detailed",
                r"deep",
                r"complete explanation",
                r"elaborate"
            ]

        }

        for style, patterns in styles.items():

            for pattern in patterns:

                if re.search(pattern, message):

                    st.session_state.response_style = style

                    return style

        return None

    def instruction(self):

        style = st.session_state.get(
            "response_style",
            "normal"
        )

        if style == "simple":

            return """
Explain like you are talking to a patient.

Use very simple language.

Avoid medical jargon.

Use examples whenever possible.
"""

        if style == "doctor":

            return """
Answer like an experienced physician.

Use proper medical terminology.

Include differential diagnosis whenever appropriate.

Include investigations and treatment.
"""

        if style == "brief":

            return """
Answer in short bullet points.

Keep the response concise.
"""

        if style == "detailed":

            return """
Provide a comprehensive explanation.

Explain causes, symptoms, diagnosis,
treatment, prevention and prognosis.
"""

        return ""


response_style_service = ResponseStyleService()