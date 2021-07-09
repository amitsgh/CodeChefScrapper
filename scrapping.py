import altair as alt
import pandas as pd
import requests
import streamlit as st
import urllib

from bs4 import BeautifulSoup
from time import sleep

def get_user_url(username):
    url = 'https://www.codechef.com/users/{}'.format(username)
    return url

def get_user_data(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    sleep(2)
    code_chef_name = soup.find("h1", attrs={'class': 'h2-style'}).text
    overall_rating = soup.find("div", attrs={'class': 'rating-number'}).text
    ratings = soup.find('table', attrs={'class': 'rating-table'}).findAll('td')
    long_rating = ratings[1].text
    cookoff_rating = ratings[5].text
    lunch_rating = ratings[9].text
    st.write("Code Chef Rating ")
    st.write(pd.DataFrame(
        {
            'Long Challenge' : [long_rating],
            'Cook Off' : [cookoff_rating],
            'Lunch Time' : [lunch_rating],
            'Overall Rating' : [overall_rating]
        },
        index=[code_chef_name],
    ))
    

try:
    st.title("""Code Chef User's Data""")
    
    st.write("### Enter Username")
    username = st.text_input(label="", )
    
    if not username:
        st.error("Please enter a username.")
    else:
        url = get_user_url(username)
        get_user_data(url)
        
except urllib.error.URLError as e:
    st.error(
        """
        **This demo requires internet access.**
        Connection error: %s
    """
        % e.reason
    )
    
