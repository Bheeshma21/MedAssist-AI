import streamlit as st


def render_recommendations(data):

    recommendations = data.get(
        "recommendations",
        []
    )

    st.subheader("🍎 AI Recommendations")

    if not recommendations:

        st.info("No recommendations available.")

        return

    for index, recommendation in enumerate(
        recommendations,
        start=1
    ):

        st.success(
            f"{index}. {recommendation}"
        )