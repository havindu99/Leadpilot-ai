import streamlit as st

from services.database_service import (
    get_dashboard_stats,
    get_category_distribution,
    get_priority_distribution,
    get_recent_leads,
)


def render_reports():
    st.title("📄 Reports")

    stats = get_dashboard_stats()
    categories = get_category_distribution()
    priorities = get_priority_distribution()
    recent = get_recent_leads(100)

    st.subheader("📊 Summary")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Messages", stats["total_messages"])
    col2.metric("High Priority", stats["high_priority"])
    col3.metric("Qualified Leads", stats["qualified_leads"])
    col4.metric("Spam", stats["spam_messages"])

    st.subheader("📂 Category Summary")
    st.dataframe(categories, use_container_width=True)

    st.subheader("🔥 Priority Summary")
    st.dataframe(priorities, use_container_width=True)

    st.subheader("📜 Recent Leads")
    st.dataframe(recent, use_container_width=True)

    st.download_button(
        "📥 Download Recent Leads CSV",
        data=recent.to_csv(index=False),
        file_name="leadpilot_report.csv",
        mime="text/csv"
    )