import streamlit as st


def render_report_summary(data):

    st.subheader("📋 AI Report Summary")

    summary = data.get(
        "summary",
        "No summary available."
    )

    with st.container(border=True):

        st.write(summary)