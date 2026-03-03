import streamlit as st
import random

# Define your grid data
actions = ["Oil", "Dildo show", "Close up", "Slap/Spank", "Vibe", "Tease"]
body_parts = ["Boobs", "Ass", "Pussy", "Feet", "Thighs", "Full body"]

st.set_page_config(layout="wide", page_title="✨ Dice Game ✨")

# Girly Custom CSS
st.markdown("""
    <style>
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Background and Font */
    .stApp {
        background-color: #fff0f6;
    }
    
    /* Big Dice Labels (1, 2, 3...) */
    .dice-label {
        font-size: 32px;
        font-weight: 900;
        color: #d63384;
        text-align: center;
        text-shadow: 2px 2px #ffdeeb;
    }
    
    /* Action Names */
    .action-text {
        font-size: 18px;
        color: #862e9c;
        font-weight: bold;
        text-align: center;
    }

    /* Buttons (The Tiles) */
    .stButton>button {
        width: 100%;
        height: 90px;
        border-radius: 20px;
        border: 3px solid #fcc2d7;
        background-color: #ffffff;
        color: #d63384;
        font-weight: bold;
        font-size: 18px;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #ffdeeb;
        border-color: #ff85b3;
    }

    /* Revealed Tile */
    .reveal-box {
        background: linear-gradient(45deg, #f06595, #cc5de8);
        color: white;
        height: 90px;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 20px;
        font-weight: bold;
        text-align: center;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
    }

    /* Roll Status Box */
    .roll-status {
        font-size: 26px;
        font-weight: bold;
        color: white;
        text-align: center;
        padding: 20px;
        background: linear-gradient(to right, #ff85b3, #da77f2);
        border-radius: 50px;
        margin-bottom: 30px;
        border: 4px solid #fff;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #d63384;'>💖 🎲 Dice Game Reveal 🎲 💖</h1>", unsafe_allow_html=True)

# Initialize session state
if 'flipped_tiles' not in st.session_state:
    st.session_state.flipped_tiles = set()
if 'part_roll' not in st.session_state:
    st.session_state.part_roll = None
if 'action_roll' not in st.session_state:
    st.session_state.action_roll = None

# --- TWO-STEP PINK DICE ROLLER ---
c1, c2, c3 = st.columns(3)
with c1:
    if st.button("🌸 Roll Die 1 (Body)"):
        st.session_state.part_roll = random.randint(1, 6)
        st.session_state.action_roll = None
with c2:
    if st.button("✨ Roll Die 2 (Action)"):
        if st.session_state.part_roll:
            st.session_state.action_roll = random.randint(1, 6)
with c3:
    if st.button("♻️ Reset Board"):
        st.session_state.flipped_tiles = set()
        st.session_state.part_roll = None
        st.session_state.action_roll = None
        st.rerun()

# Display Roll Status
if st.session_state.part_roll and not st.session_state.action_roll:
    st.markdown(f"<div class='roll-status'>Die 1: {st.session_state.part_roll} ({body_parts[st.session_state.part_roll-1]}) ... Roll Die 2!</div>", unsafe_allow_html=True)
elif st.session_state.part_roll and st.session_state.action_roll:
    p, a = st.session_state.part_roll, st.session_state.action_roll
    st.markdown(f"<div class='roll-status'>✨ {p} ({body_parts[p-1]}) + {a} ({actions[a-1]}) ✨</div>", unsafe_allow_html=True)

# --- THE GRID ---
# Header Row (Actions)
cols = st.columns([1.2] + [2]*6)
for idx, action in enumerate(actions):
    with cols[idx+1]:
        st.markdown(f"<div class='dice-label'>{idx+1}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='action-text'>{action}</div>", unsafe_allow_html=True)

# Grid Rows (Body Parts)
for row_idx, part in enumerate(body_parts):
    cols = st.columns([1.2] + [2]*6)
    with cols[0]:
        st.markdown(f"<div class='dice-label' style='text-align: right; padding-right: 10px;'>{row_idx+1}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='action-text' style='text-align: right; padding-right: 10px;'>{part}</div>", unsafe_allow_html=True)
    
    for col_idx in range(6):
        tile_id = f"{row_idx}_{col_idx}"
        with cols[col_idx + 1]:
            if tile_id in st.session_state.flipped_tiles:
                st.markdown(f"<div class='reveal-box'>🔥 {actions[col_idx]}<br>on {part}</div>", unsafe_allow_html=True)
            else:
                if st.button(f"Click", key=tile_id):
                    st.session_state.flipped_tiles.add(tile_id)
                    st.rerun()