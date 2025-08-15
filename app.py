import streamlit as st

st.set_page_config(layout="wide")

# Custom CSS for exact look
st.markdown("""
    <style>
    /* Page */
    .stApp { background-color: #f5f5f7; }

    /* Remove default Streamlit padding */
    [data-testid="stVerticalBlock"] > div:first-child { padding-top: 0px; }
    
    /* Avatar */
    .user-avatar {
        position: fixed;
        left: 24px;
        bottom: 24px;
        width: 40px;
        height: 40px;
        border-radius: 50%;
        border: 2px solid #eee;
        background-image: url('https://randomuser.me/api/portraits/men/65.jpg');
        background-size: cover;
        background-position: center;
        z-index: 99999;
    }
    
    /* Sidebar icons */
    .sidebar-icon-holder {
        position: fixed;
        left: 20px;
        top: 70px;
        display: flex;
        flex-direction: column;
        gap: 22px;
        z-index: 99998;
    }
    .sidebar-icon {
        width: 40px;
        height: 40px;
        background: #fff;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        box-shadow: 0 1px 6px rgba(60,64,67,.12);
        margin-bottom: 1px;
        border: 2px solid #f3effc;
    }
    
    /* Header styles */
    .big-header {
        font-size: 2.8rem;
        font-weight: 700;
        margin-top: 70px;
        margin-bottom: 0.5rem;
        margin-left: 11vw;
        font-family: 'Inter', sans-serif;
        color: #18181b;
        text-shadow: 0px 1px 3px rgba(0,0,0,0.04);
    }
    .big-header .username {
        color: #d387e8;
    }
    .gradient-header {
        font-size: 2.3rem;
        font-weight: 700;
        margin-left: 11vw;
        font-family: 'Inter', sans-serif;
        background: linear-gradient(90deg,#18181b 50%,#7a5af8 80%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        text-fill-color: transparent;
        margin-bottom: 2.5rem;
    }
    .subtitle {
        margin-left: 11vw;
        margin-bottom: 24px;
        font-size: 1rem;
        color: #888;
        font-family: 'Inter', sans-serif;
    }
    /* Prompt Cards */
    .prompt-row {
        display: flex;
        gap: 38px;
        margin-bottom: 2rem;
        margin-left: 11vw;
    }
    .prompt-card {
        background: #fff;
        border-radius: 16px;
        min-width: 250px;
        box-shadow: 0 1px 8px rgba(60,64,67,.16);
        padding: 28px 32px;
        font-size: 1.05rem;
        font-family: 'Inter', sans-serif;
        font-weight: 500;
        color: #18181b;
        display: flex;
        justify-content: space-between;
        align-items: center;
        transition: box-shadow .2s;
        cursor: pointer;
    }
    .prompt-card:hover {
        box-shadow: 0 9px 20px rgba(60,64,67,.18);
    }
    .prompt-card svg {
        width: 22px;
        height: 22px;
    }

    /* Prompt Input Bar */
    .prompt-input-bar {
        background: #fff;
        border-radius: 16px;
        margin-left: 11vw;
        width: 78vw;
        box-shadow: 0 1px 8px rgba(60,64,67,.10);
        padding: 24px 32px;
        font-family: 'Inter', sans-serif;
        font-size: 1.11rem;
        font-weight: 400;
        margin-bottom: 42px;
        display: flex;
        flex-direction: column;
    }
    .attach-row {
        font-size: 0.97rem;
        color: #888;
        margin-top: 6px;
        letter-spacing: 0.15px;
    }
    /* Hide Streamlit hamburger and footer */
    #MainMenu, footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR ICONS (SVG for smooth look) ---
st.markdown("""
<div class="sidebar-icon-holder">
    <div class="sidebar-icon"><svg height="22" width="22" viewBox="0 0 24 24"><path fill="#d387e8" d="M3 13h2v-2H3v2zm7-8h2V3h-2v2zm8 8h2v-2h-2v2zM3 21h18V3H3v18zm2-2V5h14v14H5zm2-2h10v-2H7v2zm10 2H7v2h10v-2z"/><title>dashboard</title></svg></div>
    <div class="sidebar-icon"><svg height="22" width="22" viewBox="0 0 24 24"><path fill="#7a5af8" d="M3 3v18h18V3H3zm16 16H5V5h14v14z"/><title>folder</title></svg></div>
    <div class="sidebar-icon"><svg height="22" width="22" viewBox="0 0 24 24"><path fill="#7a5af8" d="M21 7v10c0 1.1-.9 2-2 2H5c-1.1 0-2-.9-2-2V7c0-1.1.9-2 2-2h14c1.1 0 2 .9 2 2z"/><title>message</title></svg></div>
</div>
""", unsafe_allow_html=True)

# --- AVATAR ---
st.markdown("""<div class="user-avatar"></div>""", unsafe_allow_html=True)

# --- HEADERS ---
st.markdown("""
<div class="big-header">
    Hi there, <span class="username">John</span>
</div>
<div class="gradient-header">
    What would like to know?
</div>
<div class="subtitle">
    Use one of the most common prompts below or use your own to begin
</div>
""", unsafe_allow_html=True)

# --- PROMPTS ---
st.markdown("""
<div class="prompt-row">
    <div class="prompt-card">
        Write a to-do list for a personal project or task 
        <svg viewBox="0 0 24 24"><path fill="#d387e8" d="M3 17.25V21h3.75l11.06-11.06-3.74-3.74L3 17.25zm15.36-9.09c.39-.39.39-1.02 0-1.41l-2.12-2.12a1 1 0 0 0-1.41 0l-1.83 1.83 3.54 3.54 1.82-1.83z"/></svg>
    </div>
    <div class="prompt-card">
        Generate an email to reply to a job offer 
        <svg viewBox="0 0 24 24"><path fill="#7a5af8" d="M20 4H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4.4-8 5.2-8-5.2V6l8 5.2L20 6v2.4z"/></svg>
    </div>
    <div class="prompt-card">
        Summarise this article or text for me in one paragraph 
        <svg viewBox="0 0 24 24"><path fill="#b6a6e9" d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm0 16H5v-2h14v2zm0-4H5v-2h14v2zm0-4H5V9h14v2zm0-4H5V5h14v2z"/></svg>
    </div>
    <div class="prompt-card">
        How does AI work in a technical capacity
        <svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="10" fill="#fca7ea"/><text x="12" y="16" fill="#fff" font-size="10" text-anchor="middle" font-family="Arial">AI</text></svg>
    </div>
</div>
""", unsafe_allow_html=True)

# --- PROMPT BAR ---
st.markdown("""
<div class="prompt-input-bar">
    Ask whatever you want....<br>
    <span class="attach-row">◦ Add Attachment &nbsp; ◦ Use Image</span>
</div>
""", unsafe_allow_html=True)
