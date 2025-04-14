import streamlit as st
import re

st.set_page_config(page_title="Password Strength Checker", page_icon="🔒")

st.title(" 👋 Welcome to the Password Strength Checker!")
st.markdown("#### This app helps you create stronger, safer passwords using smart pattern recognition and analysis.")
st.markdown("Just type your password below, and we'll tell you how strong it is 💪")


password =st.text_input("Enter your Password", type="password")

def regex_password_strength(pw):
    score = 0

    # Length scoring
    if len(pw) >= 12:
        score += 3
    elif len(pw) >= 8:
        score += 2
    elif len(pw) >= 5:
        score += 1

    # Regex pattern checks
    if re.search(r"[a-z]", pw): score += 1     # lowercase
    if re.search(r"[A-Z]", pw): score += 1     # uppercase
    if re.search(r"\d", pw): score += 1        # number
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", pw): score += 1  # symbol

    # Penalty: repeated characters
    if re.search(r"(.)\1{2,}", pw):
        score -= 1

    # Bonus: contains lowercase, uppercase, and digit
    if re.search(r"[a-z]", pw) and re.search(r"[A-Z]", pw) and re.search(r"\d", pw):
        score += 1

    return max(score, 0)


def get_strength_message(score):
    if score >= 7:
        return "### 🟢 **Strong** – Your password is well-protected!"
    elif score >= 5:
        return "### 🟡 **Moderate** – Add more symbols or length to improve."
    elif score >= 3:
        return "### 🟠 **Weak** – Try mixing uppercase, numbers, and symbols."
    else:
        return "### 🔴 **Very Weak** – Easy to guess. Make it longer and more complex."


if password:
    score = regex_password_strength(password)
    st.markdown(f"## 🔢 Password Score: `{score}/8`")
    st.markdown(get_strength_message(score))


with st.expander("📌 Tips to create strong passwords"):
    st.markdown("""
    - Use **at least 12 characters**
    - Mix **UPPER** and **lower** case letters
    - Include **numbers** (`123`) and **symbols** (`@#$!`)
    - Avoid repeated patterns like `aaa`, `111`, or `password123`
    """)

