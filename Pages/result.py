import streamlit as st
from scrapper.scrapprofile import get_data_profile
from search import username
# from koneksi_db.koneksi_result import items

# def result():
#     for item in items:
#         username = item['username']
#         url = "https://instagram.fcgk37-1.fna.fbcdn.net/v/t51.2885-19/295762345_802883051085590_3738799248734909166_n.jpg?stp=dst-jpg_s320x320&_nc_ht=instagram.fcgk37-1.fna.fbcdn.net&_nc_cat=1&_nc_ohc=o5ULfVEDRxEAX81--oa&edm=ABfd0MgBAAAA&ccb=7-5&oh=00_AT-dnRD7zK63Ts-0aV1YrVAyNJfQcModJAenQ2dXrPhJMw&oe=630ACCE9&_nc_sid=7bff83"
#         # url = item['url_profile_pict']
#         post_count = item['post_count']
#         follower = item['follower']
#         biography = item['biography']
#         category_name = item['category_name']
#         fullname = ['full_name']
#         persona = ['persona']

#     if persona == "traveller":
#         persona_acc = "Travel Blogger"
#     else:
#         persona_acc = "Unknown"

#     with st.container():
#         left,center1, center2, right = st.columns((1,1,1,1))
#         with left:
#             st.image(url, width=200)
#         with center1:
#             with st.container():
#                 st.write(f"""
#                 Username :\n
#                 ## {username}""")
#                 st.write(f"""
#                 ###### {category_name}""")
#         with center2:
#             st.write(f"""
#             Post :
#             ## {post_count}""")
#         with right:
#             st.write(f"""
#             Followers :\n 
#             ## {follower}""")

#     with st.container():
#         left, center,right = st.columns((1,2,1))
#         with center:
#             st.write("""
#             Author⁣ - Content creator⁣ - Storygrapher⁣ \n
#             #LetMeTellYouAStory about how I see the world 😗
#             """)

#     with st.container():
#         st.write(f"""#### Talent kamu adalah seorang Travel Blogger, dengan jumlah followers sebanyak {follower} dan sudah membagikan sejumlah {post_count} postingan. Talent kamu termasuk "Macro Influencers" yang cenderung memiliki audiens yang beragam dengan minat yang beragam.""")


with st.container():
    left,center, right = st.columns(1,2,1)
    with center: 
        profile = get_data_profile(username)
        st.write (profile)
