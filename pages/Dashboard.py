import streamlit as st
import pandas as pd
import plotly.express as px


def render_dashboard():
    st.markdown("""
    <div class="hero">
        <h1>LeadPilot AI</h1>
        <p>Smarter Lead Management. Faster Decisions.</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown("""
        <div class="metric-card">
            <h3>📩 Total Messages</h3>
            <h2>128</h2>
            <p>All incoming messages</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="metric-card danger">
            <h3>🔥 High Priority</h3>
            <h2>24</h2>
            <p>Needs human attention</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="metric-card success">
            <h3>⭐ Qualified Leads</h3>
            <h2>41</h2>
            <p>Ready for sales follow-up</p>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
        <div class="metric-card warning">
            <h3>🚫 Spam</h3>
            <h2>14</h2>
            <p>Filtered low-quality messages</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("### 📊 Lead Overview")

    category_data = pd.DataFrame({
        "Category": ["Sales Lead", "Support", "Complaint", "Spam", "General"],
        "Count": [38, 21, 9, 14, 18]
    })

    priority_data = pd.DataFrame({
        "Priority": ["High", "Medium", "Low"],
        "Count": [24, 46, 30]
    })

    chart_col1, chart_col2 = st.columns(2)

    with chart_col1:
        fig = px.pie(
            category_data,
            names="Category",
            values="Count",
            title="Messages by Category"
        )
        st.plotly_chart(fig, use_container_width=True)

    with chart_col2:
        fig = px.bar(
            priority_data,
            x="Priority",
            y="Count",
            title="Priority Distribution"
        )
        st.plotly_chart(fig, use_container_width=True)

    st.markdown("### 📜 Recent Activity")

    recent_data = pd.DataFrame({
        "Source": ["WhatsApp", "Instagram", "Email", "Website"],
        "Message Type": ["Sales Lead", "Complaint", "Support", "Spam"],
        "Priority": ["High", "High", "Medium", "Low"],
        "Lead Score": [94, 78, 55, 12]
    })

    st.dataframe(recent_data, use_container_width=True)