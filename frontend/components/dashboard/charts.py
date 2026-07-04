import streamlit as st
import pandas as pd


def render_charts(data):

    tests = data.get("tests", [])

    if not tests:
        return

    rows = []

    for test in tests:

        value = test.get("value", "")

        try:

            value = float(
                str(value).split()[0]
            )

        except Exception:

            continue

        rows.append({

            "Test": test.get("name"),

            "Value": value

        })

    if not rows:
        return

    st.subheader("📊 Laboratory Test Overview")

    df = pd.DataFrame(rows)

    st.bar_chart(
        df.set_index("Test")
    )

    with st.expander("View Test Data"):

        st.dataframe(
            df,
            use_container_width=True
        )