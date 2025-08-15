import streamlit as st

# ---- Google Fonts for Inter ----
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
<style>
body, html, .stApp { font-family: 'Inter', sans-serif !important; }

/* Custom background */
.stApp { background-color: #f5f5f7; }

/* Hide default Streamlit sidebar and hamburger/footer */
#MainMenu, footer {visibility: hidden;}
header {visibility: hidden;}

/* Sidebar icons */
.sidebar-icons {
    position: fixed;
    top: 32px;
    left: 24px;
    display: flex;
    flex-direction: column;
    gap: 18px;
    z-index: 9999;
}
.sidebar-icon {
    background: #fff;
    border-radius: 50%;
    width: 44px;
    height: 44px;
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: 0 2px 8px rgba(60,64,67,.12);
    border: none;
    transition: box-shadow 0.2s;
}
.sidebar-icon:hover {
    box-shadow: 0 6px 16px rgba(60,64,67,.16);
}

/* Avatar */
.user-avatar {
    position: fixed;
    left: 24px;
    bottom: 24px;
    width: 37px;
    height: 37px;
    border-radius: 50%;
    border: 1.5px solid #eaeaea;
    background: url('https://randomuser.me/api/portraits/men/65.jpg') center center/cover;
    z-index: 9999;
}

/* Main header */
.main-header {
    font-size: 2.6rem;
    font-weight: 700;
    margin-top: 68px;
    margin-bottom: 3px;
    margin-left: 320px;
    color: #18181b;
    font-family: 'Inter', sans-serif;
}
.main-header .username { color: #C078DD;}

/* Gradient header */
.gradient-header {
    font-size: 2.3rem;
    font-weight: 700;
    margin-left: 320px;
    margin-bottom: 17px;
    font-family: 'Inter', sans-serif;
    background: -webkit-linear-gradient(90deg,#18181b 12%, #7a5af8 70%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.subtitle {
    margin-left: 320px;
    font-size: 1.04rem;
    color: #6F6F7C;
    margin-bottom: 28px;
    font-weight: 400;
}

.prompt-row {
    display: flex;
    gap: 30px;
    margin-left: 320px;
    margin-bottom: 22px;
}

.prompt-card {
    background: #fff;
    border-radius: 15px;
    min-width: 233px;
    box-shadow: 0 1px 8px rgba(60,64,67,.13);
    padding: 21px 24px;
    font-size: 1.08rem;
    font-family: 'Inter', sans-serif;
    font-weight: 500;
    color: #191921;
    display: flex;
    justify-content: space-between;
    align-items: center;
}
.prompt-card svg { width: 18px; height: 18px; }

/* Refresh button */
.refresh-row {
    margin-left: 320px;
    font-size: 0.96rem;
    color: #bcbcdc;
    margin-bottom: 8px;
    margin-top: -12px;
    display: flex;
    align-items:center;
}
.refresh-row svg { vertical-align: middle; margin-right: 4px; }

/* Input area */
.input-bar-holder {
    margin-left: 320px;
    margin-top: 36px;
}
.input-bar {
    background: #fff;
    border-radius: 15px;
    box-shadow: 0 1px 8px rgba(60,64,67,.10);
    padding: 22px 26px;
    font-family: 'Inter', sans-serif;
    font-size: 1.09rem;
    font-weight: 400;
    width: 750px;
    min-width: 350px;
    display: flex;
    flex-direction: column;
    position: relative;
    margin-bottom: 44px;
}
.input-bar-placeholder {
    color: #b9b9c9;
    margin-bottom: 8px;
}
.input-bar-row {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-top: 10px;
}
.input-bar-opts {
    color: #9a9aaa;
    font-size: 1rem;
}
.input-bar-opts svg {
    vertical-align: middle;
    margin-right: 4px;
}
.input-bar-right {
    display: flex;
    align-items: center;
    gap: 22px;
}
.input-bar-web {
    color: #5c5e80;
    font-size: 1.05rem;
    background:#f7f6fa;
    padding: 6px 11px;
    border-radius: 9px;
    box-shadow: 0 1px 2px rgba(60,64,67,.09);
    font-weight: 500;
    display:inline-flex;
    align-items: center;
}
.input-bar-count {
    color: #b9b9c9;
    font-size: 0.97rem;
}
.input-bar-send-btn {
    background: #7a5af8;
    border-radius: 50%;
    width: 28px;
    height: 28px;
    display: flex;
    align-items:center;
    justify-content:center;
    font-size: 1.25rem;
    color: #fff;
    box-shadow: 0 1px 7px rgba(60,64,67,.10);
    cursor: pointer;
    transition: background .2s;
}
.input-bar-send-btn:hover {
    background: #9a7ffe;
}
</style>
""", unsafe_allow_html=True)

# ---- Sidebar ----
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

# ---- Avatar ----
st.markdown("""<div class="user-avatar"></div>""", unsafe_allow_html=True)

# ---- Main Header ----
st.markdown("""
<div class='main-header'>
    Hi there, <span class='username'>John</span>
</div>
<div class='gradient-header'>
    What would like to know?
</div>
<div class='subtitle'>
    Use one of the most common prompts below or use your own to begin
</div>
""", unsafe_allow_html=True)

# ---- Prompt Cards ----
st.markdown("""
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
""", unsafe_allow_html=True)

# ---- Refresh Prompts ----
st.markdown("""
<div class="refresh-row">
    <svg width="18" height="18" viewBox="0 0 24 24" fill="none"><path d="M4 12a8 8 0 1 1 8 8" stroke="#bcbcdc" stroke-width="2" stroke-linecap="round"/><path d="M4 12h5v5" stroke="#bcbcdc" stroke-width="2" stroke-linecap="round"/></svg>
    Refresh Prompts
</div>
""", unsafe_allow_html=True)

# ---- User Input Bar ----
st.markdown("""
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
""", unsafe_allow_html=True)
