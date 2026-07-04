import streamlit as st

from controllers.auth_controller import auth_controller


def render_register():

    st.title("📝 Create Your MedAssist AI Account")

    st.write(
        "Register to save your consultations, reports, and health history."
    )

    with st.form("register_form"):

        full_name = st.text_input("Full Name")

        email = st.text_input("Email")

        password = st.text_input(
            "Password",
            type="password"
        )

        confirm_password = st.text_input(
            "Confirm Password",
            type="password"
        )

        role = st.selectbox(
            "Account Type",
            [
                "patient",
                "doctor"
            ]
        )

        submit = st.form_submit_button("Register")

    if submit:

        # -------------------------
        # Validation
        # -------------------------

        if not full_name or not email or not password:

            st.error("Please fill all fields.")

            return

        if password != confirm_password:

            st.error("Passwords do not match.")

            return

        # -------------------------
        # Register User
        # -------------------------

        success, message = auth_controller.register(
            full_name,
            email,
            password,
            confirm_password,
            role
        )

        # -------------------------
        # Success
        # -------------------------

        if success:

            st.session_state.registration_success = message

            st.session_state.page = "login"

            st.rerun()

        # -------------------------
        # Failure
        # -------------------------

        else:

            st.error(message)