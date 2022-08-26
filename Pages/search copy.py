import streamlit as st
from scrapprofile import get_profile
with st.container():
    username = st.text_input("")
    scrap = st.button("cari")

if scrap or username:
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

