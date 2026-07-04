import streamlit as st


def render_patient_card(data):

    patient = data.get("patient", {})

    st.subheader("👤 Patient Information")

    c1, c2 = st.columns(2)

    with c1:

        st.info(f"**Name:** {patient.get('name', 'Unknown')}")

        st.info(f"**Age:** {patient.get('age', 'Unknown')}")

    with c2:

        st.info(f"**Gender:** {patient.get('gender', 'Unknown')}")

        st.info(
            f"**Report Type:** {data.get('report_type', 'Unknown')}"
        )