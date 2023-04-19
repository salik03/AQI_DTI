import streamlit as st
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select



# Set Streamlit title and page configuration
st.set_page_config(page_title="Pollution News", page_icon=":newspaper:", layout="wide")

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Set Streamlit app header
st.title("Pollution News")

# Instantiate Chrome WebDriver in headless mode
options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

# Access the website
driver.get('https://www.indiatvnews.com/topic/weather')

# Find the news items using CSS selectors
news_items = driver.find_elements(By.CSS_SELECTOR, "div.row.newsListBox")

# Create an empty list to store the news items
news = []

# Extract the headlines, news descriptions, day and date-time of the news items, images, and URLs and store them in the list
for item in news_items:
    headline = item.find_elements(By.CSS_SELECTOR,"h3.title")
    newsdesc = item.find_elements(By.CSS_SELECTOR,"p.dic")
    daydatetime = item.find_elements(By.CSS_SELECTOR,"span.deskTime")
    image = item.find_elements(By.CSS_SELECTOR,"img")
    news_url = item.find_elements(By.CSS_SELECTOR,"a.thumb")
    for i in range(len(headline)):
        news.append({"headline":headline[i].text,
                     "newsdesc":newsdesc[i].text,
                     "daydatetime":daydatetime[i].text,
                     "image":image[i].get_attribute("data-original"),
                     "news_url":news_url[i].get_attribute("href")})

# Close the Chrome WebDriver
driver.quit()

# Display the news items as a table or list using Streamlit's "st" functions
if len(news) == 0:
    st.warning("No news found.")
else:
    for i, item in enumerate(news):
        st.write(f"**{i+1}. {item['headline']}**")
        st.write(f"{item['newsdesc']}")
        st.write(f"Published: {item['daydatetime']}")
        st.image(item['image'])
        st.write(f"URL: {item['news_url']}")
        st.write("")
        
# Set Streamlit app footer
st.write("Powered by Selenium WebDriver and Streamlit.")
