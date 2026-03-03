import streamlit as st
import random

# Dice Game Configuration
actions = ["Oil", "Dildo show", "Close up", "Slap/Spank", "Vibe", "Tease"]
body_parts = ["Boobs", "Ass", "Pussy", "Feet", "Thighs", "Full body"]

st.set_page_config(layout="wide", page_title="💖 Dice Game 💖")

# Girly Pink Theme & Clutter Removal
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;}
    [data-testid="stSidebar"] {display: none;}
    .stApp { background-color: #fff0f6; }
    .dice-num { font-size: 30px; font-weight: 900; color: #d63384; text-align: center; margin: 0; }
    .label-text { font-size: 16px; color: #862e9c; font-weight: bold; text-align: center; margin-bottom: 10px; }
    .stButton>button {
        width: 100%; height: 85px; border-radius: 15px; border: 2px solid #fcc2d7;
        background-color: #ffffff; color: #d63384; font-weight: bold; font-size: 16px;
    }
    .stButton>button:hover { background-color: #ffdeeb; border-color: #ff85b3; }
    .reveal-box {
        background: linear-gradient(45deg, #f06595, #cc5de8);
        color: white; height: 85px; display: flex; align-items: center;
        justify-content: center; border-radius: 15px; font-weight: bold; text-align: center;
    }
    .roll-status {
        font-size: 24px; font-weight: bold; color: white; text-align: center;
        padding: 15px; background: linear-gradient(to right, #ff85b3, #da77f2);
        border-radius: 50px; margin-bottom: 25px; border: 3px solid #fff;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #d63384;'>💖 🎲 Dice Game ($75) 🎲 💖</h1>", unsafe_allow_html=True)

# State Management
if 'flipped' not in st.session_state: st.session_state.flipped = set()
if 'd1' not in st.session_state: st.session_state.d1 = None
if 'd2' not in st.session_state: st.session_state.d2 = None

# Roller Controls
c1, c2, c3 = st.columns(3)
with c1:
    if st.button("🌸 Die 1 (Body)"):
        st.session_state.d1 = random.randint(1, 6)
        st.session_state.d2 = None
with c2:
    if st.button("✨ Die 2 (Action)"):
        if st.session_state.d1: st.session_state.d2 = random.randint(1, 6)
with c3:
    if st.button("♻️ Reset Board"):
        st.session_state.flipped = set()
        st.session_state.d1 = None
        st.session_state.d2 = None
        st.rerun()

# Show Result
if st.session_state.d1 and st.session_state.d2:
    p, a = st.session_state.d1, st.session_state.d2
    st.markdown(f"<div class='roll-status'>✨ Result: {p} ({body_parts[p-1]}) + {a} ({actions[a-1]}) ✨</div>", unsafe_allow_html=True)
elif st.session_state.d1:
    st.markdown(f"<div class='roll-status'>Die 1: {st.session_state.d1} ({body_parts[st.session_state.d1-1]}) ... Waiting for Die 2</div>", unsafe_allow_html=True)

# The 6x6 Grid
h_cols = st.columns([1.2] + [2]*6)
for i, act in enumerate(actions):
    with h_cols[i+1]:
        st.markdown(f"<p class='dice-num'>{i+1}</p><p class='label-text'>{act}</p>", unsafe_allow_html=True)

for r_idx, part in enumerate(body_parts):
    r_cols = st.columns([1.2] + [2]*6)
    with r_cols[0]:
        st.markdown(f"<p class='dice-num' style='text-align:right; padding-right:10px;'>{r_idx+1}</p>", unsafe_allow_html=True)
        st.markdown(f"<p class='label-text' style='text-align:right; padding-right:10px;'>{part}</p>", unsafe_allow_html=True)
    
    for c_idx in range(6):
        t_id = f"{r_idx}_{c_idx}"
        with r_cols[c_idx+1]:
            if t_id in st.session_state.flipped:
                st.markdown(f"<div class='reveal-box'>🔥 {actions[c_idx]}<br>{part}</div>", unsafe_allow_html=True)
            else:
                if st.button("Reveal", key=t_id):
                    st.session_state.flipped.add(t_id)
                    st.rerun()