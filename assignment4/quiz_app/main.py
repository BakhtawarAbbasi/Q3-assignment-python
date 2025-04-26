import streamlit as st
import random

st.title("📝 Quiz Application")

questions = [
    {
        "question": "What is the capital of Pakistan",
        "options":["Karachi", "Lahore", "Islamabad", "Peshawar"],
        "answer": "Islamabad"
    },
    {
        "question": "What is the national language of Pakistan?",
        "options": ["Sindhi", "Punjabi", "Urdu", "Pashto"],
        "answer": "Urdu"
    },
    {
        "question": "Which is the largest province of Pakistan by area?",
        "options": ["Punjab", "Sindh", "Balochistan", "Khyber Pakhtunkhwa"],
        "answer": "Balochistan"
    },
    {
        "question": "Who is known as the founder of Pakistan?",
        "options": ["Allama Iqbal", "Liaquat Ali Khan", "Quaid-e-Azam", "Sir Syed Ahmed Khan"],
        "answer": "Quaid-e-Azam"
    },
    {
        "question": "Which river is the longest in Pakistan?",
        "options": ["Indus", "Chenab", "Ravi", "Jhelum"],
        "answer": "Indus"
    },
    {
        "question": "What is the currency of Pakistan?",
        "options": ["Taka", "Rupee", "Dinar", "Riyal"],
        "answer": "Rupee"
    },
    {
        "question": "Which city is known as the 'City of Lights' in Pakistan?",
        "options": ["Lahore", "Islamabad", "Karachi", "Faisalabad"],
        "answer": "Karachi"
    }
]

# Fix the session state check
if "current_question" not in st.session_state:
    st.session_state.current_question = random.choice(questions)
    st.session_state.answered = False

question = st.session_state.current_question

st.subheader(question["question"])

selected_option = st.selectbox("Choose your answer", question["options"], key="answer")

if st.button("Submit Answer") and not st.session_state.answered:
    if selected_option == question["answer"]:
        st.success("✅ Correct..!")
    else:
        st.error("❌ Incorrect..! The correct answer is " + question["answer"])
    st.session_state.answered = True

# After user has answered, show a "Next Question" button
if st.session_state.answered:
    if st.button("Next Question"):
        st.session_state.current_question = random.choice(questions)
        st.session_state.answered = False
        st.rerun()
