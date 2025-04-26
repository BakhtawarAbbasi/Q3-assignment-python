import streamlit as st
import random

# Page Configuration
st.set_page_config(
    page_title="Hangman Game",
    page_icon="🎯",
    layout="centered"
)

# Custom CSS 
st.markdown("""
    <style>
        /* General Styling */
        body {
            background-color: #000000;
            color: #FFFFFF;
        }
        .stApp {
            background-color: #000000;
        }
        h1, h2, h3, h4, h5, h6, p {
            color: #FFFFFF;
        }
        
        /* Text Input Styling */
        input[type="text"] {
            background-color: #1e1e1e !important;
            color: #FFFFFF !important;
            border-radius: 8px !important;
            border: 1px solid #FFFFFF !important;
        }

        /* Button Styling */
        button[kind="secondary"] {
            background-color: #black !important;
            color: #000000 !important;
            border: 2px solid #FFFFFF !important;
            border-radius: 8px !important;
            padding: 0.5em 1.5em !important;
            font-size: 16px !important;
            font-weight: bold !important;
            transition: 0.3s ease;
        }
        button[kind="secondary"]:hover {
            background-color: #white !important;
            color: #000000 !important;
            cursor: pointer;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.title("🎯 Hangman - Word Guessing Game ")

# Instructions
st.markdown("### Guess the word, one letter at a time.")
st.markdown("You have **6 attempts**. Can you uncover the hidden word before it's too late? 🕵️‍♀️")

# Initialize session state variables
if "word" not in st.session_state:
    words_list = ['python', 'streamlit', 'hangman', 'programming', 'challenge', 'developer', 'technology', 'interface']
    st.session_state.word = random.choice(words_list).upper()
    st.session_state.guessed_letters = []
    st.session_state.attempts_left = 6
    st.session_state.game_over = False

# Display guessed letters and remaining attempts
display_word = ""
for letter in st.session_state.word:
    if letter in st.session_state.guessed_letters:
        display_word += f"{letter} "
    else:
        display_word += "_ "

st.markdown(f"## `{display_word.strip()}`")
st.markdown(f"#### Attempts Left: **{st.session_state.attempts_left}**")
st.markdown(f"#### Guessed Letters: `{', '.join(st.session_state.guessed_letters)}`")

# Input for guessing a letter
if not st.session_state.game_over:
    guess = st.text_input("Enter a letter:").upper()

    if st.button("Guess"):
        if not guess.isalpha() or len(guess) != 1:
            st.warning("⚠️ Please enter a single alphabet letter.")
        elif guess in st.session_state.guessed_letters:
            st.info("ℹ️ You've already guessed that letter.")
        else:
            st.session_state.guessed_letters.append(guess)

            if guess not in st.session_state.word:
                st.session_state.attempts_left -= 1
                st.error(f"❌ Incorrect guess! Attempts left: {st.session_state.attempts_left}")
            else:
                st.success(f"✅ Good guess! `{guess}` is in the word.")

# Check for win condition
if all(letter in st.session_state.guessed_letters for letter in st.session_state.word):
    st.balloons()
    st.success(f"🎉 Congratulations! You guessed the word: `{st.session_state.word}`")
    st.session_state.game_over = True

# Check for lose condition
if st.session_state.attempts_left <= 0:
    st.error(f"💀 Game Over! The word was: `{st.session_state.word}`")
    st.session_state.game_over = True

# Restart game button
if st.session_state.game_over:
    if st.button("Play Again"):
        words_list = ['python', 'streamlit', 'hangman', 'programming', 'challenge', 'developer', 'technology', 'interface']
        st.session_state.word = random.choice(words_list).upper()
        st.session_state.guessed_letters = []
        st.session_state.attempts_left = 6
        st.session_state.game_over = False

# Footer
st.markdown("---")
st.caption("Made with ❤️ by Bakhtawar")