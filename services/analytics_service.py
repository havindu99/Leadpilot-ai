import streamlit as st
import plotly.express as px

from services.database_service import (
    get_category_distribution,
    get_priority_distribution
)

def render_analytics():

    st.title("📊 Analytics")

    category_data = get_category_distribution()
    priority_data = get_priority_distribution()