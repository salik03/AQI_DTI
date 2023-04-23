import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor

# Hide Streamlit menu and footer
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Load data
data = pd.read_csv("pages/anand_vihar_xlsx.csv")
data['Date'] = pd.to_datetime(data['Date'])
data['Day'] = data['Date'].dt.day
data['Month'] = data['Date'].dt.month
data['Year'] = data['Date'].dt.year

# Train model
X_train = data[['Day', 'Month', 'Year']]
y_train = data['AQI']
rf = RandomForestRegressor(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)

# Generate predictions for the next three days
today = pd.Timestamp.today().floor('D')
test_dates = pd.date_range(start=today, periods=3, freq='D')
X_test = pd.DataFrame({
    'Day': test_dates.day,
    'Month': test_dates.month,
    'Year': test_dates.year
})
y_pred = rf.predict(X_test)

# Display results
st.write("""
    <style>
        .title {
            animation-name: fade-in;
            animation-duration: 1s;
        }

        @keyframes fade-in {
            from {
                opacity: 0;
            }

            to {
                opacity: 1;
            }
        }
    </style>
""", unsafe_allow_html=True)

st.write('<h1 class="title" style="text-align:center">AQI Forecast for the Next Three Days</h1>', unsafe_allow_html=True)

for i in range(3):
    date = test_dates[i].strftime('%A, %B %d, %Y')
    st.write('---')
    st.write(f'## {date}')
    
    aqi = int(y_pred[i])
    if aqi <= 50:
        color = 'green'
    elif aqi <= 100:
        color = 'yellow'
    elif aqi <= 150:
        color = 'orange'
    elif aqi <= 200:
        color = 'red'
    else:
        color = 'darkred'
    
    st.write(f'<h2 style="color:{color}">AQI: {aqi}</h2>', unsafe_allow_html=True)
