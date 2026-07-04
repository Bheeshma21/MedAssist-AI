import streamlit as st


def render_assessment(result):

    patient = result["patient_data"]

    risk = result["risk_report"]

    st.subheader("🩺 Clinical Assessment")

    st.success(
        ", ".join(risk["possible_conditions"])
    )

    if "confidence_report" in result:

        confidence = result["confidence_report"]

        st.metric(
            "Confidence",
            f"{confidence['confidence']}%"
        )