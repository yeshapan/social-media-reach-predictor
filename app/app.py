#import libraries
import streamlit as st
import joblib
import numpy as np
from PIL import Image

#load the model
model = joblib.load('model/instagram_engagement_model.pkl')

#page setup
st.set_page_config(
    page_title="Predict your reach on Instagram", 
    page_icon="🌸", 
    layout="centered"
)

#CSS (ofc we'll make it pink duh)
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
        padding-top: 1rem;
    }
            
    /*  NOT NEEDED AS WE'RE USING H1 TAG
    .title {
        font-family: Avenir, Helvetica, "sans serif";
        font-size: 100rem; /* same size as h1 */
        font-weight: bold; /* h1 is usually bold */
        color: #F5F5F5; /* whitesmoke */
        text-align: center;
        margin-top: 0;
        margin-bottom: 1.0rem;
    }
    */

    .subtitle {
        font-family: Avenir, Helvetica, "sans serif";
        font-size: 0.8rem;
        color: #F5F5F5; /*whitesmoke*/
        text-align: center;
        margin-top: -7px;
        margin-bottom: 1rem;
    }
    input {
        background-color: rgba(255, 240, 245, 0.6) !important;
        border: 1px solid #E75480 !important;
        border-radius: 10px !important;
        color: #333 !important;
    }
    button {
        background-color: #E75480 !important;
        color: white !important;
        border: none !important;
        border-radius: 10px !important;
        padding: 0.75em 1.5em !important;
        font-size: 1rem !important;
        transition: all 0.3s ease-in-out;
    }
    button:hover {
        background-color: #D4AF37 !important; /*gold hover*/
        color: black !important;
        transform: scale(1.05);
    }
    .footer {
        font-size: 0.8rem;
        text-align: center;
        color: #999;
        margin-top: 5rem;
    }
    </style>
""", unsafe_allow_html=True)

#top header and logo
col1, col2, col3 = st.columns([1,9,1])
with col1:
    st.image("assets/logo.jpeg", width=20) #logo hehe
with col2:
    st.markdown("<h1 class='title' align='center' margin-bottom=5rem>Predict your likes on Instagram</h1>", unsafe_allow_html=True)
    
with col3:
    st.write("") #just empty for centering

#input fields
st.write("##### Enter your Instagram stats below⬇️:")

followers = st.number_input('👥 Number of Followers:', min_value=0, step=10)

#predict button
if st.button('Predict Now 💮'):
    if followers == 0:
        st.warning("Hmm... please enter a followers count! ☕")
    else:
        input_data = np.array([[followers]])
        prediction = model.predict(input_data)
        
        estimated_likes = int(prediction[0][0])
        time_since_posted = int(prediction[0][1])
        
        st.success(f"💗Estimated Likes: **{estimated_likes}**")
        st.info(f"🕒Expected Time Since Posted: **{time_since_posted} hours**")

#footer
st.markdown("<div class='footer'>Made with ☕ and dreams by Yesha</div>", unsafe_allow_html=True)