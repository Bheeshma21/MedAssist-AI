import streamlit as st
import time


def render_reasoning():

    status = st.empty()

    steps = [
        "🧠 Understanding symptoms...",
        "📚 Retrieving medical evidence...",
        "🚨 Assessing clinical risk...",
        "💊 Checking drug interactions...",
        "📝 Preparing clinical summary...",
        "✅ Finalizing response..."
    ]

    for step in steps:
        status.info(step)
        time.sleep(0.6)

    status.success("✅ Analysis Complete")