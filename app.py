import streamlit as st
import random

# Game Data
actions = ["Oil", "Dildo show", "Close up", "Slap/Spank", "Vibe", "Tease"]
body_parts = ["Boobs", "Ass", "Pussy", "Feet", "Thighs", "Full body"]

st.set_page_config(layout="centered", page_title="✨ Dice Roller ✨")

# Minimalist Girly CSS
st.markdown("""
    <style>
    /* Hide all Streamlit UI clutter */
    #MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;}
    button[title="Manage app"] {display: none !important;}
    
    .stApp { background-color: #fff0f6; }
    
    /* Big Result Display */
    .result-container {
        background: linear-gradient(45deg, #f06595, #cc5de8);
        color: white;
        padding: 40px;
        border-radius: 30px;
        text-align: center;
        margin-top: 50px;
        border: 5px solid #fff;
        box-shadow: 0px 10px 20px rgba(0,0,0,0.1);
    }
    .result-text { font-size: 45px; font-weight: 900; line-height: 1.2; }
    .sub-text { font-size: 20px; font-weight: bold; opacity: 0.9; margin-top: 10px; }

    /* Large Pink Buttons */
    .stButton>button {
        width: 100%;
        height: 100px;
        border-radius: 50px;
        border: none;
        background-color: #d63384;
        color: white;
        font-weight: bold;
        font-size: 24px;
        box-shadow: 0px 4px 10px rgba(214, 51, 132, 0.3);
    }
    .stButton>button:hover {
        background-color: #f06595;
        transform: translateY(-2px);
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #d63384; margin-bottom: 50px;'>💖 🎲 DICE GAME ($75) 🎲 💖</h1>", unsafe_allow_html=True)

# State for the two dice
if 'die1' not in st.session_state: st.session_state.die1 = None
if 'die2' not in st.session_state: st.session_state.die2 = None

# Two-Step Roller
col1, col2 = st.columns(2)

with col1:
    if st.button("🌸 Roll Body"):
        st.session_state.die1 = random.randint(1, 6)
        st.session_state.die2 = None # Reset second die until rolled

with col2:
    if st.button("✨ Roll Action"):
        if st.session_state.die1:
            st.session_state.die2 = random.randint(1, 6)

# Display the Result
if st.session_state.die1 and st.session_state.die2:
    p_idx = st.session_state.die1 - 1
    a_idx = st.session_state.die2 - 1
    st.markdown(f"""
        <div class='result-container'>
            <div class='result-text'>🔥 {actions[a_idx]} 🔥</div>
            <div class='result-text'>on {body_parts[p_idx]}</div>
            <div class='sub-text'>🎲 Roll: {st.session_state.die1} + {st.session_state.die2}</div>
        </div>
    """, unsafe_allow_html=True)
    
    if st.button("♻️ Reset Game"):
        st.session_state.die1 = None
        st.session_state.die2 = None
        st.rerun()

elif st.session_state.die1:
    st.markdown(f"""
        <div class='result-container' style='background: #ff85b3;'>
            <div class='result-text'>Target: {body_parts[st.session_state.die1-1]}</div>
            <div class='sub-text'>Now roll the Action! ✨</div>
        </div>
    """, unsafe_allow_html=True)