from unittest import result
from jmespath import search
import streamlit as st
from Pages.landing import *
from Pages.search import *
from Pages.result import *
from Pages.hasilscrap import *


st.session_state.update(st.session_state)

if 'active_page' not in st.session_state:
    st.session_state.active_page = 'Landing'
    st.session_state.Search = 0
    st.session_state.result = False

def CB_Landing():
    st.session_state.active_page = 'Landing'
def CB_Search():
    st.session_state.active_page = 'Search'
def CB_Result():
    st.session_state.active_page = 'Result'
def CB_Result():
    st.session_state.active_page = 'Hasilscrap'

st.set_page_config(page_title="InSona - Temukan Influencermu!", page_icon="🏠", layout="wide")
with st.container():
    st.title("""
    InSona
    ---""")     

if   st.session_state.active_page == 'Landing':
    landing()
elif st.session_state.active_page == 'Search':
    search()
elif st.session_state.active_page == 'Result':
    result()
elif st.session_state.active_page == 'Hasilscrap':
    result()


