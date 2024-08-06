import os
from utils import utils
import streamlit as st
from PIL import Image
from backend.scriptdoctor import AIScriptDoctor
from dotenv import load_dotenv; load_dotenv()


# Setup your config
utils.page_config()
utils.style_app()


# Load and display the logo
image = Image.open("./logo/lyzr-logo.png")
st.image(image, width=150)

# App title and introduction
st.title("AI Script Doctor")
st.markdown("Identifies plot holes, pacing issues, and suggests improvements for film and TV scripts (enhances storytelling quality).")

# Setting up the sidebar for input
st.sidebar.image(image, width=100)
st.sidebar.title("AI Script Doctor")
API_KEY = st.sidebar.text_input(label="API Key",placeholder='OpenAI API Key', type="password")

st.sidebar.markdown('---')
utils.template_end()
utils.social_media()

if API_KEY != "":
    script = st.text_area("Enter Your Script", placeholder="Patse your script here", height=400)
    analyze_button = st.button("Analyze Script")
    if analyze_button:
        with st.spinner('Analyzing script...'):
            EnhancedScript = AIScriptDoctor(apikey=API_KEY, script=script)
            plot_holes = EnhancedScript[0]['task_output']
            pacing_issues = EnhancedScript[1]['task_output']
            improvements = EnhancedScript[2]['task_output']
            
            st.subheader('Plot Holes')
            st.write(plot_holes)
            
            st.subheader('Pacing Issues')
            st.write(pacing_issues)
            
            st.subheader('Suggestions for Improvement')
            st.write(improvements)
