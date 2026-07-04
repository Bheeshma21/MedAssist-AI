import streamlit as st

from services.doctor_mode_service import doctor_mode_service


def render_header():

    patient_selected = (
        st.session_state.get("chat_mode", "patient") == "patient"
    )

    # Hide the title after the first message.
    # Keep only Patient/Doctor at the top-right.
    if len(st.session_state.get("messages", [])) > 0:

        left, right = st.columns([10, 2], vertical_alignment="top")

        with right:

            c1, c2 = st.columns(2)

            with c1:

                if st.button(
                    "👤",
                    key="patient_mode",
                    use_container_width=True,
                    type="primary" if patient_selected else "secondary",
                    help="Patient Mode"
                ):

                    doctor_mode_service.set_mode("patient")
                    st.session_state.chat_mode = "patient"
                    st.rerun()

            with c2:

                if st.button(
                    "👨‍⚕️",
                    key="doctor_mode",
                    use_container_width=True,
                    type="primary" if not patient_selected else "secondary",
                    help="Doctor Mode"
                ):

                    doctor_mode_service.set_mode("doctor")
                    st.session_state.chat_mode = "doctor"
                    st.rerun()

        return

    # Landing page
    left, right = st.columns([10, 2], vertical_alignment="top")

    with right:

        c1, c2 = st.columns(2)

        with c1:

            if st.button(
                "👤",
                key="patient_mode",
                use_container_width=True,
                type="primary" if patient_selected else "secondary",
                help="Patient Mode"
            ):

                doctor_mode_service.set_mode("patient")
                st.session_state.chat_mode = "patient"
                st.rerun()

        with c2:

            if st.button(
                "👨‍⚕️",
                key="doctor_mode",
                use_container_width=True,
                type="primary" if not patient_selected else "secondary",
                help="Doctor Mode"
            ):

                doctor_mode_service.set_mode("doctor")
                st.session_state.chat_mode = "doctor"
                st.rerun()