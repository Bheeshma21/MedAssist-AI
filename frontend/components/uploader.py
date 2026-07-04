import streamlit as st


def render_uploader():

    uploaded_file = st.file_uploader(
        "Upload Medical File",
        type=[
            "pdf",
            "png",
            "jpg",
            "jpeg",
            "bmp",
            "webp"
        ],
        accept_multiple_files=False,
        label_visibility="collapsed"
    )

    return uploaded_file