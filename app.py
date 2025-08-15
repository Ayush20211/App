import streamlit as st

# --- Page settings ---
st.set_page_config(page_title="AI Dashboard", layout="wide")

# --- Load Bootstrap Icons ---
st.markdown("""
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.5/font/bootstrap-icons.css">
""", unsafe_allow_html=True)

# --- Custom CSS ---
st.markdown("""
    <style>
    body {
        background-color: #f4f4f4;
        font-family: Arial, sans-serif;
    }
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background-color: #f0f0f0;
        padding-top: 20px;
    }
    .sidebar-icon {
        font-size: 20px;
        display: flex;
        justify-content: center;
        align-items: center;
        height: 45px;
        width: 45px;
        margin: auto;
        margin-bottom: 15px;
        border-radius: 8px;
        color: #555;
        cursor: pointer;
    }
    .sidebar-icon:hover {
        background-color: #e0e0e0;
    }
    /* Main section */
    .main-container {
        padding: 40px;
        background-color: #f4f4f4;
    }
    .welcome-text {
        font-size: 34px;
        font-weight: bold;
    }
    .welcome-text span {
        background: linear-gradient(to right, #a855f7, #6366f1);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .sub-text {
        font-size: 16px;
        color: #555;
        margin-bottom: 30px;
    }
    /* Prompt cards */
    .prompt-cards {
        display: flex;
        gap: 15px;
        margin-bottom: 20px;
    }
    .prompt-card {
        background-color: white;
        border-radius: 10px;
        padding: 15px;
        width: 200px;
        box-shadow: 0 2px 6px rgba(0,0,0,0.1);
        cursor: pointer;
        font-size: 14px;
    }
    .prompt-card:hover {
        background-color: #f9f9f9;
    }
    .prompt-icon {
        font-size: 18px;
        margin-bottom: 10px;
        color: #555;
    }
    /* Input box */
    .input-container {
        background-color: white;
        border-radius: 10px;
        padding: 15px;
        box-shadow: 0 2px 6px rgba(0,0,0,0.1);
        display: flex;
        flex-direction: column;
        gap: 10px;
        width: 700px;
    }
    .input-textarea {
        border: none;
        outline: none;
        resize: none;
        font-size: 15px;
        height: 60px;
        color: #333;
    }
    .input-footer {
        display: flex;
        justify-content: space-between;
        font-size: 14px;
        color: #666;
        align-items: center;
    }
    .footer-left span {
        margin-right: 20px;
        cursor: pointer;
    }
    .footer-left span:hover {
        text-decoration: underline;
    }
    .send-btn {
        background-color: #7c3aed;
        color: white;
        border: none;
        border-radius: 50%;
        width: 35px;
        height: 35px;
        display: flex;
        justify-content: center;
        align-items: center;
        cursor: pointer;
    }
    </style>
""", unsafe_allow_html=True)

# --- Sidebar ---
with st.sidebar:
    st.markdown("<div class='sidebar-icon'><i class='bi bi-stars'></i></div>", unsafe_allow_html=True)
    st.markdown("<div class='sidebar-icon'><i class='bi bi-plus-lg'></i></div>", unsafe_allow_html=True)
    st.markdown("<div class='sidebar-icon'><i class='bi bi-search'></i></div>", unsafe_allow_html=True)
    st.markdown("<div class='sidebar-icon'><i class='bi bi-journal'></i></div>", unsafe_allow_html=True)
    st.markdown("<div class='sidebar-icon'><i class='bi bi-folder'></i></div>", unsafe_allow_html=True)
    st.markdown("<div class='sidebar-icon'><i class='bi bi-globe'></i></div>", unsafe_allow_html=True)

    st.markdown("<div style='margin-top: auto;'></div>", unsafe_allow_html=True)
    st.markdown("<div class='sidebar-icon'><i class='bi bi-gear'></i></div>", unsafe_allow_html=True)
    st.markdown("<div class='sidebar-icon'><img src='https://via.placeholder.com/30' style='border-radius:50%;'></div>", unsafe_allow_html=True)

# --- Main area ---
st.markdown("""
<div class='main-container'>
    <div class='welcome-text'>Hi there, <span>John</span></div>
    <div class='welcome-text'>What <span>would like to know?</span></div>
    <div class='sub-text'>Use one of the most common prompts below or use your own to begin</div>
    
    <div class='prompt-cards'>
        <div class='prompt-card'><div class='prompt-icon'><i class='bi bi-list-task'></i></div>Write a to-do list for a personal project or task</div>
        <div class='prompt-card'><div class='prompt-icon'><i class='bi bi-envelope'></i></div>Generate an email to reply to a job offer</div>
        <div class='prompt-card'><div class='prompt-icon'><i class='bi bi-chat-dots'></i></div>Summarise this article or text for me in one paragraph</div>
        <div class='prompt-card'><div class='prompt-icon'><i class='bi bi-sliders'></i></div>How does AI work in a technical capacity</div>
    </div>
    
    <div style='margin-bottom:20px; color:#666; font-size:14px; cursor:pointer;'><i class='bi bi-arrow-clockwise'></i> Refresh Prompts</div>
    
    <div class='input-container'>
        <textarea class='input-textarea' placeholder='Ask whatever you want....'></textarea>
        <div class='input-footer'>
            <div class='footer-left'>
                <span><i class='bi bi-paperclip'></i> Add Attachment</span>
                <span><i class='bi bi-image'></i> Use Image</span>
            </div>
            <div style='display:flex; gap:10px; align-items:center;'>
                <div>0/1000</div>
                <button class='send-btn'><i class='bi bi-arrow-right'></i></button>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)
