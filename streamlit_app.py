
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
)

currency_converter = st.Page(
    "views/currency_converter.py",
    title="currency_converter",
    icon="💰",
)

graphics = st.Page(
    "views/graphics.py",
    title="graphics",
    icon="📈",
)

forca = st.Page(
    "views/forca.py",
    title="forca",
    icon="🎮",
)

# NAVIGATION SETUP
pg = st.navigation(
    {
        "menu": [calculator, currency_converter],
        "pro-corpo": [graphics],
        "others": [forca]
    }
)

pg.run()
