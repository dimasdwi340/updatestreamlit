import streamlit as st
from streamlit_lottie import st_lottie
from scrapprofile import get_profile
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
            if cari or username:
                data = get_profile(username)
                if data:
                    with st.container():
                        left,center1, center2, right = st.columns((1,1,1,1))
                        with left:
                            st.image("https://scontent-sin6-1.cdninstagram.com/v/t51.2885-19/295762345_802883051085590_3738799248734909166_n.jpg?stp=dst-jpg_s320x320&_nc_ht=scontent-sin6-1.cdninstagram.com&_nc_cat=1&_nc_ohc=Bpkg2qthnqcAX_Py4zZ&edm=ABfd0MgBAAAA&ccb=7-5&oh=00_AT96V6vhBHcNdHTPCJXyzyIIyKovVReFgqzhsljheTmukA&oe=630EC169&_nc_sid=7bff83", width=200)
                        with center1:
                            with st.container():
                                st.write(f"""
                                Fullname :\n
                                ## {data["fullname"]}""")
                                st.write(f"""
                                ###### {data["categoryname"]}""")
                        with center2:
                            st.write(f"""
                            Post :
                            ## {data["post_count"]}""")
                        with right:
                            st.write(f"""
                            Followers :\n 
                            ## {data["count_follower"]}""")

                    with st.container():
                        left, center,right = st.columns((1,2,1))
                        with center:
                            st.write(f"""
                            {data["bio"]}
                            """)
                else:
                    st.write("Mohon maaf, pengguna tidak dapat ditemukan")


search()
