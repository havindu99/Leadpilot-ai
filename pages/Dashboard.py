import streamlit as st
import pandas as pd
import plotly.express as px

from services.database_service import (
    get_dashboard_stats,
    get_category_distribution,
    get_priority_distribution,
    get_recent_leads,
)


def render_dashboard():
    stats = get_dashboard_stats()
    category_data = get_category_distribution()
    priority_data = get_priority_distribution()
    recent_data = get_recent_leads(limit=10)

    st.markdown("""
    <div class="hero">
        <h1>LeadPilot AI</h1>
        <p>Smarter Lead Management. Faster Decisions.</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown(f"""
        <div class="metric-card">
            <h3>📩 Total Messages</h3>
            <h2>{stats["total_messages"]}</h2>
            <p>All incoming messages</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="metric-card danger">
            <h3>🔥 High Priority</h3>
            <h2>{stats["high_priority"]}</h2>
            <p>Needs human attention</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <div class="metric-card success">
            <h3>⭐ Qualified Leads</h3>
            <h2>{stats["qualified_leads"]}</h2>
            <p>Ready for sales follow-up</p>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown(f"""
        <div class="metric-card warning">
            <h3>🚫 Spam</h3>
            <h2>{stats["spam_messages"]}</h2>
            <p>Filtered low-quality messages</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("### 📊 Lead Overview")

    chart_col1, chart_col2 = st.columns(2)

    with chart_col1:
        if category_data.empty:
            st.info("No category data yet. Analyze your first message to see this chart.")
        else:
            fig = px.pie(
                category_data,
                names="Category",
                values="Count",
                title="Messages by Category"
            )
            st.plotly_chart(fig, width="stretch")

    with chart_col2:
        if priority_data.empty:
            st.info("No priority data yet. Analyze your first message to see this chart.")
        else:
            fig = px.bar(
                priority_data,
                x="Priority",
                y="Count",
                title="Priority Distribution"
            )
            st.plotly_chart(fig, width="stretch")

    st.markdown("### 📜 Recent Activity")

    if recent_data.empty:
        st.info("No recent leads yet. Go to Message Analyzer and analyze a customer message.")
    else:
        st.dataframe(recent_data, width="stretch")