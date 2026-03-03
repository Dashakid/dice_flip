import streamlit as st
import random

# Define your grid data
actions = ["Oil", "Dildo show", "Close up", "Slap/Spank", "Vibe", "Tease"]
body_parts = ["Boobs", "Ass", "Pussy", "Feet", "Thighs", "Full body"]

st.set_page_config(layout="wide", page_title="Dice Game Reveal")

# Custom CSS for the "Premium" look and highlighting the roll
st.markdown("""
    <style>
    .stButton>button { width: 100%; height: 100px; font-size: 20px; font-weight: bold; border-radius: 10px; background-color: #2e2e2e; color: white; }
    .reveal-box { background-color: #28a745; color: white; height: 100px; display: flex; align-items: center; justify-content: center; border-radius: 10px; font-weight: bold; text-align: center; }
    .roll-display { font-size: 30px; font-weight: bold; color: #ff4b4b; text-align: center; padding: 10px; border: 2px solid #ff4b4b; border-radius: 10px; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🎲 Dice Game: Roll & Reveal")

# Initialize session state
if 'flipped_tiles' not in st.session_state:
    st.session_state.flipped_tiles = set()
if 'last_roll' not in st.session_state:
    st.session_state.last_roll = None

# --- DICE ROLLER SECTION ---
if st.button("🎲 ROLL THE DICE ($75)"):
    action_roll = random.randint(1, 6)
    part_roll = random.randint(1, 6)
    st.session_state.last_roll = (part_roll, action_roll)

if st.session_state.last_roll:
    p, a = st.session_state.last_roll
    st.markdown(f"<div class='roll-display'>Landed on: {p} ({body_parts[p-1]}) + {a} ({actions[a-1]})</div>", unsafe_allow_html=True)

# --- THE GRID ---
header_cols = st.columns([1] + [2]*6)
for idx, action in enumerate(actions):
    header_cols[idx + 1].markdown(f"### {idx+1}. {action}")

for row_idx, part in enumerate(body_parts):
    cols = st.columns([1] + [2]*6)
    cols[0].markdown(f"### {row_idx+1}. {part}")
    
    for col_idx in range(6):
        tile_id = f"{row_idx}_{col_idx}"
        with cols[col_idx + 1]:
            if tile_id in st.session_state.flipped_tiles:
                st.markdown(f"<div class='reveal-box'>{actions[col_idx]}<br>{part}</div>", unsafe_allow_html=True)
            else:
                if st.button(f"Click to Reveal", key=tile_id):
                    st.session_state.flipped_tiles.add(tile_id)
                    st.rerun()