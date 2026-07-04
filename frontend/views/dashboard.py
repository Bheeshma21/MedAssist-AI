import streamlit as st

from memory.session_memory import session_memory
from frontend.components.sidebar import render_sidebar
from frontend.components.header import render_header
from frontend.components.chat import render_chat
from frontend.components.chat_input import render_chat_input
from frontend.components.dashboard.dashboard import (
    render_dashboard as render_ai_dashboard
)

from services.upload_manager import upload_manager

from controllers.chat_controller import chat_controller


def render_dashboard():

    # ======================================
    # Initialize Session State
    # ======================================

    if "messages" not in st.session_state:
        st.session_state.messages = []

    if "chat_mode" not in st.session_state:
        st.session_state.chat_mode = "patient"

    if "web_search" not in st.session_state:
        st.session_state.web_search = False

    # ======================================
    # Sidebar
    # ======================================

    render_sidebar()

    # ======================================
    # Header
    # ======================================
    render_header()

    # ======================================
    # Health Dashboard
    # ======================================

    dashboard = session_memory.get_dashboard()

    if dashboard:
        render_ai_dashboard(dashboard)

    # ======================================
    # Restore Previous Conversation
    # ======================================

    if (
        st.session_state.get("session_id")
        and
        not st.session_state.messages
    ):

        st.session_state.messages = (
            chat_controller.load_history()
        )

    # ======================================
    # Chat Window
    # ======================================

    render_chat()

    # ======================================
    # Input Bar
    # ======================================

    prompt, uploaded_file, web_search, sent = render_chat_input()

    # ======================================
    # Upload Handling
    # ======================================

    if uploaded_file:

        if uploaded_file.type == "application/pdf":

            result = upload_manager.save_report(

                uploaded_file,

                st.session_state.user_id,

                st.session_state.session_id

            )

            st.session_state.messages.append({

                "role": "assistant",

                "content": f"""## ✅ Medical Report Uploaded

**File:** `{result['filename']}`

Your report has been uploaded successfully.

You can now ask:

• Summarize my report

• Explain my blood report

• Which values are abnormal?

• What foods should I eat?

• What should I discuss with my doctor?
"""

            })

        elif uploaded_file.type.startswith("image"):

            st.session_state.messages.append({

                "role": "assistant",

                "content": "🖼️ Medical image uploaded successfully."

            })

        else:

            st.warning("Unsupported file type.")

        st.rerun()

    # ======================================
    # User Message
    # ======================================

    if sent and prompt.strip():

        st.session_state.messages.append({

            "role": "user",

            "content": prompt

        })

        with st.spinner("Thinking..."):

            response = chat_controller.send_message(
                message=prompt,
                role=st.session_state.get(
                    "chat_mode",
                    "patient"
                )

)

        st.session_state.messages.append({

            "role": "assistant",

            "content": response

        })

        st.rerun()