import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="CSE Engineering Doubt Solver")

st.title("🎓 CSE Engineering AI Doubt Solver")

api_key = st.text_input("Enter your OpenAI API Key:", type="password")
question = st.text_area("Enter your CSE question:")

if st.button("Solve") and question and api_key:
    client = OpenAI(api_key=api_key)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You are an expert CSE professor. Explain step-by-step with examples and code where needed."
            },
            {"role": "user", "content": question}
        ],
        temperature=0.3
    )

    st.markdown("### 📘 Explanation")
    st.write(response.choices[0].message.content)
