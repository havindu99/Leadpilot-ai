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

    # Pie Chart
    if category_data.empty:
        st.info("No category data available.")
    else:
        fig = px.pie(
            category_data,
            names="Category",
            values="Count",
            title="Lead Categories"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    # Bar Chart
    st.subheader("🔥 Priority Distribution")

    if priority_data.empty:
        st.info("No priority data available.")
    else:
        fig = px.bar(
            priority_data,
            x="Priority",
            y="Count",
            title="Lead Priority Distribution"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )