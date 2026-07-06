import streamlit as st

from config.settings import (
    APP_NAME,
    APP_ICON,
    APP_TAGLINE,
    NAVIGATION_ITEMS,
)


def render_sidebar():
    with st.sidebar:
        st.markdown(f"# {APP_ICON} {APP_NAME}")
        st.caption(APP_TAGLINE)

        st.markdown("---")

        selected_page = st.radio(
            "Navigation",
            NAVIGATION_ITEMS
        )

        st.markdown("---")
        st.caption("Version 1.0.0")

    return selected_page