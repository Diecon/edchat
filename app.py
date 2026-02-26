import streamlit as st
import cohere

st.set_page_config(page_title="CSE Engineering Doubt Solver")

st.title("🎓 CSE Engineering AI Doubt Solver")

st.write("Ask any Computer Science Engineering question.")

# Input fields
api_key = st.text_input("Enter your Cohere API Key:", type="password")
question = st.text_area("Enter your CSE question:")

if st.button("Solve"):

    if not api_key:
        st.error("Please enter your Cohere API key.")
    elif not question:
        st.error("Please enter a question.")
    else:
        try:
            co = cohere.Client(api_key)

            response = co.chat(
                model="command",   # Trial-safe model
                message=f"""
You are an expert Computer Science Engineering professor.
Answer only CSE-related questions.
Explain clearly step-by-step.
Include examples and code where necessary.

Question:
{question}
"""
            )

            st.markdown("### 📘 Explanation")
            st.write(response.text)

        except Exception as e:
            st.error(f"Error: {str(e)}")
