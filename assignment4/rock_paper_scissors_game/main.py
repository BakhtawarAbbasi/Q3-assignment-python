import streamlit as st
import random

st.set_page_config(page_title="Rock, Paper, Scissors Game", page_icon="🎮", layout="centered")

st.markdown("<h1 style=' color: #C68EFD;'>🎮 Rock, Paper, Scissors Game</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Choose your move and try to beat the computer!</p>", unsafe_allow_html=True)

choices = ['Rock', 'Paper', 'Scissors']
images = {
    'Rock': 'rock.png',
    'Paper': 'paper.PNG',
    'Scissors': 'scissors.PNG'
}

# Displa top images 
col1, col2, col3 = st.columns(3)
with col1:
    st.image(images['Rock'], width=100, caption="Rock")
with col2:
    st.image(images['Paper'], width=100, caption="Paper")
with col3:
    st.image(images['Scissors'], width=100, caption="Scissors")

# Select User Move
user_choice = st.selectbox("👇 Select your move:", choices)

if st.button("🔥 Play Now"):
    computer_choice = random.choice(choices)

    # Display User and Computer Choices 
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("🧑 You choose:")
        st.image(images[user_choice], width=100)
        st.markdown(f"**{user_choice}**", unsafe_allow_html=True)

    with col2:
        st.subheader("🤖 Computer choose:")
        st.image(images[computer_choice], width=100)
        st.markdown(f"**{computer_choice}**", unsafe_allow_html=True)

    # Game Logic
    if user_choice == computer_choice:
        result = "🤝 It's a Tie!"
        color = "orange"
        balloons = False
    elif (
        (user_choice == 'Rock' and computer_choice == 'Scissors') or
        (user_choice == 'Paper' and computer_choice == 'Rock') or
        (user_choice == 'Scissors' and computer_choice == 'Paper')
    ):
        result = "🎉 You Win!"
        color = "green"
        balloons = True
    else:
        result = "😢 You Lose!"
        color = "red"
        balloons = False

    st.markdown(f"<h2 style='color:{color}; text-align:center'>{result}</h2>", unsafe_allow_html=True)
    
    # Show balloons
    if balloons:
        st.balloons()

st.markdown("---")
st.markdown("<p style='text-align: center; font-size: 14px;'>Made with ❤️ by Bakhtawar </p>", unsafe_allow_html=True)
