import streamlit as st


def render_upload_menu():

    uploaded_file = None
    action = None

    if "web_search" not in st.session_state:
        st.session_state.web_search = False

    # ==============================
    # Upload Popover
    # ==============================

    with st.popover("➕"):

        st.markdown("### Add to Chat")

        # --------------------------
        # Web Search
        # --------------------------

        st.session_state.web_search = st.toggle(
            "🌐 Web Search",
            value=st.session_state.web_search
        )

        st.divider()

        # --------------------------
        # Upload
        # --------------------------

        uploaded_file = st.file_uploader(
            "Upload",
            type=["pdf", "png", "jpg", "jpeg"],
            key="chat_upload"
        )

        st.caption("PDF • PNG • JPG • JPEG")

        st.divider()

        # --------------------------
        # Voice / Video
        # --------------------------

        c1, c2 = st.columns(2)

        with c1:

            if st.button(
                "🎤 Voice",
                key="voice_btn",
                use_container_width=True
            ):
                action = "voice"

        with c2:

            if st.button(
                "📹 Video",
                key="video_btn",
                use_container_width=True
            ):
                action = "video"

    return (
        uploaded_file,
        action,
        st.session_state.web_search
    )