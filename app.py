import streamlit as st

# --------------------
# Page Config
# --------------------
st.set_page_config(page_title="AI to Human", layout="wide")

# --------------------
# Custom CSS for Styling
# --------------------
st.markdown("""
    <style>
    /* General Page Styling */
    body {
        background-color: #f9f9fc;
        font-family: 'Arial', sans-serif;
    }
    .card {
        background: white;
        border-radius: 20px;
        padding: 20px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.05);
        text-align: center;
    }
    .section-title {
        font-size: 28px;
        font-weight: 700;
        margin-bottom: 20px;
    }
    .subtitle {
        color: #555;
        font-size: 16px;
        margin-bottom: 20px;
    }
    /* Gradient Button */
    .blue-btn {
        background: linear-gradient(90deg, #4f46e5, #3b82f6);
        color: white;
        padding: 12px 30px;
        border-radius: 8px;
        border: none;
        font-weight: bold;
        cursor: pointer;
        text-decoration: none;
        display: inline-block;
    }
    /* Pricing Table */
    .price-card {
        background: white;
        border-radius: 15px;
        padding: 20px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.05);
        text-align: center;
    }
    .price-title {
        font-size: 20px;
        font-weight: 600;
    }
    .price {
        font-size: 28px;
        font-weight: bold;
        margin: 10px 0;
    }
    </style>
""", unsafe_allow_html=True)

# --------------------
# Section 1: From AI to Human in 3-Steps
# --------------------
st.markdown("<div class='section-title'>From AI to Human in 3-Steps</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Detect AI patterns instantly and identify content that needs human touch.</div>", unsafe_allow_html=True)

cols = st.columns(3)
steps = [
    ("Input Content", "Place your AI-generated text here or upload it for instant analysis."),
    ("Detect AI Patterns", "See exactly where your writing is AI-like and needs improvement."),
    ("Humanize Content", "Make your text sound natural, readable, and trustworthy.")
]

for col, (title, desc) in zip(cols, steps):
    with col:
        st.markdown(f"<div class='card'><h4>{title}</h4><p>{desc}</p></div>", unsafe_allow_html=True)

st.write("---")

# --------------------
# Section 2: Testimonials
# --------------------
st.markdown("<div class='section-title'>Don’t take our words for granted</div>", unsafe_allow_html=True)

testimonial_cols = st.columns(4)
testimonials = [
    ("Jane Patel", "Content Creator", "Writing got easier using this platform."),
    ("Carl Poppa", "Freelancer", "My AI content now sounds 100% human."),
    ("Chris Vokse", "Marketer", "I stopped worrying about AI detection."),
    ("Manuel Sim", "Blogger", "Great tool for transforming AI drafts.")
]

for col, (name, role, feedback) in zip(testimonial_cols, testimonials):
    with col:
        st.markdown(f"<div class='card'><strong>{name}</strong><br><em>{role}</em><p>{feedback}</p></div>", unsafe_allow_html=True)

st.write("---")

# --------------------
# Section 3: Stop Worrying About AI Detection
# --------------------
st.markdown("""
    <div style="background: url('https://images.unsplash.com/photo-1506748686214-e9df14d4d9d0?fit=crop&w=1350&q=80'); 
                padding: 50px; 
                text-align: center;
                border-radius: 20px;
                color: white;">
        <h2>Stop worrying about AI detection</h2>
        <p>Start with 10,000 words free. No credit card required.</p>
        <a href="#" class="blue-btn">Start Free Trial</a>
    </div>
""", unsafe_allow_html=True)

st.write("---")

# --------------------
# Section 4: Pricing
# --------------------
st.markdown("<div class='section-title'>Simple Pricing for Better Content</div>", unsafe_allow_html=True)
pricing_cols = st.columns(3)
pricing_plans = [
    ("Free", "$0.00", ["10,000 words monthly", "Basic AI detection", "Standard humanizing", "2 AI-based history"]),
    ("Standard", "$9.99", ["50,000 words monthly", "Advanced AI detection", "Enhanced humanizing", "Full history"]),
    ("Premium", "$19.99", ["100,000 words monthly", "Advanced AI detection", "Enhanced humanizing", "Full history"])
]

for col, (plan, price, features) in zip(pricing_cols, pricing_plans):
    with col:
        st.markdown(f"<div class='price-card'><div class='price-title'>{plan}</div><div class='price'>{price}</div>", unsafe_allow_html=True)
        for f in features:
            st.write(f"✅ {f}")
        st.markdown("<br><a href='#' class='blue-btn'>Choose Plan</a></div>", unsafe_allow_html=True)
