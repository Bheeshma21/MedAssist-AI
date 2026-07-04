import streamlit as st


def render_chat():

    if "messages" not in st.session_state:
        st.session_state.messages = [
            {
                "role": "assistant",
                "content": (
                    "👋 Hello! I'm MedAssist AI.\n\n"
                    "I can help you with:\n"
                    "• Health consultations\n"
                    "• Medical questions\n"
                    "• Drug interaction checks\n"
                    "• Medical report analysis\n"
                    "• Image and document review"
                )
            }
        ]

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])