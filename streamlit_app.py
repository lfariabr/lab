
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

graphics_leads = st.Page(
    "views/graphics.py",
    title="graphics",
    icon="📈",
)

graphics_sales = st.Page(
    "views/graphics_sales.py",
    title="graphics_sales",
    icon="💸",
)

forca = st.Page(
    "views/forca.py",
    title="forca",
    icon="🎮",
)

# NAVIGATION SETUP
pg = st.navigation(
    {
        "numbers": [currency_converter, calculator],
        "pro-corpo reports": [graphics_leads, graphics_sales],
        "games": [forca]
    }
)

pg.run()
