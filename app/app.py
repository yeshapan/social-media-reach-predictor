import streamlit as st
import joblib
import numpy as np
from PIL import Image

# Load model
model = joblib.load('model/instagram_engagement_model.pkl')

# Set page config
st.set_page_config(page_title="Predict your reach on Instagram", page_icon="🌸", layout="centered")

# Custom CSS for baby pink + gold + elegant aesthetic
st.markdown("""
    <style>
    body {
        background-color: #fffafc;
    }
    .main {
        background-color: #fffafc;
    }
    header, footer {visibility: hidden;}
    .css-18e3th9 {
        padding-top: 2rem;
    }
    .title {
        font-family: 'Arial', sans-serif;
        font-size: 2.5rem;
        color: #E75480; /* Baby pink */
        text-align: center;
        margin-bottom: 0.5em;
    }
    .subtitle {
        font-family: 'Arial', sans-serif;
        font-size: 1.2rem;
        color: #D4AF37; /* Gold */
        text-align: center;
        margin-top: -10px;
        margin-bottom: 2em;
    }
    </style>
""", unsafe_allow_html=True)

# Top Logo
col1, col2, col3 = st.columns([1,2,1])
with col1:
    st.image("assets/logo.jpeg", width=80)  # profile logo in a circle
with col2:
    st.markdown("<h1 class='title'>Predict your reach on Instagram</h1>", unsafe_allow_html=True)
    st.markdown("<h3 class='subtitle'>coffee.compile ☕ by Yesha</h3>", unsafe_allow_html=True)
with col3:
    st.write("")

# User input
st.write("### Enter your Instagram stats:")

followers = st.number_input('Number of Followers:', min_value=0, step=10)

# Predict button
if st.button('Predict🌸'):
    if followers == 0:
        st.warning("Please enter your followers count!")
    else:
        input_data = np.array([[followers]])
        prediction = model.predict(input_data)
        
        estimated_likes = int(prediction[0][0])
        time_since_posted = int(prediction[0][1])
        
        st.success(f"✨ Estimated Likes: **{estimated_likes}**")
        st.info(f"🕒 Estimated Time Since Posted: **{time_since_posted} hours**")
