import streamlit as st
import re
import random
import string

def check_password_strength(password):
    score = 0
    feedback = []

    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password must be at least 8 characters long.")

    # Uppercase + Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Include both uppercase and lowercase letters.")

    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Include at least one number (0-9).")

    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("Include at least one special character (!@#$%^&*).")

    return score, feedback

def generate_strong_password(length=12):
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(characters) for _ in range(length))

# Streamlit UI
st.set_page_config(page_title="🔐 Password Strength Meter", page_icon="🔐")
st.title("🔐 Password Strength Meter + Generator")

password = st.text_input("Enter your password:")

if password:
    score, suggestions = check_password_strength(password)

    if score == 4:
        st.success("Strong Password! Well done!")
    elif score == 3:
        st.warning(" Moderate Password Consider improving it for better security.")
    else:
        st.error("Weak Password See the suggestions below:")
        for tip in suggestions:
            st.markdown(f"- {tip}")

st.markdown("---")
st.subheader("Strong Password Generator")

length = st.slider("Choose the password length:", 8, 24, 12)
if st.button("🔁 Generate Strong Password"):
    strong_password = generate_strong_password(length)
    st.code(strong_password, language='text')

st.write("------------------------------")

st.write("Created with 💕 by [Ghulam Mustafa Bhutto](https://github.com/ghulammustafa119)")