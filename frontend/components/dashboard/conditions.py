import streamlit as st


def render_conditions(data):

    conditions = data.get("possible_conditions", [])

    st.subheader("🩺 Possible Medical Conditions")

    if not conditions:

        st.success("✅ No major conditions detected.")

        return

    for condition in conditions:

        st.warning(
            f"⚠️ {condition}"
        )