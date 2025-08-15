import streamlit as st

st.set_page_config(layout="wide", page_title="UI Clone Responsive")

st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
<style>
.stApp { background: #f5f5f7 !important; font-family: 'Inter', sans-serif !important; }

/* Responsive layout: main container */
.main-container {
    max-width: 1100px;
    margin: auto;
    padding-top: 64px;
    padding-left: 60px;
    padding-right: 60px;
}

/* Mobile container overrides */
@media (max-width: 800px) {
    .main-container {
        padding: 18px;
        padding-top: 70px;
    }
}

/* Sidebar icons, fixed for desktop */
.sidebar-icons {
    position: fixed;
    left: 22px;
    top: 40px;
    display: flex;
    flex-direction: column;
    gap: 18px;
    z-index: 100;
}

/* Sidebar: horizontal on small screens */
@media (max-width: 650px) {
    .sidebar-icons {
        left: auto;
        right: 12px;
        top: 10px;
        flex-direction: row;
        gap: 12px;
        background: none;
    }
    .sidebar-icon {
        width: 38px !important;
        height: 38px !important;
    }
}

/* Avatar fixed for desktop, moves up for mobile */
.user-avatar {
    position: fixed;
    left: 22px;
    bottom: 24px;
    width: 34px;
    height: 34px;
    border-radius: 50%;
    border: 1.5px solid #eaeaea;
    background: url('https://randomuser.me/api/portraits/men/65.jpg') center center/cover;
    z-index: 101;
}

@media (max-width:650px) {
    .user-avatar { left: 14px; bottom: 12px; width: 28px; height: 28px;}
}

/* Headers */
.main-header {
    font-size: 2.6rem;
    font-weight: 700;
    margin-bottom: 0px;
    color: #18181b; font-family: 'Inter', sans-serif;
}
.main-header .username { color: #C078DD; }
.gradient-header {
    font-size: 2.3rem;
    font-weight: 700;
    margin-bottom: 11px;
    font-family: 'Inter', sans-serif;
    background: linear-gradient(90deg,#18181b 18%, #7a5af8 75%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.subtitle {
    font-size: 1.04rem;
    color: #6F6F7C;
    margin-bottom: 22px;
    font-weight: 400;
}

/* Responsive header text */
@media (max-width:650px){
    .main-header { font-size: 1.25rem; }
    .gradient-header { font-size: 1.09rem;}
    .subtitle { font-size: 0.90rem;}
}

/* Prompt cards group */
.prompt-row {
    display: flex;
    gap: 18px;
    margin-bottom: 21px;
    flex-wrap: wrap;
}

/* Individual card */
.prompt-card {
    background: #fff;
    border-radius: 15px;
    min-width: 200px;
    max-width: 260px;
    box-shadow: 0 1px 9px rgba(60,64,67,.13);
    padding: 17px 17px;
    font-size: 1.07rem;
    font-family: 'Inter', sans-serif;
    font-weight: 500;
    color: #191921;
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 9px;
    flex: 1 1 200px;
}
.prompt-card svg { width: 18px; height: 18px; }

@media (max-width: 650px) {
    .prompt-row { flex-direction: column; }
    .prompt-card { width: 100%; min-width: unset; max-width: unset; font-size: 1rem; }
}

/* Refresh row */
.refresh-row {
    font-size: 0.99rem;
    color: #bcbcdc;
    margin-bottom: 4px;
    display: flex;
    align-items:center;
}
.refresh-row svg { vertical-align: middle; margin-right: 4px; }

/* Input section */
.input-bar-holder { margin-top: 22px; }
.input-bar {
    background: #fff;
    border-radius: 15px;
    box-shadow: 0 1px 8px rgba(60,64,67,.08);
    padding: 17px 17px;
    font-family: 'Inter', sans-serif;
    font-size: 1.04rem;
    font-weight: 400;
    width: 100%;
    min-width: 230px;
    max-width: 670px;
    display: flex;
    flex-direction: column;
    position: relative;
    margin-bottom: 25px;
}
.input-bar-placeholder { color: #b9b9c9; margin-bottom: 8px; font-size: 1.05rem;}
.input-bar-row {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-top: 10px;
    flex-wrap: wrap;
}
.input-bar-opts { color: #9a9aaa; font-size: 0.98rem;}
.input-bar-opts svg { vertical-align: middle; margin-right: 4px;}
.input-bar-right { display: flex; align-items: center; gap: 13px;}
.input-bar-web {
    color: #5c5e80; font-size: 0.96rem; background:#f7f6fa; padding: 5px 11px;
    border-radius: 8px; box-shadow: 0 1px 2px rgba(60,64,67,.09);
    font-weight: 500; display:inline-flex; align-items: center;
}
.input-bar-count { color: #b9b9c9; font-size: 0.93rem;}
.input-bar-send-btn {
    background: #7a5af8; border-radius: 50%; width: 25px; height: 25px; display: flex; align-items: center; justify-content: center; font-size: 1.09rem; color: #fff; box-shadow: 0 1px 7px rgba(60,64,67,.10); cursor: pointer; transition: background .2s;
}
.input-bar-send-btn:hover { background: #9a7ffe; }

@media (max-width: 650px){
    .input-bar { max-width:100vw; min-width: 0; font-size: 0.99rem; padding: 9px 7px;}
    .input-bar-placeholder { font-size: 0.99rem;}
    .input-bar-row { flex-direction: column; align-items: flex-start;}
    .input-bar-opts { margin-bottom: 9px;}
    .input-bar-right { margin-bottom: 2px;}
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class='sidebar-icons'>
  <div class='sidebar-icon'>
    <svg fill="none" viewBox="0 0 24 24"><rect fill="#e8e6fb" width="16" height="16" x="4" y="4" rx="4"/><rect fill="#d3d0ed" width="6" height="6" x="4" y="4" rx="2"/></svg>
  </div>
  <div class='sidebar-icon'>
    <svg fill="none" viewBox="0 0 24 24"><rect fill="#e8e6fb" width="16" height="10" x="4" y="6" rx="4"/><rect fill="#d3d0ed" width="10" height="4" x="7" y="9" rx="2"/></svg>
  </div>
  <div class='sidebar-icon'>
    <svg fill="none" viewBox="0 0 24 24"><circle cx="12" cy="12" r="8" fill="#e8e6fb"/><circle cx="12" cy="12" r="4" fill="#d3d0ed"/></svg>
  </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""<div class="user-avatar"></div>""", unsafe_allow_html=True)

# Everything else in a responsive container
st.markdown("""
<div class="main-container">
    <div class='main-header'>
        Hi there, <span class='username'>John</span>
    </div>
    <div class='gradient-header'>
        What would like to know?
    </div>
    <div class='subtitle'>
        Use one of the most common prompts below or use your own to begin
    </div>
    <div class='prompt-row'>
        <div class='prompt-card'>
            Write a to-do list for a personal project or task
            <svg fill="none" viewBox="0 0 24 24"><rect width="18" height="18" x="3" y="3" rx="4" fill="#f3eccf"/><path d="M7 8.5h10M7 12h6M7 15.5h5" stroke="#c4a856" stroke-width="1.3" stroke-linecap="round"/></svg>
        </div>
        <div class='prompt-card'>
            Generate an email to reply to a job offer
            <svg fill="none" viewBox="0 0 24 24"><rect width="18" height="14" x="3" y="5" rx="4" fill="#e6e9f9"/><path d="M3 5l9 7 9-7" stroke="#8167d6" stroke-width="1.3"/></svg>
        </div>
        <div class='prompt-card'>
            Summarise this article or text for me in one paragraph
            <svg fill="none" viewBox="0 0 24 24"><rect x="3.5" y="5" width="17" height="13" rx="3.5" fill="#e6e7e9"/><path d="M7 9h10M7 13h5" stroke="#9696b7" stroke-width="1.3" stroke-linecap="round"/></svg>
        </div>
        <div class='prompt-card'>
            How does AI work in a technical capacity
            <svg fill="none" viewBox="0 0 24 24"><rect x="3" y="6" width="18" height="12" rx="6" fill="#f6d3ef"/><path d="M9 12h6M12 9v6" stroke="#e163b2" stroke-width="1.3" stroke-linecap="round"/></svg>
        </div>
    </div>
    <div class="refresh-row">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none"><path d="M4 12a8 8 0 1 1 8 8" stroke="#bcbcdc" stroke-width="2" stroke-linecap="round"/><path d="M4 12h5v5" stroke="#bcbcdc" stroke-width="2" stroke-linecap="round"/></svg>
        Refresh Prompts
    </div>
    <div class="input-bar-holder">
        <div class="input-bar">
            <div class="input-bar-placeholder">Ask whatever you want....</div>
            <div class="input-bar-row">
                <div class="input-bar-opts">
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none"><circle cx="12" cy="12" r="6" stroke="#b9b9c9" stroke-width="2"/><title>Add Attachment</title></svg>
                    Add Attachment &nbsp; •&nbsp; Use Image
                </div>
                <div class="input-bar-right">
                    <span class="input-bar-web">
                        <svg width="14" height="14" viewBox="0 0 24 24" fill="none"><circle cx="12" cy="12" r="6" stroke="#a098d0" stroke-width="2"/><title>Web</title></svg>
                        All Web
                    </span>
                    <span class="input-bar-count">0/1000</span>
                    <span class="input-bar-send-btn">
                        <svg width="16" height="16" fill="none" viewBox="0 0 24 24"><path d="M5 12l14-6-6 14-2-5-6-3z" fill="#fff"/><title>Send</title></svg>
                    </span>
                </div>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)
