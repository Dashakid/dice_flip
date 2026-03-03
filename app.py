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
        border-radius: