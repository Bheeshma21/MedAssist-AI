import streamlit as st


def render_credit_card(remaining=10):

    st.info(
        f"⭐ AI Credits Remaining: {remaining}/10"
    )

    st.progress(remaining / 10)