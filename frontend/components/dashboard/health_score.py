import streamlit as st


def render_health_score(data):

    score = data.get("health_score", 0)
    risk = data.get("risk_level", "Unknown")

    if score >= 80:
        color = "🟢"
        status = "Excellent"

    elif score >= 60:
        color = "🟡"
        status = "Moderate"

    else:
        color = "🔴"
        status = "Needs Attention"

    st.subheader("🏥 Overall Health")

    c1, c2, c3 = st.columns(3)

    with c1:

        st.metric(
            "Health Score",
            f"{score}/100"
        )

    with c2:

        st.metric(
            "Risk Level",
            risk
        )

    with c3:

        st.metric(
            "Overall Status",
            f"{color} {status}"
        )

    st.progress(score / 100)