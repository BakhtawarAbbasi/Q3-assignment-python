import streamlit as st
from password_check import check_password_strength

# Page settings
st.set_page_config(page_title="🔐 Password Strength Meter", layout="centered")

# Title and instructions
st.markdown("## 🔐 Password Strength Meter")
st.markdown("Enter your password below and get instant feedback on its strength:")

# Show/hide password checkbox
show_password = st.checkbox("👁 Show Password")
password = st.text_input("Enter Password", type="default" if show_password else "password")

if password:
    # Call function
    strength, color, progress, suggestions = check_password_strength(password)

    # Show result
    st.markdown(f"### Strength: **:{color}[{strength}]**")
    st.progress(progress)

    # Suggestions
    if suggestions:
        st.markdown("#### 🔧 Suggestions to improve:")
        for tip in suggestions:
            st.markdown(f"- {tip}")
    else:
        st.success("✅ Your password is strong and secure!")

    # Bonus: Copy password (for fun)
    st.markdown("---")
    st.code(password, language="text")
    st.caption("📋 You can copy your password from above if needed.")
