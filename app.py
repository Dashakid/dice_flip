import streamlit as st
import random
import time

# Game Data
actions = ["Oil", "Dildo show", "Close up", "Slap/Spank", "Vibe", "Tease"]
body_parts = ["Boobs", "Ass", "Pussy", "Feet", "Thighs", "Full body"]

st.set_page_config(layout="centered", page_title="🎲 DesiWaifu Dice")

# Custom CSS for Branding and Animation
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;}
    button[title="Manage app"] {display: none !important;}
    .stApp { background-color: #fff0f6; }
    
    .brand-header {
        text-align: center; background: #d63384; color: white;
        padding: 10px; border-radius: 15px; font-size: 30px;
        font-weight: 900; text-transform: uppercase; border: 4px solid #ffffff;
    }

    .roll-box {
        background: white; color: #d63384; padding: 30px;
        border-radius: 30px; text-align: center; margin: 20px 0;
        border: 4px dashed #d63384; font-size: 40px; font-weight: bold;
    }

    .result-container {
        background: linear-gradient(135deg, #ff007a, #7000ff);
        color: white; padding: 35px; border-radius: 40px;
        text-align: center; margin-top: 15px; border: 6px solid #ffffff;
    }
    .result-text { font-size: 45px; font-weight: 900; text-transform: uppercase; }

    .stButton>button {
        width: 100%; height: 80px; border-radius: 40px; border: 4px solid #ffffff;
        background: #d63384; color: white; font-weight: 900; font-size: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<div class='brand-header'>DESIWAIFU DICE GAME</div>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #d63384;'>✨ $50 TO PLAY ✨</h3>", unsafe_allow_html=True)

if 'die1' not in st.session_state: st.session_state.die1 = None
if 'die2' not in st.session_state: st.session_state.die2 = None

col1, col2 = st.columns(2)

with col1:
    if st.button("🌸 ROLL BODY"):
        st.session_state.die1 = None # Reset
        st.session_state.die2 = None
        placeholder = st.empty()
        # Longer Roll: 30 iterations at ~0.1s each = ~3 seconds
        for i in range(30):
            temp_name = random.choice(body_parts)
            placeholder.markdown(f"<div class='roll-box'>🎲 {temp_name}</div>", unsafe_allow_html=True)
            time.sleep(0.05 + (i * 0.005)) # Gradually slows down
        st.session_state.die1 = random.randint(1, 6)
        st.rerun()

with col2:
    if st.button("✨ ROLL ACTION"):
        if st.session_state.die1:
            placeholder = st.empty()
            for i in range(30):
                temp_name = random.choice(actions)
                placeholder.markdown(f"<div class='roll-box'>🎲 {temp_name}</div>", unsafe_allow_html=True)
                time.sleep(0.05 + (i * 0.005))
            st.session_state.die2 = random.randint(1, 6)
            st.rerun()

# Display logic
if st.session_state.die1 and st.session_state.die2:
    p = body_parts[st.session_state.die1 - 1]
    a = actions[st.session_state.die2 - 1]
    st.markdown(f"""
        <div class='result-container'>
            <div style='font-size: 18px; font-weight: bold;'>FINAL PRIZE:</div>
            <div class='result-text'>{a}</div>
            <div class='result-text' style='font-size:28px;'>ON {p}</div>
        </div>
    """, unsafe_allow_html=True)
    if st.button("♻️ RESET GAME"):
        st.session_state.die1 = None
        st.session_state.die2 = None
        st.rerun()

elif st.session_state.die1:
    st.markdown(f"""
        <div class='result-container' style='background:#ff85b3;'>
            <div style='font-size: 18px; font-weight: bold;'>Landed on:</div>
            <div class='result-text'>{body_parts[st.session_state.die1-1]}</div>
        </div>
    """, unsafe_allow_html=True)