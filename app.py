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
    
    /* Result Box */
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
    .result-text { font-size: 50px; font-weight: 900; text-transform: uppercase; }
    .dice-shake { font-size: 100px; text-align: center; display: block; }

    /* Monopoly-style Round Buttons */
    .stButton>button {
        width: 100%; height: 100px; border-radius: 50px; border: 4px solid #ffffff;
        background: #d63384; color: white; font-weight: 900; font-size: 26px;
        box-shadow: 0px 8px 0px #9e205e;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #d63384;'>✨ $50 DICE ROLL ✨</h1>", unsafe_allow_html=True)

if 'die1' not in st.session_state: st.session_state.die1 = None
if 'die2' not in st.session_state: st.session_state.die2 = None

# Step 1: Roll Body Part
if not st.session_state.die1:
    if st.button("🎲 SHAKE & ROLL BODY"):
        placeholder = st.empty()
        dice_frames = ["⚀", "⚄", "⚂", "⚅", "⚁", "⚃"]
        # Fast "Monopoly" shake animation
        for i in range(15):
            frame = random.choice(dice_frames)
            placeholder.markdown(f"<div class='dice-shake'>{frame}</div>", unsafe_allow_html=True)
            time.sleep(0.06)
        st.session_state.die1 = random.randint(1, 6)
        st.rerun()

# Step 2: Roll Action
elif st.session_state.die1 and not st.session_state.die2:
    st.markdown(f"<div class='result-container' style='background:#ff85b3;'><h3>TARGET:</h3><div class='result-text'>{body_parts[st.session_state.die1-1]}</div></div>", unsafe_allow_html=True)
    if st.button("🎲 SHAKE & ROLL ACTION"):
        placeholder = st.empty()
        dice_frames = ["⚃", "⚁", "⚅", "⚂", "⚄", "⚀"]
        for i in range(15):
            frame = random.choice(dice_frames)
            placeholder.markdown(f"<div class='dice-shake'>{frame}</div>", unsafe_allow_html=True)
            time.sleep(0.06)
        st.session_state.die2 = random.randint(1, 6)
        st.rerun()

# Final Result
if st.session_state.die1 and st.session_state.die2:
    p = body_parts[st.session_state.die1 - 1]
    a = actions[st.session_state.die2 - 1]
    st.markdown(f"""
        <div class='result-container'>
            <div style='font-size: 20px; font-weight: bold;'>THE WINNER GETS:</div>
            <div class='result-text'>{a}</div>
            <div class='result-text' style='font-size:30px;'>ON {p}</div>
        </div>
    """, unsafe_allow_html=True)
    
    if st.button("♻️ RESET FOR NEXT ($50)"):
        st.session_state.die1 = None
        st.session_state.die2 = None
        st.rerun()