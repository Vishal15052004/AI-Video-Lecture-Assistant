import streamlit as st
from query import ask_question

st.set_page_config(
    page_title="AI Video Lecture Assistant",
    page_icon="🎥"
)

st.title("AI Video Lecture Assistant")

st.write("Ask any question related to your lecture video.")

question = st.text_input("Enter your question")

if st.button("Ask"):

    if question.strip():

        with st.spinner("Searching the lecture..."):

            answer = ask_question(question)

        st.subheader("Answer")

        st.write(answer)