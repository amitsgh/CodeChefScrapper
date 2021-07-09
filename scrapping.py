import altair as alt
import pandas as pd
import requests
import streamlit as st
import urllib

from bs4 import BeautifulSoup
from time import sleep

@st.cache
def get_user_url(username):
    base_url = "https://www.codechef.com/"
    url = base_url + username
    return url

def get_user_data(url):
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, features='lxml')
    sleep(2)
    code_chef_name = soup.find("h1", attrs={'class': 'h2-style'}).text
    overall_rating = soup.find("div", attrs={'class': 'rating-number'}).text
    ratings = soup.find('table', attrs={'class': 'rating-table'}).findAll('td')
    long_rating = ratings[1].text
    cookoff_rating = ratings[5].text
    lunch_rating = ratings[9].text
    st.write("Code Chef rating of", code_chef_name)
    st.write(pd.DataFrame(
    {
    'first column' : [long_rating],
    'second column' : [cookoff_rating],
    'third column' : [lunch_rating],
    'fourth column' : [overall_rating]
    }
    ))
    

try:
    st.title(
        """
        Code Chef User's Data
        """
    )
    st.write("### Enter Username")
    username = st.text_input(label="", )
    if not username:
        st.error("Please enter a username.")
    else:
        st.write(" #### Fetching data...")
        url = get_user_url(username)
        get_user_data(url)
        
        # st.write("###  user's data ", data.sort_index())
        # data = data.T.reset_index()
        # data = pd.melt(data, id_vars=["index"]).rename(
        #     columns={"index": "year", "value": "Gross Agricultural Product ($B)"}
        # )
        # chart = (
        #     alt.Chart(data)
        #     .mark_area(opacity=0.3)
        #     .encode(
        #         x="year:T",
        #         y=alt.Y("Gross Agricultural Product ($B):Q", stack=None),
        #         color="Region:N",
        #     )
        # )
        # st.altair_chart(chart, use_container_width=True)
        
except urllib.error.URLError as e:
    st.error(
        """
        **This demo requires internet access.**
        Connection error: %s
    """
        % e.reason
    )
    
