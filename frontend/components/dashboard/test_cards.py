import streamlit as st


def render_test_cards(data):

    tests = data.get("tests", [])

    st.subheader("🧪 Laboratory Test Results")

    if not tests:

        st.info("No laboratory test results found.")
        return

    for test in tests:

        status = str(test.get("status", "Normal")).lower()

        if status == "normal":
            icon = "🟢"
        elif status == "high":
            icon = "🟠"
        elif status == "low":
            icon = "🔴"
        else:
            icon = "⚪"

        with st.container(border=True):

            col1, col2 = st.columns([3, 1])

            with col1:

                st.markdown(f"### {icon} {test.get('name', 'Unknown Test')}")

                st.write(
                    f"**Value:** {test.get('value', '-')}"
                )

                st.write(
                    f"**Normal Range:** {test.get('normal_range', '-')}"
                )

            with col2:

                st.metric(
                    "Status",
                    test.get("status", "-")
                )

                severity = test.get("severity", "")

                if severity:
                    st.caption(
                        f"Severity: {severity}"
                    )

            explanation = test.get("explanation", "")

            if explanation:
                st.info(explanation)