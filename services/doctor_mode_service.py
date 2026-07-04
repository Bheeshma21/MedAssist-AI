import streamlit as st


class DoctorModeService:

    def __init__(self):

        if "chat_mode" not in st.session_state:
            st.session_state.chat_mode = "patient"

    # =====================================
    # Set Mode
    # =====================================

    def set_mode(self, mode):

        mode = mode.lower()

        if mode in ["patient", "doctor"]:

            st.session_state.chat_mode = mode

    # Backward Compatibility
    def set_role(self, role):

        self.set_mode(role)

    # =====================================
    # Get Mode
    # =====================================

    def get_mode(self):

        return st.session_state.get(
            "chat_mode",
            "patient"
        )

    # Backward Compatibility
    def get_role(self):

        return self.get_mode()

    # =====================================
    # Helpers
    # =====================================

    def is_doctor(self):

        return self.get_mode() == "doctor"

    def is_patient(self):

        return self.get_mode() == "patient"

    # =====================================
    # Prompt Instruction
    # =====================================

    def instruction(self):

        if self.is_doctor():

            return """
You are responding to a licensed medical professional.

Use professional medical terminology.

Provide:

• Differential diagnosis
• Clinical reasoning
• Recommended investigations
• Evidence-based treatment
• Relevant clinical guidelines
• Drug interactions
• Follow-up recommendations
• Red flags

Do not simplify medical terminology.
"""

        return """
You are responding to a patient.

Use simple, friendly language.

Explain medical terms when necessary.

Give practical lifestyle advice.

Recommend consulting a healthcare professional whenever appropriate.

Do not provide a definitive diagnosis.
"""


doctor_mode_service = DoctorModeService()