import streamlit as st
import calendar



# Set page title
st.set_page_config(page_title="Calendar")

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)


# Define CSS style tags for each font color and the table
style = """
    <style>
        table {
            width: 100%;
            font-size: 24px;
        }
        th {
            color: #333;
        }
        td {
            text-align: center;
            padding: 10px;
            color: #888;
        }
        .orange {
            color: orange;
        }
        .yellow {
            color: yellow;
        }
        .red {
            color: red;
        }
        .white {
            color: white;
        }
    </style>
"""

# Define function to get the style class for each day based on its value
def get_class(day):
    if day in [19, 17, 14, 10, 3]:
        return 'orange'
    elif day in [1, 2, 4, 5, 6, 7, 8]:
        return 'yellow'
    elif day <= 19:
        return 'red'
    else:
        return 'white'

# Define the days of the week
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

# Define a dropdown menu for the year and month
current_year = calendar.datetime.datetime.now().year
year = st.selectbox("Select year:", range(current_year - 10, current_year + 11))

months = [calendar.month_name[i] for i in range(1, 13)]
month_name = st.selectbox("Select month:", months)

# Get the calendar for the selected year and month
month_num = list(calendar.month_name).index(month_name)
cal = calendar.monthcalendar(year, month_num)

# Create an empty list to hold the styled days
styled_days = []

# Iterate over each week in the calendar
for week in cal:
    # Create an empty list to hold the styled days for this week
    styled_week = []
    # Iterate over each day in the week
    for day in week:
        # Add the styled day to the list for this week
        styled_week.append(f'<td class="{get_class(day)}">{day}</td>')
    # Add the list of styled days for this week to the overall list
    styled_days.append(styled_week)

# Format the styled days into an HTML table
table_rows = ''
for week in styled_days:
    row = '<tr>'
    for day in week:
        row += day
    row += '</tr>'
    table_rows += row
table = f'<table>{table_rows}</table>'

# Format the days of the week into an HTML row
days_row = '<tr>'
for day in days:
    days_row += f'<th>{day}</th>'
days_row += '</tr>'

# Combine the days of the week and the calendar table into an HTML table
html_table = f'<div>{style}<table>{days_row}{table_rows}</table></div>'

# Display the styled calendar with the days of the week
st.write(html_table, unsafe_allow_html=True)
