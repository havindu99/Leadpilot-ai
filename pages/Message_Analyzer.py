import streamlit as st
from services.ai_service import analyze_message
from services.database_service import save_lead


def render_MessageAnalyzer():

    st.title("🤖 AI Message Analyzer")
    st.write("Analyze customer messages using Gemini AI.")

    source = st.selectbox(
        "Message Source",
        ["WhatsApp", "Facebook", "Instagram", "Email", "Website"]
    )

    message = st.text_area(
        "Customer Message",
        height=200,
        placeholder="Type the customer's message here..."
    )

    if st.button("🚀 Analyze"):

        if message.strip() == "":
            st.warning("Please enter a customer message.")

        else:
            with st.spinner("Analyzing..."):
                result = analyze_message(message)

            result["source"] = source
            result["message"] = message

            st.session_state["latest_result"] = result

    if "latest_result" in st.session_state:

        result = st.session_state["latest_result"]

        st.success("Analysis Completed!")

        st.subheader("📊 AI Analysis")
        st.write(f"**Category:** {result['category']}")
        st.write(f"**Priority:** {result['priority']}")
        st.write(f"**Lead Score:** {result['lead_score']}")
        st.write(f"**Sentiment:** {result['sentiment']}")
        st.write(f"**Urgency:** {result['urgency']}")

        st.subheader("💬 Suggested Reply")
        st.info(result["suggested_reply"])

        st.subheader("➡️ Next Action")
        st.success(result["next_action"])

        st.subheader("📝 Reason")
        st.write(result["reason"])

        if st.button("💾 Save Lead"):
            try:
                save_lead(result)
                st.success("✅ Lead saved successfully!")
            except Exception as e:
                st.error(e)