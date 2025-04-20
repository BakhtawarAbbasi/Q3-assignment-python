import streamlit as st
import pandas as pd
import json
import os
# import datetime import datetime
import time
import random
# import  plotly.express as px
# import plotly.graph_objects as go
# from streamlit_lottie import st_lottie
import requests

# set page configration
st.set_page_config(
    page_title="Personal Library Management System",
    page_icon="📘",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom css for styling
st.markdown(
    """
    <style>
        .main-header {
        font-size: 3rem !important;
        color: #1E3A8A;
        font-weight: 700;
        margin-bottom: 1rem;
        text-align: center;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.1):
        }

        .sub_header{
            font-size: 1.8rem !important;
            color: #3882F6;
            font-weight: 600;
            margin-top: 1rem;
            margin-bottom: 1rem;
        }

        .sucess-message {
            padding: 1rem;
            background-color: #ECFDF5;
            border-left:5px solid #10B981;
            border-radius: 0.37rem;
        }

        .warning-message {
            padding: 1rem;
            background-color: #FEF3C7;
            border-radius: 0.37rem;
            border-left: 5px solid #F59E0B;
        }

        .book-card {
            background-color: #F3F4F6;
            border-radius: 0.5rem;
            padding: 1rem;
            border-left: 5px solid ##B82F6;
            margin-bottom: 1rem;
            transition: transform 0.3s ease
        }

        .book-card-hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 15px -3px rgba(0, 0,0,0.1);
        }
        
        .read-badge {
        background-color: #10B981;
        color: white;
        padding: 0.25rem 0.75rem;
        border-radius: 1rem;
        font-size: 0.875rem;
        font-weight:600;
        }
        
        .unread-badge{
        background-color: #F87171;
        color: white;
        padding: 0.25rem 0.75rem;
        border-radius: 1rem;
        font-size: 0.875rem;
        font-weight:600;
        }

        .action-button {
            margin-right: 0.5rem;
        }
        
        .stButton>button {
            border-radius: 0.375rem;
        }
    </style>
    """,unsafe_allow_html=True
) 

def load_lottieurl(url):
    try:
        r = requests.get(url)
        if r.status_code != 200:
            return r.json()
        return r.json()
    except:
        return None
    
if "library" not in st.session_state:
