import streamlit as st

st.set_page_config(layout="wide")

# Hide default Streamlit elements
st.markdown("""
    <style>
        #MainMenu, header, footer {visibility: hidden;}
        body {
            background-color: #f5f5f5;
        }
        .sidebar {
            background-color: #f5f5f5 !important;
        }
        .sidebar-icons {
            display: flex;
            flex-direction: column;
            align-items: center;
            padding-top: 20px;
            gap: 20px;
        }
        .sidebar-icons i {
            font-size: 20px;
            color: #555;
            cursor: pointer;
        }
        .main-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            padding-top: 60px;
            font-family: Arial, sans-serif;
        }
        .greeting {
            font-size: 36px;
            font-weight: bold;
            text-align: center;
        }
        .greeting span.name {
            color: #a855f7;
        }
        .greeting span.question {
            background: linear-gradient(to right, #a855f7, #3b82f6);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .subtitle {
            color: #666;
            font-size: 16px;
            margin-top: 5px;
            text-align: center;
        }
        .prompt-cards {
            display: flex;
            gap: 15px;
            margin-top: 25px;
        }
        .prompt-card {
            background: white;
            border-radius: 10px;
            padding: 15px;
            width: 200px;
            text-align: left;
            box-shadow: 0px 1px 3px rgba(0,0,0,0.1);
            font-size: 14px;
            cursor: pointer;
            transition: 0.2s;
        }
        .prompt-card:hover {
            box-shadow: 0px 4px 8px rgba(0,0,0,0.15);
        }
        .prompt-icon {
            font-size: 18px;
            margin-bottom: 8px;
            color: #666;
        }
        .input-container {
            background: white;
            border-radius: 10px;
            padding: 10px;
            margin-top: 30px;
            width: 600px;
            box-shadow: 0px 1px 3px rgba(0,0,0,0.1);
        }
        textarea {
            width: 100%;
            border: none;
            resize: none;
            outline: none;
            font-size: 14px;
        }
        .input-footer {
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-size: 13px;
            color: #666;
            margin-top: 5px;
        }
        .input-footer-left {
            display: flex;
            gap: 15px;
            align-items: center;
        }
        .send-btn {
            background: #a855f7;
            border-radius: 50%;
            padding: 6px 10px;
            color: white;
            cursor: pointer;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar icons
st.sidebar.markdown("""
<div class="sidebar-icons">
    <i class="bi bi-stars"></i>
    <i class="bi bi-plus-lg"></i>
    <i class="bi bi-search"></i>
    <i class="bi bi-stickies"></i>
    <i class="bi bi-folder"></i>
    <i class="bi bi-globe"></i>
    <i class="bi bi-gear"></i>
</div>
""", unsafe_allow_html=True)

# Main container
st.markdown("""
<div class="main-container">
    <div class="greeting">
        Hi there, <span class="name">John</span><br>
        What <span class="question">would like to know?</span>
    </div>
    <div class="subtitle">
        Use one of the most common prompts below or use your own to begin
    </div>
    <div class="prompt-cards">
        <div class="prompt-card"><div class="prompt-icon"><i class="bi bi-list-task"></i></div>Write a to-do list for a personal project or task</div>
        <div class="prompt-card"><div class="prompt-icon"><i class="bi bi-envelope"></i></div>Generate an email to reply to a job offer</div>
        <div class="prompt-card"><div class="prompt-icon"><i class="bi bi-chat-dots"></i></div>Summarise this article or text for me in one paragraph</div>
        <div class="prompt-card"><div class="prompt-icon"><i class="bi bi-sliders"></i></div>How does AI work in a technical capacity</div>
    </div>
    <div class="input-container">
        <textarea placeholder="Ask whatever you want...."></textarea>
        <div class="input-footer">
            <div class="input-footer-left">
                <i class="bi bi-paperclip"></i> Add Attachment
                <i class="bi bi-image"></i> Use Image
            </div>
            <div class="send-btn">
                <i class="bi bi-arrow-right"></i>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Load Bootstrap Icons
st.markdown('<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.5/font/bootstrap-icons.css">', unsafe_allow_html=True)
