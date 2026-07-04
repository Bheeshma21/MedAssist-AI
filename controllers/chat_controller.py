import streamlit as st

from backend.conversation_engine import conversation_engine
from services.file_restore_service import file_restore_service


class ChatController:

    def send_message(
        self,
        message,
        role="patient",
        web_search=False
    ):

        if not message.strip():
            return "Please enter a message."

        if "user_id" not in st.session_state:
            return "Please login."

        session_id = st.session_state.get(
            "session_id",
            None
        )
        response, session_id = conversation_engine.process(

            user_input=message,

            user_id=st.session_state.user_id,

            role=role,

            session_id=session_id
        )

        st.session_state.session_id = session_id

        return response

    def load_history(self):

        if "user_id" not in st.session_state:
            return []

        if "session_id" not in st.session_state:
            return []

        file_restore_service.restore(
            st.session_state.session_id
        )

        return conversation_engine.load_history(

            st.session_state.user_id,

            st.session_state.session_id

        )

    def get_chats(self):

        if "user_id" not in st.session_state:
            return []

        chats = conversation_engine.get_sessions(
            st.session_state.user_id
        )

        return [

            chat

            for chat in chats

            if chat["title"].strip().lower() != "new chat"

        ]


chat_controller = ChatController()