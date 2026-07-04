import streamlit as st

from services.voice_service import voice_service


def render_chat():

    if "messages" not in st.session_state:
        st.session_state.messages = []

    # =====================================================
    # Empty Landing Screen
    # =====================================================

    if len(st.session_state.messages) == 0:

        st.markdown("<br>", unsafe_allow_html=True)

        c1, c2, c3 = st.columns([1, 3, 1])

        with c2:

            st.markdown(
                """
                <div style="text-align:center;">

                <h1 style="font-size:56px;margin-bottom:8px;">
                🏥 MedAssist AI
                </h1>

                <p style="
                color:#9CA3AF;
                font-size:20px;
                margin-bottom:35px;">
                Intelligent Healthcare Copilot
                </p>

                <h3 style="margin-bottom:35px;">
                How can I help you today?
                </h3>

                </div>
                """,
                unsafe_allow_html=True
            )

            a, b = st.columns(2)

            with a:

                st.button(
                    "🩸 Analyze Blood Report",
                    use_container_width=True,
                    disabled=True
                )

                st.button(
                    "💊 Explain Medicines",
                    use_container_width=True,
                    disabled=True
                )

            with b:

                st.button(
                    "🩻 Analyze Medical Image",
                    use_container_width=True,
                    disabled=True
                )

                st.button(
                    "❤️ Heart Disease Information",
                    use_container_width=True,
                    disabled=True
                )

        return

    # =====================================================
    # Chat Messages
    # =====================================================

    for index, message in enumerate(st.session_state.messages):

        avatar = "🩺" if message["role"] == "assistant" else "🙂"

        with st.chat_message(
            message["role"],
            avatar=avatar
        ):

            st.markdown(message["content"])

            if message["role"] == "assistant":

                c1, c2, c3 = st.columns([1, 1, 12])

                with c1:

                    if st.button(
                        "🔊",
                        key=f"listen_{index}"
                    ):

                        with st.spinner("Generating audio..."):

                            audio_path = voice_service.generate_audio(
                                message["content"]
                            )

                        with open(audio_path, "rb") as audio:

                            st.audio(
                                audio.read(),
                                format="audio/mp3"
                            )

                with c2:

                    if st.button(
                        "📋",
                        key=f"copy_{index}"
                    ):

                        st.toast(
                            "Copy feature coming soon."
                        )