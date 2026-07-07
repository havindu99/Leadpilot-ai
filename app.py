import streamlit as st
from services.database_service import init_database
from config.settings import APP_NAME, APP_ICON
from components.sidebar import render_sidebar

from app_pages.Dashboard import render_dashboard
from app_pages.Message_Analyzer import render_MessageAnalyzer
from app_pages.History import render_history
from app_pages.Analytics import render_analytics
from app_pages.Reports import render_reports
from app_pages.Settings import render_settings


def load_css():
    with open("styles/style.css", "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def main():
    st.set_page_config(
        page_title=APP_NAME,
        page_icon=APP_ICON,
        layout="wide",
        initial_sidebar_state="expanded",
    )
    init_database()

    load_css()

    selected_page = render_sidebar()

    if selected_page == "Dashboard":
        render_dashboard()
    elif selected_page == "Message Analyzer":
        render_MessageAnalyzer()
    elif selected_page == "History":
        render_history()
    elif selected_page == "Analytics":
        render_analytics()
    elif selected_page == "Reports":
        render_reports()
    elif selected_page == "Settings":
        render_settings()


if __name__ == "__main__":
    main()