import streamlit as st


def render_welcome():

    st.title("🏥 MedAssist AI")

    st.subheader(
        "Intelligent Multimodal Healthcare Copilot"
    )

    st.write(
        """
Welcome to MedAssist AI.

Your personal AI healthcare assistant capable of:

✅ Medical Consultation

✅ Medical Report Analysis

✅ Medical Image Analysis

✅ Drug Interaction Checks

✅ AI Health Dashboard

✅ Voice Responses

✅ Patient & Doctor Modes
"""
    )

    st.divider()

    c1, c2 = st.columns(2)

    with c1:

        if st.button(
            "🔐 Login",
            use_container_width=True
        ):

            st.session_state.page = "login"

            st.rerun()

    with c2:

        if st.button(
            "📝 Register",
            use_container_width=True
        ):

            st.session_state.page = "register"

            st.rerun()