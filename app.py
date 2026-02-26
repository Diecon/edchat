import streamlit as st
import cohere

st.set_page_config(page_title="CSE Engineering Doubt Solver")

st.title("🎓 CSE Engineering AI Doubt Solver")

api_key = st.text_input("Enter your Cohere API Key:", type="password")
question = st.text_area("Enter your CSE question:")

if st.button("Solve") and question and api_key:
    co = cohere.Client(api_key)

    response = co.chat(
        model="command-r",
        message=f"You are an expert CSE professor. Explain step-by-step with examples and code where needed.\n\nQuestion: {question}"
    )

    st.markdown("### 📘 Explanation")
    st.write(response.text)
