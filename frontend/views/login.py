import streamlit as st

from controllers.auth_controller import auth_controller


def render_login():

    st.title("🔐 Login")

    if st.button("⬅ Back"):

        st.session_state.page = "welcome"
        st.rerun()

    st.divider()

    with st.form("login_form"):

        email = st.text_input("Email")

        password = st.text_input(
            "Password",
            type="password"
        )

        submitted = st.form_submit_button("Login")

    if submitted:

        success, result = auth_controller.login(
            email,
            password
        )

        if success:

            st.session_state.logged_in = True

            st.session_state.user = dict(result)

            st.session_state.user_id = result["id"]

            st.session_state.user_name = result["name"]

            st.session_state.role = result["role"]

            # Default mode after login
            st.session_state.chat_mode = "patient"

            st.session_state.page = "dashboard"

            st.rerun()

        else:

            st.error(result)