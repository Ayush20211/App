import streamlit as st

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="Custom UI",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ---------- CUSTOM CSS ----------
st.markdown("""
    <style>
    /* Background */
    .stApp { background-color: #f5f5f7 !important; }

    /* Main header styles */
    .custom-header1 {
        font-size: 2.5rem;
        font-weight: 700;
        margin-top: 2rem;
        margin-bottom: 0.5rem;
        margin-left: 6%;
        color: #111111;
        font-family: 'Inter', sans-serif;
    }
    .custom-header2 {
        font-size: 2.25rem;
        font-weight: 700;
        margin-left: 6%;
        margin-bottom: 2rem;
        font-family: 'Inter', sans-serif;
    }
    .pink { color: #d387e8; }
    .purple { color: #7a5af8; }
    
    /* Prompt cards */
    .prompt-row {
        display: flex;
        gap: 30px;
        margin-bottom: 2rem;
        margin-left: 6%;
    }
    .prompt-card {
        background: #fff;
        border-radius: 16px;
        min-width: 210px;
        box-shadow: 0 1px 6px rgba(60,64,67,.15);
        padding: 20px 28px;
        text-align: left;
        font-size: 1.05rem;
        font-family: 'Inter', sans-serif;
        color: #111111;
        cursor: pointer;
        transition: box-shadow .2s;
    }
    .prompt-card:hover {
        box-shadow: 0 4px 12px rgba(60,64,67,.18);
    }
    .prompt-card-icon {
        font-size: 1.3rem;
        color: #aaa;
        float: right;
    }

    /* Prompt input box */
    .prompt-input {
        background: #fff;
        border-radius: 16px;
        margin-left: 6%;
        width: 80%;
        margin-bottom: 2rem;
        box-shadow: 0 1px 6px rgba(60,64,67,.08);
        padding: 20px 22px;
        font-family: 'Inter', sans-serif;
    }

    .attach-options {
        color: #888;
        font-size: 0.95rem;
        margin-top: 10px;
    }

    /* Sidebar icons */
    .sidebar-icons {
        position: fixed;
        top: 20px;
        left: 18px;
        display: flex;
        flex-direction: column;
        gap: 28px;
    }
    .sidebar-icon-button {
        background: #fff;
        border-radius: 50%;
        width: 38px;
        height: 38px;
        display: flex;
        align-items: center;
        justify-content: center;
        box-shadow: 0 2px 7px rgba(60,64,67,.11);
        transition: box-shadow .2s;
    }
    .sidebar-icon-button:hover {
        box-shadow: 0 5px 16px rgba(60,64,67,.14);
    }

    /* User avatar */
    .user-avatar {
        position: fixed;
        bottom: 18px;
        left: 18px;
        width: 35px;
        height: 35px;
        border-radius: 50%;
        background: url('https://randomuser.me/api/portraits/men/65.jpg') center center/cover;
        border: 1.5px solid #eaeaea;
    }
    </style>
""", unsafe_allow_html=True)

# ---------- SIDEBAR ICONS ----------
# You can use emoji or SVG for icons
st.markdown("""
<div class='sidebar-icons'>
    <div class='sidebar-icon-button'>🏠</div>
    <div class='sidebar-icon-button'>🗂️</div>
    <div class='sidebar-icon-button'>📄</div>
    <div class='sidebar-icon-button'>💬</div>
</div>
""", unsafe_allow_html=True)

# ---------- AVATAR ----------
st.markdown("<div class='user-avatar'></div>", unsafe_allow_html=True)

# ---------- MAIN HEADER ----------
st.markdown("""
    <div class='custom-header1'>Hi there, <span class='pink'>John</span></div>
    <div class='custom-header2'>What <span class='purple'>would like to know?</span></div>
""", unsafe_allow_html=True)

st.caption("Use one of the most common prompts below or use your own to begin")

# ---------- PROMPT CARDS ----------
st.markdown("""
<div class='prompt-row'>
    <div class='prompt-card'>Write a to-do list for a personal project or task <span class='prompt-card-icon'>📝</span></div>
    <div class='prompt-card'>Generate an email to reply to a job offer <span class='prompt-card-icon'>✉️</span></div>
    <div class='prompt-card'>Summarise this article or text for me in one paragraph <span class='prompt-card-icon'>🗨️</span></div>
    <div class='prompt-card'>How does AI work in a technical capacity <span class='prompt-card-icon'>🧠</span></div>
</div>
""", unsafe_allow_html=True)

st.markdown("##### ", unsafe_allow_html=True) # Spacer

# ---------- PROMPT INPUT ----------
st.markdown("""
<div class='prompt-input'>
    Ask whatever you want....<br>
    <div class='attach-options'>
        ◦ Add Attachment&nbsp;&nbsp;&nbsp;◦ Use Image
    </div>
</div>
""", unsafe_allow_html=True)

# OPTIONAL: You can add interactive Streamlit widgets if you want to make it dynamic.

