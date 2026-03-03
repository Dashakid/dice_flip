import streamlit as st

# --- 1. GUI STYLING (The "Streamer" Look) ---
st.set_page_config(layout="wide")

st.markdown("""
    <style>
    /* Dark background for the whole app */
    .stApp { background-color: #0e1117; }
    
    /* Style for the Tile Buttons */
    div.stButton > button {
        height: 100px;
        width: 100%;
        background-color: #262730;
        color: #FFD700; /* Gold Text */
        border: 2px solid #FFD700;
        border-radius: 12px;
        font-size: 24px;
        font-weight: bold;
        transition: transform 0.2s, background-color 0.2s;
    }
    div.stButton > button:hover {
        transform: scale(1.05);
        background-color: #FFD700;
        color: #000000;
    }
    
    /* Style for the Revealed Prize */
    .prize-revealed {
        height: 100px;
        display: flex;
        align-items: center;
        justify-content: center;
        background-color: #00FF41; /* "Matrix" Green */
        color: black;
        border-radius: 12px;
        font-weight: bold;
        font-size: 18px;
        text-align: center;
        border: 2px solid white;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("💎 $75 Scratch-Off Reveal")

# --- 2. GAME LOGIC ---
# Define 30 prizes (You can change these to whatever she wants!)
if 'prizes' not in st.session_state:
    prizes_list = ["Sex Tape", "Private Live", "Spanks", "Fuck Machine", "Squirt"] * 6
    st.session_state.prizes = prizes_list

# Track which cards have been clicked
if 'flipped' not in st.session_state:
    st.session_state.flipped = [False] * 30

# --- 3. THE GUI GRID ---
# Create 5 rows
for row in range(5):
    cols = st.columns(6) # 6 columns per row = 30 tiles
    for col in range(6):
        index = (row * 6) + col
        with cols[col]:
            if st.session_state.flipped[index]:
                # Show the prize text if clicked
                st.markdown(f"<div class='prize-revealed'>{st.session_state.prizes[index]}</div>", unsafe_allow_html=True)
            else:
                # Show the interactive button
                if st.button(f"#{index + 1}", key=f"tile_{index}"):
                    st.session_state.flipped[index] = True
                    st.rerun()

# Secret Reset Button in the sidebar
if st.sidebar.button("Reset All Tiles"):
    st.session_state.flipped = [False] * 30
    st.rerun()