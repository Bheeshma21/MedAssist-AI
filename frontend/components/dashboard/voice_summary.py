import streamlit as st

from services.voice_service import voice_service


def render_voice_summary(data):

    st.subheader("🔊 Listen to Report Summary")

    summary = data.get("summary", "")

    if not summary:

        return

    if st.button(
        "🔊 Generate Voice Summary",
        use_container_width=True
    ):

        audio_path = voice_service.generate_audio(
            summary
        )

        with open(audio_path, "rb") as audio:

            st.audio(
                audio.read(),
                format="audio/mp3"
            )