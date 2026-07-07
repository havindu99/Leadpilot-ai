import streamlit as st
from services.database_service import clear_database


def render_settings():

    st.title("⚙️ Settings")

    st.subheader("Database")

    if st.button("🗑️ Clear All Leads"):
        clear_database()
        st.success("Database cleared successfully!")

    st.divider()

    st.subheader("About")

    st.write("LeadPilot AI")
    st.write("Version 1.0.0")
    st.write("Powered by Gemini AI")