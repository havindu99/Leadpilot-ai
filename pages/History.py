import streamlit as st
from services.database_service import get_all_leads, delete_lead


def render_history():

    st.title("📜 Lead History")

    search = st.text_input(
        "🔍 Search Leads",
        placeholder="Search by source, category or priority..."
    )

    priority_filter = st.selectbox(
        "Priority Filter",
        ["All", "High", "Medium", "Low"]
    )

    df = get_all_leads()

    # Search
    if search:
        df = df[
            df.astype(str)
            .apply(lambda row: row.str.contains(search, case=False).any(), axis=1)
        ]

    # Priority Filter
    if priority_filter != "All":
        df = df[df["priority"] == priority_filter]

    # Display
    if df.empty:
        st.info("No leads found.")
    else:
        st.dataframe(
            df,
            use_container_width=True
        )

        st.download_button(
            "📥 Download CSV",
            data=df.to_csv(index=False),
            file_name="lead_history.csv",
            mime="text/csv"
        )

        df = get_all_leads()

# search/filter code 

    if df.empty:
     st.info("No leads found.")

    else:
     st.dataframe(df, use_container_width=True)

    st.divider()

    st.subheader("🗑 Delete Lead")

    lead_id = st.selectbox("Select Lead ID", df["id"])

    if st.button("Delete Selected Lead"):
        delete_lead(lead_id)
        st.success("Lead deleted successfully!")
        st.rerun()