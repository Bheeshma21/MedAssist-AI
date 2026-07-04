import streamlit as st


def render_body_systems(data):

    systems = data.get("body_systems", [])

    st.subheader("🩺 Body Systems Analysis")

    if not systems:

        st.info("No body system analysis available.")

        return

    cols = st.columns(2)

    for index, system in enumerate(systems):

        icon = system.get("icon", "🩺")
        name = system.get("name", "Unknown")
        status = system.get("status", "Unknown")
        reason = system.get("reason", "")

        if status.lower() == "normal":
            color = "🟢"

        elif status.lower() == "warning":
            color = "🟡"

        elif status.lower() == "critical":
            color = "🔴"

        else:
            color = "⚪"

        with cols[index % 2]:

            with st.container(border=True):

                st.markdown(f"### {icon} {name}")

                st.write(f"**Status:** {color} {status}")

                if reason:
                    st.caption(reason)