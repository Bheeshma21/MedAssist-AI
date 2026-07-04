import streamlit as st
import time


def thinking():

    placeholder = st.empty()

    messages = [
        "🧠 Understanding your request...",
        "📚 Searching trusted medical knowledge...",
        "🩺 Performing clinical reasoning...",
        "💊 Checking medication safety...",
        "📄 Preparing your response..."
    ]

    for message in messages:
        placeholder.info(message)
        time.sleep(0.5)

    placeholder.success("✅ Analysis completed")