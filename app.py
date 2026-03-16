from dotenv import load_dotenv
load_dotenv()

import streamlit as st
from db import get_connection
from ai_trip_engine import run_crew


# Page settings
st.set_page_config(
    page_title="AI Travel Planner",
    page_icon="✈️",
    layout="wide"
)


# Custom CSS
st.markdown("""
<style>

/* Background */
[data-testid="stAppViewContainer"]{
background: linear-gradient(135deg,#0f2027,#203a43,#2c5364);
}

/* Remove default header background */
[data-testid="stHeader"]{
background: transparent;
}

/* Main page text */
h1, h2, h3, h4, h5, h6, p, span, label, div{
color:white !important;
}

/* FIX SIDEBAR TEXT COLOR ONLY */
section[data-testid="stSidebar"] *{
color:black !important;
}

/* Title */
h1{
text-align:center;
}

/* Subtitle */
.subtitle{
text-align:center;
color:#e0e0e0 !important;
margin-bottom:40px;
}

/* Input fields */
input, textarea{
color:black !important;
background:white !important;
}

/* Number input */
[data-baseweb="input"] input{
color:black !important;
}

/* Button styling */
.stButton>button{
background:linear-gradient(45deg,#ff416c,#ff4b2b);
color:white !important;
border:none;
border-radius:10px;
height:3em;
font-size:16px;
font-weight:bold;
width:200px;
}

.stButton>button:hover{
background:linear-gradient(45deg,#ff4b2b,#ff416c);
}

/* Result card */
.result-card{
background:white;
padding:25px;
border-radius:12px;
margin-top:20px;
box-shadow:0px 4px 15px rgba(0,0,0,0.2);
color:black !important;
}

</style>
""", unsafe_allow_html=True)


# Sidebar
with st.sidebar:
    st.title("✈️ Travel Planner")
    st.write("AI-powered itinerary generator using multi-agent systems.")
    st.write("Enter trip details to generate a smart travel plan.")


# Header
st.title("✈️ AI Multi-Agent Travel Planner")
st.markdown(
'<p class="subtitle">Plan your trip with intelligent AI agents</p>',
unsafe_allow_html=True
)


# Input section
col1, col2, col3 = st.columns(3)

with col1:
    destination = st.text_input("Destination")

with col2:
    budget = st.number_input("Budget (₹)", min_value=0)

with col3:
    days = st.number_input("Number of Days", min_value=1)


generate = st.button("Generate Trip")


# Generate itinerary
if generate:

    if destination.strip() == "":
        st.warning("Please enter a destination")
        st.stop()

    # Save trip
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO trips (destination, budget, days)
        VALUES (%s, %s, %s)
        """,
        (destination, budget, days)
    )

    conn.commit()
    cursor.close()
    conn.close()

    # Removed success message

    st.subheader("Generating AI Travel Plan...")

    with st.spinner("AI agents are planning your trip..."):
        itinerary = run_crew(destination, days, budget)

    st.markdown('<div class="result-card">', unsafe_allow_html=True)

    st.subheader("Your Travel Plan")
    st.markdown(itinerary)

    st.markdown('</div>', unsafe_allow_html=True)