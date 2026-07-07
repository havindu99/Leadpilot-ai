import streamlit as st
from services.database_service import (
    clear_database,
    get_dashboard_stats
)


def render_settings():

    st.title("⚙️ Settings")
    st.write("Manage your application settings and system information.")

    stats = get_dashboard_stats()

    # ---------------- Database ---------------- #

    st.subheader("🗄 Database Management")

    st.warning(
        "⚠️ Clearing the database will permanently delete all stored leads. "
        "This action cannot be undone."
    )

    if st.button("🗑 Clear All Leads", use_container_width=True):

        clear_database()

        st.success("✅ Database cleared successfully!")

        st.rerun()

    st.divider()

    # ---------------- System Information ---------------- #

    st.subheader("💻 System Information")

    col1, col2 = st.columns(2)

    with col1:

        st.info(f"""
**Application**

LeadPilot AI

**Version**

1.0.0

**Framework**

Streamlit
""")

    with col2:

        st.info(f"""
**Programming Language**

Python

**Database**

SQLite

**AI Model**

Google Gemini 2.5 Flash
""")

    st.divider()

    # ---------------- Statistics ---------------- #

    st.subheader("📊 Current Statistics")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "📩 Messages",
        stats["total_messages"]
    )

    c2.metric(
        "🔥 High Priority",
        stats["high_priority"]
    )

    c3.metric(
        "⭐ Qualified",
        stats["qualified_leads"]
    )

    c4.metric(
        "🚫 Spam",
        stats["spam_messages"]
    )

    st.divider()

    # ---------------- About ---------------- #

    st.subheader("ℹ About")

    st.markdown("""
### LeadPilot AI

LeadPilot AI is an AI-powered Lead & Message Triage Platform designed to
help businesses analyze customer inquiries, classify leads, prioritize
important conversations, and generate intelligent replies using
Google Gemini AI.

---

**Developer**

Havindu Hesara Perera

**Technologies**

Python • Streamlit • Gemini AI • SQLite • Plotly

**License**

Educational Project

© 2026 LeadPilot AI
""")