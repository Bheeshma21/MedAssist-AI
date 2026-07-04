import streamlit as st
import pandas as pd

from database.health_timeline import health_timeline


def render_health_timeline(user_id):

    reports = health_timeline.get_reports(user_id)

    st.subheader("📈 Health Timeline")

    if not reports:

        st.info("No previous health reports found.")

        return

    timeline = []

    for report in reports:

        timeline.append({
            "Date": report[7],
            "Report": report[2],
            "Health Score": report[4],
            "Risk": report[5]
        })

    df = pd.DataFrame(timeline)

    st.dataframe(
        df,
        use_container_width=True
    )

    st.subheader("📊 Health Score Trend")

    chart_df = df[["Date", "Health Score"]].copy()

    chart_df["Date"] = pd.to_datetime(chart_df["Date"])

    chart_df = chart_df.set_index("Date")

    st.line_chart(chart_df)