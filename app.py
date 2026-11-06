import streamlit as st
from agent import run_agent

st.set_page_config(page_title="Omni Deal Intelligence", layout="wide")
st.title("💼 Enterprise Deal Intelligence Agent (Hindsight Powered)")

col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("Interactive Sales Agent Chat")
    user_query = st.text_input("Enter client dialogue / deal objection:")
    if st.button("Send Input") and user_query:
        with st.spinner("Querying Hindsight memory and Groq LLM..."):
            result = run_agent(user_query)
            st.session_state["last_result"] = result
            st.success("Interaction logged to memory!")

        if "last_result" in st.session_state:
            st.write("**Agent Response:**")
            st.write(st.session_state["last_result"]["response"])

with col2:
    st.subheader("🧠 Live Hindsight Memory Bank")
    if "last_result" in st.session_state:
        st.info("**Recalled Context:**")
        st.code(st.session_state["last_result"]["recalled_context"])
    else:
        st.caption("Recalled memory context will display here after submitting input.")