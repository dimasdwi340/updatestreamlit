import streamlit as st
from koneksi_db.koneksi import db
# import util
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
from scrapprofile import get_profile
# from sklearn import metrics, neighbors
# from sklearn.model_selection import train_test_split, cross_val_score, cross_val_predict
# import vectorize

username = st.text_input("")
cari = st.button("🕵️Cari")
# scrap = st.button("scrap cepat!")
if cari or username:
    data_profile = get_profile(username)
    # st.image (data_profile('profile'))
    st.write (data_profile)

    col= db["influencer"]
    dataa = col.find()
    # x = '{0} {1}'.format(dataa['_id'], dataa['fullname'], dataa['count_follower'], dataa['post_count'], dataa['category_name'], dataa['verified'], dataa['professional'])
    # y = ({},{'_id': 0, 'label': 1})
    X = []
    y = []
    le=LabelEncoder()

    for data in dataa:
        para = [[int(data['count_follower'])], [int(data['post_count'])], [int(data['verified'])], [int(data['professional'])]]
        para = X.append(para)
        label = y.append(data['label'])
        print (y)

    # y = le.fit_transform(y)

    # print(len(X))
    # print(len(y))

    # data = util.get_parser_data('profile.xlsx')

    # print (data['bio'])
    # st.write (X.groupby('label'.size()))
    X = np.array(X)
    X = X.reshape(X.shape[0], -1)

    neigh = KNeighborsClassifier(n_neighbors=3)
    neigh.fit(X, y)
    # print (X)

    data_parameter = [[data_profile["count_follower"], data_profile["post_count"], data_profile["verified"], data_profile["professional"]]]
    coba = np.array(data_parameter)
    coba = coba.reshape(coba.shape[0], -1)
    # print (coba)

    # print (X.shape, coba.shape)
    st.write (neigh.score(X, y, sample_weight=None))
    st.write (neigh.predict(coba))
    store = dict(
        count_follower = data_profile["count_follower"],
        post_count = data_profile['post_count'],
        verified = data_profile["verified"], 
        professional = data_profile["professional"]
    )
    insert = col.insert_one(store)