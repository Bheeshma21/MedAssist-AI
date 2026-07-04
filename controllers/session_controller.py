import streamlit as st

from database.database_service import database
from memory.session_memory import session_memory


class SessionController:

    def new_chat(self, user_id):

        session_memory.clear_report()
        session_memory.clear_image()
        session_memory.clear_dashboard()

        st.session_state.conversation_context = []

        session_id = database.create_chat_session(
            user_id=user_id,
            title="New Chat"
        )

        return session_id

    def get_all_chats(self, user_id):

        return database.get_chat_sessions(user_id)

    def rename_chat(
        self,
        session_id,
        title
    ):

        database.rename_chat_session(
            session_id=session_id,
            title=title
        )

    def delete_chat(
        self,
        session_id
    ):

        database.delete_chat_session(
            session_id
        )


session_controller = SessionController()