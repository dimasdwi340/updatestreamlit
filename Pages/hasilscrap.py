# import sys 
# sys.path.append ("..")
import streamlit as st
from scrapper.scrapprofile import get_profile
from search import username

def hasilscrap():
    with st.container():
        left,center, right = st.columns(1,2,1)
        with center:   
            profile = get_profile(username)
            st.write (profile)

if __name__=='__main__':
    hasilscrap()