# app.py
import streamlit as st

st.set_page_config(page_title="AI Home", layout="wide", initial_sidebar_state="collapsed")

# ----- CSS & icons -----
st.markdown("""
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.5/font/bootstrap-icons.css">
<style>
/* Hide Streamlit chrome */
#MainMenu, header[data-testid="stHeader"], footer, [data-testid="stSidebar"] {display:none;}
/* App background + container paddings */
[data-testid="stAppViewContainer"]{ background:#eeeeef; }
.block-container{ padding: 0 32px 60px 132px; max-width: 1400px; }

/* Left vertical toolbar */
.toolbar{
  position:fixed; left:18px; top:18px; width:68px; height:calc(100vh - 36px);
  background:#f3f3f4; border:1px solid #e6e7eb; border-radius:18px;
  display:flex; flex-direction:column; align-items:center; gap:14px; padding:12px 0;
  box-shadow:0 1px 2px rgba(0,0,0,.04);
}
.toolbar .icon{
  width:42px; height:42px; border-radius:12px; display:flex; align-items:center; justify-content:center;
  color:#6b7280; cursor:pointer;
}
.toolbar .icon:hover{ background:#e9e9ea; color:#111827; }
.toolbar .spacer{ flex:1; }
.toolbar .avatar{ width:30px; height:30px; border-radius:50%; border:1px solid #e5e7eb; overflow:hidden; }

/* Main page */
.page{ max-width: 980px; margin: 90px auto; color:#111827; font-family: ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Arial; }
.hi{ font-size:44px; font-weight:800; line-height:1.1; margin:0 0 6px 0; }
.grad{ background:linear-gradient(90deg,#a855f7,#6366f1); -webkit-background-clip:text; background-clip:text; color:transparent; }
.sub{ color:#6b7280; margin:10px 0 8px; }

/* Prompt cards */
.grid{ display:grid; grid-template-columns:repeat(4,1fr); gap:16px; margin-top:16px; }
.card{
  background:#ffffff; border:1px solid #e5e7eb; border-radius:14px; padding:16px; min-height:112px;
  box-shadow:0 1px 2px rgba(0,0,0,.04);
}
.card .cicon{ font-size:18px; color:#6b7280; margin-bottom:10px; }
.card p{ margin:0; color:#374151; font-weight:600; }

/* Refresh link */
.refresh{ margin-top:12px; color:#6b7280; font-size:14px; display:inline-flex; align-items:center; gap:6px; cursor:pointer; }

/* Composer */
.composer{
  margin-top:18px; width: 720px; background:#ffffff; border:1px solid #e5e7eb; border-radius:14px;
  box-shadow:0 1px 2px rgba(0,0,0,.04); padding:12px;
}
.composer textarea{
  width:100%; min-height:68px; resize:none; border:none; outline:none; font-size:15px; color:#111827;
}
.controls{ display:flex; justify-content:space-between; align-items:center; margin-top:8px; color:#6b7280; font-size:14px; }
.left span{ margin-right:20px; display:inline-flex; align-items:center; gap:8px; cursor:pointer; }
.right{ display:flex; align-items:center; gap:10px; }
.dd{ background:#f9fafb; border:1px solid #e5e7eb; color:#374151; border-radius:10px; padding:6px 10px; }
.counter{ color:#9ca3af; }
.send{ width:34px; height:34px; border-radius:50%; background:#8b5cf6; color:#fff;
       display:flex; align-items:center; justify-content:center; }
</style>
""", unsafe_allow_html=True)

# ----- Left fixed toolbar -----
st.markdown("""
<div class="toolbar">
  <div class="icon"><i class="bi bi-stars"></i></div>
  <div class="icon"><i class="bi bi-plus-lg"></i></div>
  <div class="icon"><i class="bi bi-search"></i></div>
  <div class="icon"><i class="bi bi-stickies"></i></div>
  <div class="icon"><i class="bi bi-folder"></i></div>
  <div class="icon"><i class="bi bi-globe2"></i></div>
  <div class="spacer"></div>
  <div class="icon"><i class="bi bi-gear"></i></div>
  <div class="icon" style="background:transparent">
    <img class="avatar" src="https://i.pravatar.cc/60?img=12">
  </div>
</div>
""", unsafe_allow_html=True)

# ----- Main content (center) -----
st.markdown("""
<div class="page">
  <div class="hi">Hi there, <span class="grad">John</span></div>
  <div class="hi">What <span class="grad">would like to know?</span></div>
  <div class="sub">Use one of the most common prompts below or use your own to begin</div>

  <div class="grid">
    <div class="card">
      <div class="cicon"><i class="bi bi-list-task"></i></div>
      <p>Write a to-do list for a personal project or task</p>
    </div>
    <div class="card">
      <div class="cicon"><i class="bi bi-envelope"></i></div>
      <p>Generate an email to reply to a job offer</p>
    </div>
    <div class="card">
      <div class="cicon"><i class="bi bi-chat-dots"></i></div>
      <p>Summarise this article or text for me in one paragraph</p>
    </div>
    <div class="card">
      <div class="cicon"><i class="bi bi-sliders"></i></div>
      <p>How does AI work in a technical capacity</p>
    </div>
  </div>

  <div class="refresh"><i class="bi bi-arrow-clockwise"></i> Refresh Prompts</div>

  <div class="composer">
    <textarea placeholder="Ask whatever you want...."></textarea>
    <div class="controls">
      <div class="left">
        <span><i class="bi bi-paperclip"></i> Add Attachment</span>
        <span><i class="bi bi-image"></i> Use Image</span>
      </div>
      <div class="right">
        <div class="dd"><i class="bi bi-globe2"></i> All Web</div>
        <div class="counter">0/1000</div>
        <div class="send"><i class="bi bi-arrow-right"></i></div>
      </div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)
