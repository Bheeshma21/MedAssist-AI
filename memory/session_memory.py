import streamlit as st


class SessionMemory:

    def initialize(self):

        defaults = {

            "messages": [],

            "session_id": None,

            "uploaded_report": None,

            "uploaded_report_text": None,
            "dashboard_data": None,

            "uploaded_image": None,

            "uploaded_audio": None,

            "uploaded_video": None,

            "patient_profile": {},

            "conversation_context": []

        }

        for key, value in defaults.items():

            if key not in st.session_state:

                st.session_state[key] = value

    # ------------------------------------

    def save_report(self, file_path, report_text):

        st.session_state.uploaded_report = file_path
        st.session_state.uploaded_report_text = report_text

    # ------------------------------------

    def get_report(self):
        return st.session_state.get(
            "uploaded_report",
            None
            )

    # ------------------------------------

    def get_report_text(self):
        return st.session_state.get(
            "uploaded_report_text",
            None
            )

    # ------------------------------------

    def clear_report(self):

        st.session_state.uploaded_report = None
        st.session_state.uploaded_report_text = None

    # ------------------------------------

    def add_message(self, role, content):

        st.session_state.conversation_context.append({

            "role": role,

            "content": content

        })

        if len(st.session_state.conversation_context) > 10:

            st.session_state.conversation_context = (
                st.session_state.conversation_context[-10:]
            )

    # ------------------------------------

    def get_conversation(self):

        return st.session_state.conversation_context
    # ------------------------------------

        # ------------------------------------

    def save_image(
        self,
        image_path
    ):

        st.session_state.uploaded_image = image_path

    # ------------------------------------

    def get_image(self):

        return st.session_state.get(
            "uploaded_image",
            None
        )

    # ------------------------------------

    def clear_image(self):

        st.session_state.uploaded_image = None
    # ------------------------------------

    def save_dashboard(
            self,dashboard
            ):
        st.session_state.dashboard_data = dashboard

# ------------------------------------

    def get_dashboard(
            self
            ):
        return st.session_state.get(
            "dashboard_data",
            None
            )

# ------------------------------------

    def clear_dashboard(
            self
            ):

        st.session_state.dashboard_data = None

session_memory = SessionMemory()