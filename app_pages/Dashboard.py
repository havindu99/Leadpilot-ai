from datetime import datetime

import streamlit as st
import pandas as pd
import plotly.express as px

from services.database_service import (
    get_dashboard_stats,
    get_category_distribution,
    get_priority_distribution,
    get_recent_leads,
)

# NOTE: visual theme (hero, metric-card, sidebar nav, chart container, etc.)
# lives centrally in theme.css, loaded once at app start-up.
# This file only supplies HTML structure + data, not colors.

_PRIORITY_BADGE = {
    "High":   ("#F87171", "rgba(239, 68, 68, 0.16)"),
    "Medium": ("#FBBF24", "rgba(245, 158, 11, 0.16)"),
    "Low":    ("#34D399", "rgba(16, 185, 129, 0.16)"),
}

_SENTIMENT_BADGE = {
    "Positive": ("#34D399", "rgba(16, 185, 129, 0.16)"),
    "Neutral":  ("#94A3B8", "rgba(148, 163, 184, 0.16)"),
    "Negative": ("#F87171", "rgba(239, 68, 68, 0.16)"),
}


def _badge_html(value: str, palette: dict) -> str:
    color, bg = palette.get(value, ("#94A3B8", "rgba(148, 163, 184, 0.16)"))
    return (
        f'<span style="background:{bg}; color:{color}; padding:3px 10px; '
        f'border-radius:999px; font-size:12.5px; font-weight:700; '
        f'white-space:nowrap;">{value}</span>'
    )


# ---------------------------------------------------------------------------
# Sections
# ---------------------------------------------------------------------------
def _render_hero():
    st.markdown("""
    <div class="hero">
        <h1>LeadPilot AI</h1>
        <p>Smarter Lead Management. Faster Decisions.</p>
    </div>
    """, unsafe_allow_html=True)


def _metric_card(col, icon: str, title: str, value, subtitle: str, variant: str = ""):
    with col:
        st.markdown(f"""
        <div class="metric-card {variant}">
            <h3><span>{icon}</span> {title}</h3>
            <h2>{value}</h2>
            <p>{subtitle}</p>
        </div>
        """, unsafe_allow_html=True)


def _render_metrics(stats: dict):
    col1, col2, col3, col4 = st.columns(4)

    _metric_card(col1, "📩", "Total Messages", stats.get("total_messages", 0),
                 "All incoming messages")
    _metric_card(col2, "🔥", "High Priority", stats.get("high_priority", 0),
                 "Needs human attention", variant="danger")
    _metric_card(col3, "⭐", "Qualified Leads", stats.get("qualified_leads", 0),
                 "Ready for sales follow-up", variant="success")
    _metric_card(col4, "🚫", "Spam", stats.get("spam_messages", 0),
                 "Filtered low-quality messages", variant="warning")


def _section_header(icon: str, title: str, count=None):
    badge = (
        f'<span style="margin-left:10px; background:rgba(99,102,241,0.18); '
        f'color:#A5B4FC; padding:2px 10px; border-radius:999px; font-size:13px; '
        f'font-weight:700;">{count}</span>'
        if count is not None else ""
    )
    st.markdown(
        f'<h3 style="display:flex; align-items:center;">{icon} {title}{badge}</h3>',
        unsafe_allow_html=True,
    )


def _render_charts(category_data: pd.DataFrame, priority_data: pd.DataFrame):
    total = int(category_data["Count"].sum()) if not category_data.empty else None
    _section_header("📊", "Lead Overview", total)

    chart_col1, chart_col2 = st.columns(2)

    # Shared dark-mode chart theme so plots match the rest of the app
    dark_theme = dict(
        template="plotly_dark",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        margin=dict(t=50, b=20, l=20, r=20),
        font=dict(family="Inter, Arial, sans-serif", size=13, color="#E2E8F0"),
        legend=dict(bgcolor="rgba(0,0,0,0)"),
    )

    palette = ["#6366F1", "#38BDF8", "#F472B6", "#F87171", "#34D399", "#FBBF24"]

    with chart_col1:
        if category_data.empty:
            st.info("No category data yet. Analyze your first message to see this chart.")
        else:
            fig = px.pie(
                category_data,
                names="Category",
                values="Count",
                title="Messages by Category",
                hole=0.55,
                color_discrete_sequence=palette,
            )
            fig.update_traces(
                textposition="inside",
                textinfo="percent",
                marker=dict(line=dict(color="#0F172A", width=2)),
            )
            fig.update_layout(**dark_theme, showlegend=True)
            st.plotly_chart(fig, width="stretch")

    with chart_col2:
        if priority_data.empty:
            st.info("No priority data yet. Analyze your first message to see this chart.")
        else:
            fig = px.bar(
                priority_data,
                x="Priority",
                y="Count",
                title="Priority Distribution",
                color="Priority",
                text="Count",
                color_discrete_map={
                    "High": "#F87171",
                    "Medium": "#FBBF24",
                    "Low": "#34D399",
                },
            )
            fig.update_traces(textposition="outside", marker=dict(cornerradius=6))
            fig.update_layout(**dark_theme, showlegend=False)
            fig.update_xaxes(showgrid=False)
            fig.update_yaxes(showgrid=True, gridcolor="rgba(148,163,184,0.12)")
            st.plotly_chart(fig, width="stretch")


def _render_recent_activity(recent_data: pd.DataFrame):
    _section_header("📜", "Recent Activity", len(recent_data) if not recent_data.empty else None)

    if recent_data.empty:
        st.info("No recent leads yet. Go to Message Analyzer and analyze a customer message.")
        return

    display_df = recent_data.copy()

    # Render priority / sentiment as colored pill badges instead of plain text
    if "priority" in display_df.columns:
        display_df["priority"] = display_df["priority"].apply(
            lambda v: _badge_html(v, _PRIORITY_BADGE)
        )
    if "sentiment" in display_df.columns:
        display_df["sentiment"] = display_df["sentiment"].apply(
            lambda v: _badge_html(v, _SENTIMENT_BADGE)
        )
    if "lead_score" in display_df.columns:
        display_df["lead_score"] = display_df["lead_score"].apply(
            lambda v: f'<strong>{v}</strong>'
        )

    table_html = display_df.to_html(escape=False, index=False, border=0)
    st.markdown(
        f'<div class="pro-table">{table_html}</div>',
        unsafe_allow_html=True,
    )


def _render_footer():
    st.markdown(
        f'<p style="text-align:right; color:#64748B; font-size:12.5px; margin-top:0.5rem;">'
        f'Last updated: {datetime.now().strftime("%Y-%m-%d %H:%M")}</p>',
        unsafe_allow_html=True,
    )


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------
def render_dashboard():
    try:
        stats = get_dashboard_stats()
        category_data = get_category_distribution()
        priority_data = get_priority_distribution()
        recent_data = get_recent_leads(limit=10)
    except Exception as e:
        st.error(f"Dashboard data load කරන්න බැරි වුනා: {e}")
        return

    _render_hero()
    _render_metrics(stats)
    st.markdown("<div style='height: 0.8rem'></div>", unsafe_allow_html=True)
    _render_charts(category_data, priority_data)
    st.markdown("<div style='height: 0.8rem'></div>", unsafe_allow_html=True)
    _render_recent_activity(recent_data)
    _render_footer()