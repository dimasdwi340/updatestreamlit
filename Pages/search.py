import streamlit as st
from streamlit_lottie import st_lottie
# from streamlit import caching
import requests

def search():

    def load_lottieurl(url):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()

    lottie_coding = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_f74ijzbr.json")

    with st.container():
        st.write("""
                <h2 style='text-align: center;'>
                Cari tau yuk!
                </h2>""", unsafe_allow_html=True)
        st_lottie(lottie_coding, height = 300, key = "home")

    with st.container():
        left, center, right = st.columns((1,2,1))
        with center:
            username = st.text_input("")
            cari = st.button("🕵️Cari")
            scrap = st.button("scrap cepat!")
            if cari:
                st.session_state.active_page = 'Result'
            if scrap:
                st.session_state.active_page = 'Hasilscrap'