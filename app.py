import streamlit as st

# --- Page config ---
st.set_page_config(page_title="ChatGPT Clone", layout="wide")

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
    }
    .chat-item {
        padding: 8px;
        background-color: transparent;
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
        justify-content: center;
        align-items: center;
        background-color: #2a2b2f;
        padding: 10px;
        border-radius: 50px;
        width: 400px;
        margin: auto;
    }
    .search-input {
        background: transparent;
        border: none;
        color: white;
        width: 300px;
        font-size: 16px;
        outline: none;
    }
    </style>
""", unsafe_allow_html=True)

# --- Sidebar ---
with st.sidebar:
    st.markdown("<div class='sidebar-title'>ChatGPT</div>", unsafe_allow_html=True)
    st.markdown("<div class='menu-item'>New chat</div>", unsafe_allow_html=True)
    st.markdown("<div class='menu-item'>Search chats</div>", unsafe_allow_html=True)
    st.markdown("<div class='menu-item'>Library</div>", unsafe_allow_html=True)
    st.markdown("<div class='menu-item'>Sora</div>", unsafe_allow_html=True)
    st.markdown("<div class='menu-item'>GPTs</div>", unsafe_allow_html=True)
    st.markdown("<div class='menu-item'>Humanize AI</div>", unsafe_allow_html=True)

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
            <input class='search-input' type='text' placeholder='Ask anything'>
        </div>
    </div>
""", unsafe_allow_html=True)
