import streamlit as st
from koneksi_db.koneksi import db
# import util
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
# from sklearn import metrics, neighbors
# from sklearn.model_selection import train_test_split, cross_val_score, cross_val_predict
# import vectorize

col= db["profil"]
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
    # print (y)

# y = le.fit_transform(y)

# print(len(X))
# print(len(y))

# data = util.get_parser_data('profile.xlsx')

# print (data['bio'])
X = np.array(X)
X = X.reshape(X.shape[0], -1)

neigh = KNeighborsClassifier(n_neighbors=3)
neigh.fit(X, y)
# print (X)

coba = [[[250], [34985], [1], [1]]]
coba = np.array(coba)
coba = coba.reshape(coba.shape[0], -1)
# print (coba)

# print (X.shape, coba.shape)
print (neigh.score(X, y, sample_weight=None))
# print (neigh.predict(coba))