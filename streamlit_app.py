
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

# Configuração da página
calculadora = st.Page(
    "view/calculadora.py",
    title="calculadora",
    icon="🧮",
)

# Configuração da navegação
pg = st.navigation(
    {
        "parte1": [calculadora],
    }
)
