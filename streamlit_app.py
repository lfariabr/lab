
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
    "views/calculator.py",
    title="calculator",
    icon="🧮",
    layout="centered",
    initial_sidebar_state="auto"
)

currency_converter = st.Page(
    "views/currency_converter.py",
    title="currency_converter",
    icon="💰",
    layout="centered",
    initial_sidebar_state="auto"
)

graphics = st.Page(
    "views/graphics.py",
    title="graphics",
    icon="📈",
    layout="centered",
    initial_sidebar_state="auto"
)

forca = st.Page(
    "views/forca.py",
    title="forca",
    icon="🎮",
    layout="centered",
    initial_sidebar_state="auto"
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
