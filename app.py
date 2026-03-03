import streamlit as st
import random
import time

# Game Data
actions = ["Oil", "Dildo show", "Close up", "Slap/Spank", "Vibe", "Tease"]
body_parts = ["Boobs", "Ass", "Pussy", "Feet", "Thighs", "Full body"]

st.set_page_config(layout="centered", page_title="🎲 DesiWaifu Dice")

# Monopoly/Mobile Style CSS with DesiWaifu Branding
st.markdown("""
    <style>
    /* Hide Streamlit UI */
    #MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;}
    button[title="Manage app"] {display: none !important;}
    
    .stApp { background-color: #fff0f6; }
    
    /* Branding Header */
    .brand-header {
        text-align: center;
        background: #d63384;
        color: white;
        padding: 10px;
        border-radius: 15px;
        font-size: 35px;
        font-weight: 900;
        text-transform: uppercase;
        letter-spacing: 2px;
        margin-bottom: 20px;
        border: 4px solid #ffffff;
    }

    /* Result Box */
    .result-container {
        background: linear-gradient(135deg, #ff007a, #7000ff);
        color: white;
        padding: 30px;
        border-radius: 40px;
        text-align: center;
        margin-top: 15px;
        border: 6px solid #ffffff;
        box-shadow: 0px 10px 20px rgba(0,0,0,0.1);
    }
    .result-text { font-size: 45px; font-weight: 900; text-transform: uppercase; }
    .dice-shake { font-size: 120px; text-align: center; display: block; margin: 10px 0; }

    /* Round Buttons */
    .stButton>button {
        width: 100%; height: 90px; border-radius: 45px; border: 4px solid #ffffff;
        background: #d63384; color: white; font-weight: 900; font-size: 22px;
        box-shadow: 0px 6px 0px #9e205e;
    }
    .stButton>button:active { transform: translateY(3px); box-shadow: 0px 3px 0px #9e205e; }
    </style>
    """, unsafe_allow_html=True)

# Branded Header
st.markdown("<div class='brand-header'>DESIWAIFU DICE GAME</div>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #d63384;'>✨ ONLY $50 TO PLAY ✨</h3>", unsafe_allow_html=True)

# State Management
if 'die1' not in st.session_state: st.session_state.die1 = None
if 'die2' not in st.session_state: st.session_state.die2 = None

# Two-Step Roller Layout
col1, col2 = st.columns(2)

with col1:
    if st.button("🌸 ROLL BODY"):
        placeholder = st.empty()
        dice_frames = ["⚀", "⚄", "⚂", "⚅", "⚁", "⚃"]
        for i in range(12):
            frame = random.choice(dice_frames)
            placeholder.markdown(f"<div class='dice-shake'>{frame}</div>", unsafe_allow_html=True)
            time.sleep(0.06)
        st.session_state.die1 = random.randint(1, 6)
        st.session_state.die2 = None 
        st.rerun()

with col2:
    if st.button("✨ ROLL ACTION"):
        if st.session_state.die1:
            placeholder = st.empty()
            dice_frames = ["⚃", "⚁", "⚅", "⚂", "⚄", "⚀"]
            for i in range(12):
                frame = random.choice(dice_frames)
                placeholder.markdown(f"<div class='dice-shake'>{frame}</div>", unsafe_allow_html=True)
                time.sleep(0.06)
            st.session_state.die2 = random.randint(1, 6)
            st.rerun()

# Display logic
if st.session_state.die1 and st.session_state.die2:
    p = body_parts[st.session_state.die1 - 1]
    a = actions[st.session_state.die2 - 1]
    st.markdown(f"""
        <div class='result-container'>
            <div style='font-size: 18px; font-weight: bold;'>PRIZE UNLOCKED:</div>
            <div class='result-text'>{a}</div>
            <div class='result-text' style='font-size:28px;'>ON {p}</div>
        </div>
    """, unsafe_allow_html=True)
    
    st.write("")
    if st.button("♻️ RESET FOR NEXT PLAYER"):
        st.session_state.die1 = None
        st.session_state.die2 = None
        st.rerun()

elif st.session_state.die1:
    st.markdown(f"""
        <div class='result-container' style='background:#ff85b3;'>
            <div style='font-size: 18px; font-weight: bold;'>BODY PART:</div>
            <div class='result-text'>{body_parts[st.session_state.die1-1]}</div>
            <div style='margin-top:10px; font-style: italic;'>Now Roll for Action!</div>
        </div>
    """, unsafe_allow_html=True)