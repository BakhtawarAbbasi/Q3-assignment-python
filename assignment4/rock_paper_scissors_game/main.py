import streamlit as st
import random

st.set_page_config(page_title="Rock, Paper, Scissors Game", page_icon="🎮", layout="centered")

st.markdown("<h1 style='text-align: center; color: purple;'>🎮 Rock, Paper, Scissors Game</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Choose your move and try to beat the computer!</p>", unsafe_allow_html=True)

choices = ['🪨 Rock', '📄 Paper', '✂️ Scissors']

# Select User Move
user_choice = st.selectbox("👇 Select your move:", choices)

if st.button("🔥 Play Now"):
    computer_choice = random.choice(choices)

    # Display both choices in the same row
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("🧑 You chosoe:")
        st.markdown(f"<h2 style='text-align: center;'>{user_choice}</h2>", unsafe_allow_html=True)

    with col2:
        st.subheader("🤖 Computer choose:")
        st.markdown(f"<h2 style='text-align: center;'>{computer_choice}</h2>", unsafe_allow_html=True)

    # Remove emojis for logic comparison
    user = user_choice.split()[1]
    computer = computer_choice.split()[1]

    # Game Logic
    if user == computer:
        result = "🤝 It's a Tie!"
        color = "orange"
        balloons = False
    elif (
        (user == 'Rock' and computer == 'Scissors') or
        (user == 'Paper' and computer == 'Rock') or
        (user == 'Scissors' and computer == 'Paper')
    ):
        result = "🎉 You Win!"
        color = "green"
        balloons = True
    else:
        result = "😢 You Lose!"
        color = "red"
        balloons = False

    st.markdown(f"<h2 style='color:{color}; text-align:center'>{result}</h2>", unsafe_allow_html=True)

    if balloons:
        st.balloons()

st.markdown("---")
st.markdown("<p style='text-align: center; font-size: 14px;'>Made with ❤️ by Bakhtawar Abdul Kareem</p>", unsafe_allow_html=True)
