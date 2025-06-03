import streamlit as st

# Page config
st.set_page_config(page_title="Hello Kitty Letters 💌", page_icon="🌸", layout="centered")

# Cute header
st.markdown("""
    <h1 style='text-align: center; color: #e75480; margin-bottom: 0;'>🌸 Hello Kitty Letters 💌</h1>
    <p style='text-align: center; color: #ffb6c1; margin-top: 5px;'>Made with love by Vanshika for her second home👩‍❤️‍💋‍👩</p>
""", unsafe_allow_html=True)

# Ask user for their name
name = st.text_input("Enter your name to receive your letter:", placeholder="Type your name here")

# Messages for each friend
letters = {
    "devyani": "Devyani 🦦 — To my Dearest Devu, I don’t even know where to start this letter from. First of all, thank you for being in my life. ... 🧡🧡🧡🧡🧡🧡🧡🧡🧡🧡",
    "shazia": "Shazia 🪼 — Hiiiiiiiiiiiiiiiii shazuuuuuuuuuuuuuuuuuu. This is for the coolest person I know. ... ❤️❤️❤️❤️❤️❤️❤️❤️",
    "tasmia": "Tasmia 🐙 — TASSUSUSUSUUUSUSUSUSUSUUSU. You are my favourite I don’t think ive hidden the fact ever. ... 💓💓💓💓💓💓💓💓💓💓💓",
    "samridhi": "Samridhi 🦆 — Helloooooooooooooooo SAMMMMMMMMMMMMMMM. The mom of our group, the most understanding and caring friend I've ever had. ... 💗💗💗💗💗💗💗💗💗💗💗"
}

# Normalize input for matching
name_lower = name.lower().strip()

# Display the letter if found
if name_lower in letters:
    st.markdown(f"""
        <div style='background-color: #ffe6f0; padding: 20px; border-radius: 20px; border: 2px solid pink; margin-top: 20px;'>
            <p style='color: #d63384; font-size: 18px; white-space: pre-line;'>{letters[name_lower]}</p>
            <p style='text-align: right; font-weight: bold;'>💖 Love, Vanshika</p>
        </div>
    """, unsafe_allow_html=True)
elif name != "":
    st.warning("Oops! I couldn’t find your name in my special Hello Kitty list 😿")

# Cute footer
st.markdown("<br><center>🌸 Powered by Streamlit x Hello Kitty ✨</center>", unsafe_allow_html=True)
