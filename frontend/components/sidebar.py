import streamlit as st

from controllers.session_controller import session_controller
from controllers.chat_controller import chat_controller


def render_sidebar():

    if "rename_chat" not in st.session_state:
        st.session_state.rename_chat = None

    with st.sidebar:

        # =====================================
        # Sidebar CSS
        # =====================================

        st.markdown(
            """
            <style>

            div[data-testid="stPopover"] > button{
                width:32px !important;
                min-width:32px !important;
                height:32px !important;
                padding:0 !important;
                border-radius:8px !important;
                font-size:18px !important;
            }

            </style>
            """,
            unsafe_allow_html=True,
        )

        # =====================================
        # Logo
        # =====================================

        st.markdown(
            """
            <h2 style="margin-bottom:0;">
                🏥 MedAssist AI
            </h2>

            <p style="color:#9CA3AF;margin-top:0;font-size:14px;">
                Intelligent Healthcare Copilot
            </p>
            """,
            unsafe_allow_html=True,
        )

        st.write("")

        # =====================================
        # New Chat
        # =====================================

        if st.button(
            "➕ New Chat",
            type="primary",
            use_container_width=True,
        ):

            st.session_state.session_id = None
            st.session_state.messages = []
            st.session_state.conversation_context = []
            st.session_state.rename_chat = None

            st.rerun()

        st.write("")

        # =====================================
        # Search
        # =====================================

        search = st.text_input(
            "Search",
            placeholder="Search chats...",
            label_visibility="collapsed",
        )

        st.markdown("### 💬 Chats")

        chats = chat_controller.get_chats()

        if search.strip():

            chats = [
                c
                for c in chats
                if search.lower() in c["title"].lower()
            ]

        # =====================================
        # Chat List
        # =====================================

        if chats:

            for chat in chats:

                title = chat["title"]

                if len(title) > 28:
                    title = title[:28] + "..."

                selected = (
                    chat["id"]
                    == st.session_state.get("session_id")
                )

                left, right = st.columns(
                    [12, 1],
                    vertical_alignment="center",
                )

                # --------------------------
                # Conversation Button
                # --------------------------

                with left:

                    if st.button(
                        title,
                        key=f"chat_{chat['id']}",
                        use_container_width=True,
                        type="primary" if selected else "secondary",
                    ):

                        st.session_state.session_id = chat["id"]

                        st.session_state.messages = (
                            chat_controller.load_history()
                        )

                        st.session_state.rename_chat = None

                        st.rerun()

                # --------------------------
                # Three Dots
                # --------------------------

                with right:

                    with st.popover("⋮"):

                        if st.button(
                            "✏ Rename",
                            key=f"rename_{chat['id']}",
                            use_container_width=True,
                        ):

                            st.session_state.rename_chat = chat["id"]
                            st.rerun()

                        if st.button(
                            "🔗 Share",
                            key=f"share_{chat['id']}",
                            use_container_width=True,
                        ):

                            st.toast("Share feature coming soon.")

                        if st.button(
                            "🗑 Delete",
                            key=f"delete_{chat['id']}",
                            use_container_width=True,
                        ):

                            session_controller.delete_chat(chat["id"])

                            if (
                                st.session_state.get("session_id")
                                == chat["id"]
                            ):
                                st.session_state.session_id = None
                                st.session_state.messages = []

                            st.rerun()

                # --------------------------
                # Rename Area
                # --------------------------

                if st.session_state.rename_chat == chat["id"]:

                    new_title = st.text_input(
                        "Rename Conversation",
                        value=chat["title"],
                        key=f"title_{chat['id']}",
                    )

                    c1, c2 = st.columns(2)

                    with c1:

                        if st.button(
                            "Save",
                            key=f"save_{chat['id']}",
                            use_container_width=True,
                        ):

                            session_controller.rename_chat(
                                chat["id"],
                                new_title,
                            )

                            st.session_state.rename_chat = None
                            st.rerun()

                    with c2:

                        if st.button(
                            "Cancel",
                            key=f"cancel_{chat['id']}",
                            use_container_width=True,
                        ):

                            st.session_state.rename_chat = None
                            st.rerun()

        else:

            st.caption("No conversations yet.")

        st.divider()

        st.caption(
            f"👤 {st.session_state.get('user_name','User')}"
        )

        if st.button(
            "🚪 Sign Out",
            use_container_width=True,
        ):

            st.session_state.clear()
            st.session_state.page = "welcome"
            st.rerun()