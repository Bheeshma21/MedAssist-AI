import streamlit as st


def render_uploader():

    uploaded = st.file_uploader(
        "Attach a medical file",
        type=[
            "pdf",
            "png",
            "jpg",
            "jpeg",
            "mp3",
            "wav",
            "mp4",
            "avi",
            "mov"
        ]
    )

    return uploaded