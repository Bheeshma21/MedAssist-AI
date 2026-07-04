import streamlit as st

from .health_score import render_health_score
from .body_systems import render_body_systems
from .patient_card import render_patient_card
from .report_summary import render_report_summary
from .test_cards import render_test_cards
from .charts import render_charts
from .conditions import render_conditions
from .recommendations import render_recommendations
from .voice_summary import render_voice_summary
from .health_timeline import render_health_timeline


def render_dashboard(data):

    if not data:
        return

    st.header("🏥 AI Health Dashboard")

    # -----------------------------------------
    # Overall Health
    # -----------------------------------------

    render_health_score(data)

    st.divider()

    # -----------------------------------------
    # Body Systems
    # -----------------------------------------

    render_body_systems(data)

    st.divider()

    # -----------------------------------------
    # Patient Details
    # -----------------------------------------

    render_patient_card(data)

    st.divider()

    # -----------------------------------------
    # AI Summary
    # -----------------------------------------

    render_report_summary(data)

    st.divider()

    # -----------------------------------------
    # Laboratory Tests
    # -----------------------------------------

    render_test_cards(data)

    st.divider()

    # -----------------------------------------
    # Charts
    # -----------------------------------------

    render_charts(data)

    st.divider()

    # -----------------------------------------
    # Possible Conditions
    # -----------------------------------------

    render_conditions(data)

    st.divider()

    # -----------------------------------------
    # Recommendations
    # -----------------------------------------

    render_recommendations(data)

    st.divider()

    # -----------------------------------------
    # Voice Summary
    # -----------------------------------------

    render_voice_summary(data)
    st.divider()
    
    render_health_timeline(
    st.session_state.user_id
)