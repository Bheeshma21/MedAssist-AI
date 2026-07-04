import sys
import os



# ==========================================
# Add Project Root to Python Path
# ==========================================

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)

import streamlit as st

# ==========================================
# Load CSS
# ==========================================

css_path = os.path.join(
    os.path.dirname(__file__),
    "assets",
    "style.css"
)

if os.path.exists(css_path):

    with open(css_path, encoding="utf-8") as f:

        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

# ==========================================
# Imports
# ==========================================

from memory.session_memory import session_memory
from frontend.components.theme import load_theme

from frontend.views.welcome import render_welcome
from frontend.views.login import render_login
from frontend.views.register import render_register
from frontend.views.dashboard import render_dashboard

# ==========================================
# Page Config
# ==========================================

st.set_page_config(

    page_title="MedAssist AI",

    page_icon="🏥",

    layout="wide"

)

# ==========================================
# Load Theme
# ==========================================

session_memory.initialize()

load_theme()

# ==========================================
# Initialize Session State
# ==========================================

defaults = {

    "page": "welcome",

    "logged_in": False,

    "chat_mode": "patient"

}

for key, value in defaults.items():

    if key not in st.session_state:

        st.session_state[key] = value

# ==========================================
# Routing
# ==========================================

if st.session_state.logged_in:

    render_dashboard()

else:

    if st.session_state.page == "welcome":

        render_welcome()

    elif st.session_state.page == "login":

        render_login()

    elif st.session_state.page == "register":

        render_register()

    else:

        render_welcome()