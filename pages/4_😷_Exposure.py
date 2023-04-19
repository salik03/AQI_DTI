import streamlit as st
import base64
st.title("Exposure")
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)


st.title("BreatheEasy")
st.write("EXPOSURE PAGE")

# Define the equation to calculate ADD
def calculate_add(cair, inh_rate, et, ef, ed, bw, at):
    add = cair * inh_rate * et * ef * ed / (bw * at)
    return add

# Get user input for body weight
bw = st.slider('Enter your body weight in kg:', 30, 200, 70)

# Estimate inhalation rate based on age
inh_rate = 0.5 # default value
age = st.slider('Enter your age:', 1, 100, 30)
if age <= 2:
    inh_rate = 0.25
elif age <= 12:
    inh_rate = 0.5
elif age <= 65:
    inh_rate = 0.5
else:
    inh_rate = 0.25

# Get user input for the remaining variables
cair = 261
et = st.slider('Enter the exposure time in hours per day:', 1, 24, 8)
ef = st.slider('Enter the exposure frequency in days per year:', 1, 365, 365)
ed = st.slider('Enter the exposure duration in years:', 1, 50, 1)
at = st.slider('Enter the averaging time in days:', 1, 365, 365)

# Calculate the ADD using the input values and the equation
add = calculate_add(cair, inh_rate, et, ef, ed, bw, at)

# Display the calculated ADD to the user
st.write('Your average daily dose (ADD) is:', add, 'mg/kg-day')

# Check if ADD is higher than threshold and display appropriate message
threshold = 1.5
if add >= threshold:
    st.write('Your ADD is high. Please consider lessening your exposure to the pollutant.')
    

else:
    st.write('Your ADD is Nominal')
