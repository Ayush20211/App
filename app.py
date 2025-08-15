import streamlit as st

# --- Page config ---
st.set_page_config(page_title="ChatGPT Clone", layout="wide")

# --- Load Bootstrap Icons ---
st.markdown("""
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.5/font/bootstrap-icons.css">
""", unsafe_allow_html=True)

# --- Custom CSS for Dark UI ---
st.markdown("""
    <style>
    body {
        background-color: #111418;
        color: white;
        font-family: Arial, sans-serif;
    }
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background-color: #1e1f23;
        color: white;
        padding: 20px;
    }
    .sidebar-title {
        font-size: 20px;
        font-weight: bold;
        margin-bottom: 20px;
    }
    .menu-item {
        display: flex;
        align-items: center;
        gap: 10px;
        padding: 10px;
        cursor: pointer;
        border-radius: 8px;
        margin-bottom: 5px;
        color: white;
    }
    .menu-item:hover {
        background-color: #2a2b2f;
    }
    .chat-list {
        margin-top: 20px;
        font-weight: bold;
        font-size: 14px;
        opacity: 0.8;
    }
    .chat-item {
        padding: 8px;
        border-radius: 6px;
        cursor: pointer;
    }
    .chat-item:hover {
        background-color: #2a2b2f;
    }
    /* Main area */
    .main-container {
        text-align: center;
        margin-top: 150px;
    }
    .main-title {
        font-size: 28px;
        font-weight: bold;
        margin-bottom: 20px;
    }
    .search-box {
        display: flex;
        justify-content: space-between;
        align-items: center;
        background-color: #2a2b2f;
        padding: 10px 15px;
        border-radius: 50px;
        width: 500px;
        margin: auto;
    }
    .search-input {
        background: transparent;
        border: none;
        color: white;
        width: 350px;
        font-size: 16px;
        outline: none;
    }
    .icon-btn {
        color: white;
        font-size: 18px;
        cursor: pointer;
    }
    </style>
""", unsafe_allow_html=True)

# --- Sidebar ---
with st.sidebar:
    st.markdown("<div class='sidebar-title'>ChatGPT</div>", unsafe_allow_html=True)

    st.markdown("<div class='menu-item'><i class='bi bi-plus-lg'></i> New chat</div>", unsafe_allow_html=True)
    st.markdown("<div class='menu-item'><i class='bi bi-search'></i> Search chats</div>", unsafe_allow_html=True)
    st.markdown("<div class='menu-item'><i class='bi bi-journal'></i> Library</div>", unsafe_allow_html=True)
    st.markdown("<div class='menu-item'><i class='bi bi-play-circle'></i> Sora</div>", unsafe_allow_html=True)
    st.markdown("<div class='menu-item'><i class='bi bi-grid'></i> GPTs</div>", unsafe_allow_html=True)
    st.markdown("<div class='menu-item'><i class='bi bi-infinity'></i> Humanize AI</div>", unsafe_allow_html=True)

    st.markdown("<div class='chat-list'>Chats</div>", unsafe_allow_html=True)
    st.markdown("<div class='chat-item'>Streamlit UI creation</div>", unsafe_allow_html=True)
    st.markdown("<div class='chat-item'>JavaScript interview questions</div>", unsafe_allow_html=True)
    st.markdown("<div class='chat-item'>setTimeout function explanation</div>", unsafe_allow_html=True)
    st.markdown("<div class='chat-item'>Higher-order functions JavaScript</div>", unsafe_allow_html=True)
    st.markdown("<div class='chat-item'>Hoisting definition explained</div>", unsafe_allow_html=True)

# --- Main content ---
st.markdown("""
    <div class='main-container'>
        <div class='main-title'>What can I help with?</div>
        <div class='search-box'>
            <i class="bi bi-plus-lg icon-btn"></i>
            <input class='search-input' type='text' placeholder='Ask anything'>
            <i class="bi bi-mic icon-btn"></i>
            <i class="bi bi-sliders icon-btn"></i>
        </div>
    </div>
""", unsafe_allow_html=True)
