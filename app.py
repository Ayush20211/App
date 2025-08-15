# app.py
import base64
from io import BytesIO
from PIL import Image
import streamlit as st

st.set_page_config(page_title="Resume Builder", layout="wide")

# ---------- helpers ----------
def _b64_img(file):
    if not file:
        return None
    img = Image.open(file).convert("RGB")
    # keep it small for preview
    img.thumbnail((220, 220))
    buf = BytesIO()
    img.save(buf, format="PNG")
    return base64.b64encode(buf.getvalue()).decode()

def pill(text):
    return f"""<span class="pill">{text}</span>"""

def icon_pill(text):
    # colored little dot + label (like the dribbble/instagram/linkedin pills)
    return f"""<span class="net-pill"><span class="dot"></span>{text}</span>"""

def dl_html(name, html):
    st.download_button(
        "Download",
        data=html.encode("utf-8"),
        file_name=f"{name or 'resume'}.html",
        mime="text/html",
        help="Download the preview as a single HTML file",
        key="dlbtn_top",
    )

# ---------- styles ----------
st.markdown(
    """
<style>
:root{
  --bg:#f4f5f7;
  --card:#ffffff;
  --text:#101114;
  --muted:#6b7280;
  --border:#e5e7eb;
  --primary:#111827;
  --pill:#f1f2f4;
  --shadow: 0 1px 2px rgba(0,0,0,.04), 0 8px 24px rgba(0,0,0,.06);
}
html, body, [data-testid="stAppViewContainer"]{
  background: var(--bg);
  font-family: ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, "Helvetica Neue", Arial, "Noto Sans", "Apple Color Emoji","Segoe UI Emoji";
}
.block-container{
  padding-top: 0rem;
  padding-bottom: 2rem;
}
.topbar{
  height:64px; background:var(--card); border:1px solid var(--border);
  border-radius: 12px; display:flex; align-items:center; padding:0 14px;
  box-shadow: var(--shadow);
}
.topbar .left{display:flex; gap:16px; align-items:center; flex:1}
.logo{
  width:28px; height:28px; background:#000; border-radius:50%;
  display:inline-flex; align-items:center; justify-content:center; color:#fff; font-weight:700;
}
.crumbs{color:var(--muted); font-size:14px}
.crumbs b{color:var(--text)}
.status{color:var(--muted); font-size:14px}
.topbar .right{display:flex; align-items:center; gap:10px}
.btn{
  height:38px; padding:0 16px; border-radius:10px; border:1px solid var(--border);
  background:#fff; font-weight:600; cursor:pointer;
}
.btn.primary{background:#111827; color:#fff; border-color:#111827}
.avatar{
  width:34px; height:34px; border-radius:50%; background:#fde68a; display:inline-block;
}

.layout{
  margin-top:18px; display:grid; grid-template-columns: 360px 1fr; gap:18px;
}
.panel{
  background:var(--card); border:1px solid var(--border); border-radius:12px; box-shadow:var(--shadow);
}
.panel .inner{padding:0;}
.sidebar{
  width:100%; display:grid; grid-template-rows:auto 1fr; min-height:720px;
}
.sidebar .sections{
  border-right:1px solid var(--border);
}
.section-item{
  display:flex; align-items:center; justify-content:space-between;
  padding:14px 16px; border-bottom:1px solid var(--border);
  font-weight:600;
}
.section-item .muted{color:var(--muted); font-weight:500}
.section-item .badge{background:#f1e7ff; color:#7c3aed; font-weight:700; font-size:12px; padding:4px 8px; border-radius:999px}

.form{
  padding:18px;
}
.form .uploader{
  display:flex; gap:16px; align-items:center; margin-bottom:16px;
}
.pic-circle{
  width:84px; height:84px; border-radius:50%; background:#f3f4f6; border:1px dashed var(--border);
  display:flex; align-items:center; justify-content:center; overflow:hidden;
}
.pic-circle img{ width:100%; height:100%; object-fit:cover;}
.browse{border:1px solid var(--border); background:#fff; height:36px; padding:0 12px; border-radius:8px; cursor:pointer;}
.label{font-size:13px; color:var(--muted); margin-bottom:6px}
.input{width:100%; height:40px; border:1px solid var(--border); border-radius:10px; padding:0 12px; background:#fff;}
.textarea{width:100%; min-height:90px; border:1px solid var(--border); border-radius:12px; padding:10px 12px; background:#fff;}

.preview{
  padding:18px;
}
.resume{
  width:720px; max-width:100%;
  background:#fff; border:1px solid var(--border); border-radius:12px; margin:0 auto; box-shadow:var(--shadow);
}
.resume .top-pills{
  padding:12px 16px; border-bottom:1px solid var(--border);
  background: linear-gradient(90deg, #efe7ff 0%, #e9f0ff 40%, #e2f5ff 100%);
  border-top-left-radius:12px; border-top-right-radius:12px;
}
.net-pill{
  display:inline-flex; gap:8px; align-items:center;
  background:#fff; border:1px solid var(--border); padding:6px 10px; border-radius:999px; margin-right:8px; font-weight:600; font-size:12px;
}
.net-pill .dot{width:8px; height:8px; background:#8b5cf6; border-radius:50%;}
.resume .body{padding:16px}
.resume .header{display:grid; grid-template-columns:72px 1fr; gap:12px; align-items:center;}
.resume .header .pfp{
  width:72px; height:72px; border-radius:50%; overflow:hidden; background:#f3f4f6; border:1px solid var(--border);
}
.resume .header h2{margin:0; font-size:22px}
.resume .header .role{color:var(--muted); margin-top:2px}
.resume .summary{color:#4b5563; margin-top:12px; border-top:1px solid var(--border); padding-top:12px;}

.block{border-top:1px solid var(--border); padding:14px 0}
.block h4{margin:0 0 10px 0; font-size:14px; text-transform:uppercase; letter-spacing:.02em; color:#6b7280}
.item{display:flex; align-items:center; justify-content:space-between; padding:8px 0}
.item .title{font-weight:600}
.date-pill{
  border:1px solid var(--border); background:#f9fafb; border-radius:999px; padding:6px 10px; font-size:12px;
}
.skills{display:flex; flex-wrap:wrap; gap:8px; padding-bottom:12px;}
.pill{
  background:var(--pill); border:1px solid var(--border); border-radius:999px;
  padding:6px 10px; font-weight:600; font-size:12px;
}
.footer-controls{display:flex; gap:10px; justify-content:center; padding:14px;}
.circle-btn{
  width:34px; height:34px; border-radius:50%; border:1px solid var(--border); background:#fff; display:flex; align-items:center; justify-content:center; cursor:pointer;
}

[data-testid="stForm"] {padding:0; background:transparent; border:0}
</style>
""",
    unsafe_allow_html=True,
)

# ---------- header bar ----------
with st.container():
    colL, colR = st.columns([1, 1])
    with colL:
        st.markdown(
            """
<div class="topbar">
  <div class="left">
    <div class="logo"></div>
    <div class="crumbs">Home  /  <b>Create resume</b></div>
    <div class="status">Saving your resume...</div>
  </div>
  <div class="right">
    """,
            unsafe_allow_html=True,
        )
    with colR:
        # Right side controls
        dl_placeholder = st.container()
        st.markdown(
            """
    <button class="btn">Share</button>
    <span class="avatar"></span>
</div></div>
""",
            unsafe_allow_html=True,
        )

# ---------- defaults/state ----------
st.session_state.setdefault("full_name", "Christina Sebastian")
st.session_state.setdefault("job_title", "UI UX Designer")
st.session_state.setdefault(
    "email", "christina1992@gmail.com"
)
st.session_state.setdefault("phone", "+00 9876543210")
st.session_state.setdefault(
    "address", "123 Main Street, Cityville, State 12345\nUnited States"
)
st.session_state.setdefault(
    "summary",
    "Designs digital interfaces and user experiences that are intuitive, visually appealing, and improve user satisfaction and engagement.",
)
st.session_state.setdefault("exp1_title", "UI/UX Designer")
st.session_state.setdefault("exp1_company", "ABC Company Inc.")
st.session_state.setdefault("exp1_dates", "Jan 2023 to Present")
st.session_state.setdefault("exp2_title", "UI/UX Designer")
st.session_state.setdefault("exp2_company", "XYZ Company")
st.session_state.setdefault("exp2_dates", "Jan 2020 to Dec 2022")
st.session_state.setdefault("edu_degree", "Bachelor of Design")
st.session_state.setdefault("edu_school", "XYZ University")
st.session_state.setdefault("edu_dates", "Jan 2017 to Jan 2020")
ALL_SKILLS = [
    "Figma",
    "Adobe XD",
    "Sketch",
    "Adobe Photoshop",
    "Adobe Illustrator",
    "Adobe Premiere Pro",
    "Adobe After Effects",
]
st.session_state.setdefault("skills", ALL_SKILLS[:7])

# ---------- layout ----------
st.markdown('<div class="layout">', unsafe_allow_html=True)

# -- left: sections + form
st.markdown('<div class="panel sidebar">', unsafe_allow_html=True)
st.markdown(
    """
<div class="sections">
  <div class="section-item">Personal informations <span>—</span></div>
  <div class="section-item">Professional summary <span>+</span></div>
  <div class="section-item">Experience <span>+</span></div>
  <div class="section-item">Education <span>+</span></div>
  <div class="section-item">Skills <span>+</span></div>
  <div class="section-item">Profile or portfolio URL <span>+</span></div>
  <div class="section-item">Add more details <span class="badge">Premium</span></div>
</div>
""",
    unsafe_allow_html=True,
)

# form
st.markdown('<div class="form">', unsafe_allow_html=True)
with st.form("resume_form", clear_on_submit=False):
    c1, c2 = st.columns([1, 2])
    with c1:
        photo_file = st.file_uploader("Upload your photo", type=["png", "jpg", "jpeg"])
        b64 = _b64_img(photo_file)
    with c2:
        st.write("")  # spacing
        st.markdown(
            '<div class="uploader"><div class="pic-circle">'
            + (f'<img src="data:image/png;base64,{b64}"/>' if b64 else "")
            + '</div><button class="browse" type="button">Browse photos</button></div>',
            unsafe_allow_html=True,
        )

    st.text_input("Full name", key="full_name")
    st.text_input("Job title", key="job_title")
    st.text_input("Email address", key="email")
    st.text_input("Mobile number", key="phone")
    st.text_area("Address", key="address")

    st.markdown("### Professional summary")
    st.text_area("", key="summary")

    st.markdown("### Experience 1")
    st.text_input("Role", key="exp1_title")
    st.text_input("Company", key="exp1_company")
    st.text_input("Dates", key="exp1_dates")

    st.markdown("### Experience 2")
    st.text_input("Role ", key="exp2_title")
    st.text_input("Company ", key="exp2_company")
    st.text_input("Dates ", key="exp2_dates")

    st.markdown("### Education")
    st.text_input("Degree", key="edu_degree")
    st.text_input("Institute", key="edu_school")
    st.text_input("Dates  ", key="edu_dates")

    st.markdown("### Skills")
    st.multiselect("Select skills", ALL_SKILLS, key="skills")

    st.form_submit_button("Apply changes")

st.markdown("</div></div>", unsafe_allow_html=True)  # end form + sidebar panel

# -- right: preview
st.markdown('<div class="panel"><div class="preview">', unsafe_allow_html=True)

# preview HTML
img_tag = (
    f'<img src="data:image/png;base64,{_b64_img(photo_file)}"/>'
    if photo_file
    else ""
)
skills_html = "".join(pill(s) for s in st.session_state["skills"])

resume_html = f"""
<div class="resume">
  <div class="top-pills">
    {icon_pill("Dribbble.com")}
    {icon_pill("Instagram.com")}
    {icon_pill("Linkedin.com")}
  </div>
  <div class="body">
    <div style="display:flex; gap:18px;">
      <div style="flex:1">
        <div style="display:grid; grid-template-columns: 64px 1fr; gap:12px; align-items:center;">
          <div class="pfp">{img_tag}</div>
          <div>
            <h2 style="margin:0">{st.session_state['full_name']}</h2>
            <div class="role">{st.session_state['job_title']}</div>
          </div>
        </div>
      </div>
      <div style="min-width:220px; font-size:12px; color:#111;">
        <div style="margin-bottom:6px"><b>Email</b><br>{st.session_state['email']}</div>
        <div style="margin-bottom:6px"><b>Phone</b><br>{st.session_state['phone']}</div>
        <div><b>Address</b><br>{st.session_state['address'].replace("\n","<br>")}</div>
      </div>
    </div>

    <div class="summary">{st.session_state['summary']}</div>

    <div class="block">
      <h4>Experience</h4>
      <div class="item">
        <div><div class="title">{st.session_state['exp1_title']}</div>{st.session_state['exp1_company']}</div>
        <div class="date-pill">{st.session_state['exp1_dates']}</div>
      </div>
      <div class="item">
        <div><div class="title">{st.session_state['exp2_title']}</div>{st.session_state['exp2_company']}</div>
        <div class="date-pill">{st.session_state['exp2_dates']}</div>
      </div>
    </div>

    <div class="block">
      <h4>Education</h4>
      <div class="item">
        <div><div class="title">{st.session_state['edu_degree']}</div>{st.session_state['edu_school']}</div>
        <div class="date-pill">{st.session_state['edu_dates']}</div>
      </div>
    </div>

    <div class="block" style="border-bottom:1px solid var(--border);">
      <h4>Skills</h4>
      <div class="skills">{skills_html}</div>
    </div>

    <div class="footer-controls">
      <div class="circle-btn">←</div>
      <div class="circle-btn">→</div>
    </div>
  </div>
</div>
"""

# render preview + top "Download" that exports the HTML
st.markdown(resume_html, unsafe_allow_html=True)
with dl_placeholder:
    dl_html(st.session_state["full_name"], f"<!doctype html><html><head><meta charset='utf-8'><title>Resume</title></head><body>{resume_html}</body></html>")

st.markdown("</div></div>", unsafe_allow_html=True)  # end preview panel
st.markdown("</div>", unsafe_allow_html=True)  # end grid layout
