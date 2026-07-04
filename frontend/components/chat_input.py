import streamlit as st

from frontend.components.upload_menu import render_upload_menu


def render_chat_input():

    # =====================================
    # Session State
    # =====================================

    if "web_search" not in st.session_state:
        st.session_state.web_search = False

    if "send_from_enter" not in st.session_state:
        st.session_state.send_from_enter = False

    prompt = ""
    uploaded_file = None
    action = None

    # =====================================
    # Layout
    # =====================================

    col1, col2, col3 = st.columns(
        [1, 14, 1],
        vertical_alignment="center"
    )

    # =====================================
    # Upload Menu
    # =====================================

    with col1:

        uploaded_file, action, web_search = render_upload_menu()

        st.session_state.web_search = web_search

    # =====================================
    # Prompt
    # =====================================

    with col2:

        prompt = st.text_input(
            "Message",
            placeholder="Ask MedAssist AI anything...",
            label_visibility="collapsed",
            key="chat_prompt",
            on_change=lambda: st.session_state.update(
                {"send_from_enter": True}
            )
        )

    # =====================================
    # Send Button
    # =====================================

    with col3:

        button_send = st.button(
            "⬆",
            key="send_button",
            type="primary",
            use_container_width=True,
            help="Send"
        )

    # =====================================
    # Send Logic
    # =====================================

    send = button_send or st.session_state.send_from_enter

    if send:
        st.session_state.send_from_enter = False

    # =====================================
    # Temporary Features
    # =====================================

    if action == "voice":
        st.toast("🎤 Voice feature coming soon.")

    elif action == "video":
        st.toast("📹 Video feature coming soon.")

    # =====================================
    # Return
    # =====================================

    return (
        prompt,
        uploaded_file,
        st.session_state.web_search,
        send
    )