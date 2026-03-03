import streamlit as st
import random

# Dice Game Data Only
actions = ["Oil", "Dildo show", "Close up", "Slap/Spank", "Vibe", "Tease"]
body_parts = ["Boobs", "Ass", "Pussy", "Feet", "Thighs", "Full body"]

st.set_page_config(layout="wide", page_title="💖 Dice Game 💖")

st.markdown("""
    <style>
    #MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;}
    .stApp { background-color: #fff0f6; }
    .dice-label { font-size: 32px; font-weight: 900; color: #d63384; text-align: center; }
    .action-text { font-size: 18px; color: #862e9c; font-weight: bold; text-align: center; }
    .stButton>button { width: 100%; height: 90px; border-radius: 20px; border: 3px solid #fcc2d7; background-color: #ffffff; color: #d63384; font-weight: bold; }
    .reveal-box { background: linear-gradient(45deg, #f06595, #cc5de8); color: white; height: 90px; display: flex; align-items: center; justify-content: center; border-radius: 20px; font-weight: bold; text-align: center; }
    .roll-status { font-size: 26px; font-weight: bold; color: white; text-align: center; padding: 20px; background: linear-gradient(to right, #ff85b3, #da77f2); border-radius: 50px; margin-bottom: 30px; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #d63384;'>💖 🎲 Dice Game ($75) 🎲 💖</h1>", unsafe_allow_html=True)

if 'flipped_tiles' not in st.session_state: st.session_state.flipped_tiles = set()
if 'p_roll' not in st.session_state: st.session_state.p_roll = None
if 'a_roll' not in st.session_state: st.session_state.a_roll = None

# Controls
c1, c2, c3 = st.columns(3)
with c1:
    if st.button("🌸 Roll Body Part"):
        st.session_state.p_roll = random.randint(1, 6)
        st.session_state.a_roll = None
with c2:
    if st.button("✨ Roll Action"):
        if st.session_state.p_roll: st.session_state.a_roll = random.randint(1, 6)
with c3:
    if st.button("♻️ Reset Board"):
        st.session_state.flipped_tiles = set()
        st.session_state.p_roll = None
        st.session_state.a_roll = None
        st.rerun()

if st.session_state.p_roll and st.session_state.a_roll:
    p, a = st.session_state.p_roll, st.session_state.a_roll
    st.markdown(f"<div class='roll-status'>✨ {p} ({body_parts[p-1]}) + {a} ({actions[a-1]}) ✨</div>", unsafe_allow_html=True)

# Grid
cols = st.columns([1.2] + [2]*6)
for idx, action in enumerate(actions):
    with cols[idx+1]:
        st.markdown(f"<div class='dice-label'>{idx+1}</div><div class='action-text'>{action}</div>", unsafe_allow_html=True)

for r_idx, part in enumerate(body_parts):
    cols = st.columns([1.2] + [2]*6)
    with cols[0]:
        st.markdown(f"<div class='dice-label' style='text-align:right;'>{r_idx+1}</div><div class='action-text' style='text-align:right;'>{part}</div>", unsafe_allow_html=True)
    for c_idx in range(6):
        t_id = f"{r_idx}_{c_idx}"
        with cols[c_idx + 1]:
            if t_id in st.session_state.flipped_tiles:
                st.markdown(f"<div class='reveal-box'>🔥 {actions[c_idx]}<br>on {part}</div>", unsafe_allow_html=True)
            else:
                if st.button(f"Reveal", key=t_id):
                    st.session_state.flipped_tiles.add(t_id)
                    st.rerun()