
import os
import shutil
import subprocess
import pandas as pd
import os
import requests
import json
import streamlit as st
import pandas as pd
import plotly.express as px

# PAGE SETUP

calculator = st.Page(
    title="calculator",
    page_icon="🧮",
    layout="centered",
    initial_sidebar_state="auto",
    "views/calculator.py"
)

currency_converter = st.Page(
    title="currency_converter",
    page_icon="💰",
    layout="centered",
    initial_sidebar_state="auto",
    "views/currency_converter.py"
)

graphics = st.Page(
    title="graphics",
    page_icon="📈",
    layout="centered",
    initial_sidebar_state="auto",
    "views/graphics.py"
)

forca = st.Page(
    title="forca",
    page_icon="🎮",
    layout="centered",
    initial_sidebar_state="auto",
    "views/forca.py"
)

# NAVIGATION SETUP
pg = st.navigation(
    {
        "calculator": [calculator],
        "currency_converter": [currency_converter],
        "graphics": [graphics],
        "forca": [forca]
    }
)

pg.run()
