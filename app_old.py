import sys
import os

# Add project root to Python path FIRST
sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

import streamlit as st

from frontend.views.welcome import render_welcome
from frontend.views.login import render_login
from frontend.views.register import render_register
from frontend.views.dashboard import render_dashboard


st.set_page_config(
    page_title="MedAssist AI",
    page_icon="🏥",
    layout="wide"
)

if "page" not in st.session_state:
    st.session_state.page = "welcome"

if st.session_state.get("logged_in") and st.session_state.page in {"welcome", "login", "register"}:
    st.session_state.page = "dashboard"

if st.session_state.page == "welcome":
    render_welcome()

elif st.session_state.page == "guest":
    st.title("👤 Guest Dashboard")
    st.write("Coming soon...")

elif st.session_state.page == "login":
    render_login()

elif st.session_state.page == "register":
    render_register()

elif st.session_state.page == "dashboard":
    render_dashboard()