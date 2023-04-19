import streamlit as st
from PIL import Image

# Set page title and icon
st.set_page_config(page_title="BreatheEasy", page_icon="🌬️")
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Load logo
logo = Image.open('logo.png')

# Set up homepage layout
st.image(logo, width=200)
st.title('BreathEasy')
st.write('Your one-stop solution for air pollution monitoring and control in India!')
st.write('')

# Display main features
st.header('Main Features')
st.write('BreathEasy offers the following features to help you breathe easy:')
st.write('- Real-time Air Quality Index (AQI) data for major Indian cities')
st.write('- Personalized air quality recommendations based on your health status')
st.write('- Smart air purifiers with HEPA filters for your home or office')
st.write('- Air pollution masks designed for comfort and style')

# Display call-to-action
st.write('')
st.write('Ready to breathe easy? Sign up now and get a FREE air quality monitor with your first purchase!')
st.button('Sign Up Now')

# Display social media links
st.write('')
st.write('Follow us on social media:')
st.write('[Twitter](https://twitter.com/BreathEasyIndia)')
st.write('[Facebook](https://www.facebook.com/BreathEasyIndia)')
st.write('[Instagram](https://www.instagram.com/BreathEasyIndia)')

# Display footer
st.write('')
st.write('© 2023 BreathEasy, Inc. All rights reserved. Terms | Privacy | About')

# Display hero image in sidebar
st.sidebar.image('hero.png', use_column_width=True, clamp=True)
