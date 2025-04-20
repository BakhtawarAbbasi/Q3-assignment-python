import streamlit as st
import random

st.set_page_config(page_title="Guess the Number Game", page_icon="🎯")

# Title & Instructions
st.markdown("## 🎮 Welcome to the Guess the Number Game!")
st.markdown("I’m thinking of a number between **1 and 100**. Can you guess it? 🤔")

st.info("💡 Tip: Click 'Guess' after entering your number. You’ll get hints if it's too high or too low.")

# Initialize session state
if 'number' not in st.session_state:
    st.session_state.number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.game_over = False
    st.session_state.history = []

# Game Logic
if not st.session_state.game_over:
    guess = st.number_input("🎯 Enter your guess:", min_value=1, max_value=100, step=1, key="guess_input")
    
    if st.button("🔍 Guess"):
        st.session_state.attempts += 1
        st.session_state.history.append(guess)

        if guess < st.session_state.number:
            st.warning("📉 Too low! Try a higher number.")
        elif guess > st.session_state.number:
            st.warning("📈 Too high! Try a lower number.")
        else:
            st.success(f"🎉 Hooray! You guessed it right. The number was {st.session_state.number}!")
            st.balloons()
            st.session_state.game_over = True
            st.write(f"✅ You took **{st.session_state.attempts}** attempts.")

        # Show previous guesses
        if st.session_state.history:
            st.markdown(f"📜 Previous guesses: `{st.session_state.history}`")

# Reset Game
if st.button("🔁 Play Again"):
    st.session_state.number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.game_over = False
    st.session_state.history = []
    st.success("Game reset! Try to guess the new number 🎲")

# Footer
st.markdown("---")
st.markdown("Made with ❤️ by Bakhtawar using Streamlit")
