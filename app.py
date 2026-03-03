import streamlit as st
import random
import time

# Game Data
actions = ["Oil", "Dildo show", "Close up", "Slap/Spank", "Vibe", "Tease"]
body_parts = ["Boobs", "Ass", "Pussy", "Feet", "Thighs", "Full body"]

st.set_page_config(layout="centered", page_title="🎲 $50 Monopoly Roll")

# Monopoly/Mobile Style CSS
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;}
    button[title="Manage app"] {display: none !important;}
    
    .stApp { background-color: #fff0f6; }
    
    /* Result Box with 'Pop' effect */
    .result-container {
        background: linear-gradient(135deg, #ff007a, #7000ff);
        color: white;
        padding: 40px;
        border-radius: 40px;
        text-align: center;
        margin-top: 20px;
        border: 8px solid #ffffff;
        box-shadow: 0px 15px 30px rgba(0,0,0,0.2);
    }
    .result-text { font-size: 55px; font-weight: 900; text-transform: uppercase; letter-spacing: -1px; }
    .sub-text { font-size: 22px; font-weight: bold; opacity: 0.8; margin-top: 5px; }

    /* Monopoly-style Round Buttons */
    .stButton>button {
        width: 100%;
        height: 110px;
        border-radius: 55px;
        border: 4px solid #ffffff;
        background: #d63384;
        color: white;
        font-weight: 900;
        font-size: 26px;
        box-shadow: 0px 8px 0px #9e205e;
        transition: 0.1s;
    }
    .stButton>button:active {
        transform: translateY(4px);
        box-shadow: 0px 4px 0px #9e205e;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #d63384; font-size: 40px;'>✨ $50 ROLL ✨</h1>", unsafe_allow_html=True)

if 'die1' not in st.session_state: st.session_state.die1 = None
if 'die2' not in st.session_state: st.session_state.die2 = None

# Step 1: Roll Body Part
if not st.session_state.die1:
    if st.button("🎲 ROLL BODY PART"):
        placeholder = st.empty()
        # Monopoly-style rapid shuffle
        for i in range(12):
            temp_part = random.choice(body_parts)
            placeholder.markdown(f"<div class='result-container' style='background:#ff85b3;'><div class='result-text'>{temp_part}</div></div>", unsafe_allow_html=True)
            time.sleep(0.05 + (i * 0.02)) # Gets slightly slower at the end
        st.session_state.die1 = random.randint(1, 6)
        st.rerun()

# Step 2: Roll Action
elif st.session_state.die1 and not st.session_state.die2:
    st.markdown(f"<div class='result-container' style='background:#ff85b3;'><div class='sub-text'>TARGET:</div><div class='result-text'>{body_parts[st.session_state.die1-1]}</div></div>", unsafe_allow_html=True)
    st.write("")
    if st.button("🎲 ROLL THE ACTION"):
        placeholder = st.empty()
        for i in range(12):
            temp_action = random.choice(actions)
            placeholder.markdown(f"<div class='result-container'><div class='result-text'>{temp_action}</div></div>", unsafe_allow_html=True)
            time.sleep(0.05 + (i * 0.02))
        st.session_state.die2 = random.randint(1, 6)
        st.rerun()

# Step 3: Final Reveal
if st.session_state.die1 and st.session_state.die2:
    p = body_parts[st.session_state.die1 - 1]
    a = actions[st.session_state.die2 - 1]
    st.markdown(f"""
        <div class='result-container'>
            <div class='sub-text'>YOU GOT:</div>
            <div class='result-text'>{a}</div>
            <div class='result-text' style='font-size:30px;'>ON {p}</div>
        </div>
    """, unsafe_allow_html=True)
    
    st.write("")
    if st.button("♻️ NEXT PLAYER ($50)"):
        st.session_state.die1 = None
        st.session_state.die2 = None
        st.rerun()