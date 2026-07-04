import streamlit as st


def render_risk(result):

    risk = result["risk_report"]

    if risk["risk_level"] == "HIGH":
        st.error(f"🚨 {risk['risk_level']} Risk")

    elif risk["risk_level"] == "MEDIUM":
        st.warning(f"⚠ {risk['risk_level']} Risk")

    else:
        st.success(f"✅ {risk['risk_level']} Risk")

    st.write("### Reasons")

    for reason in risk["reasons"]:
        st.write(f"• {reason}")