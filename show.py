import streamlit as st
from koneksi_db.koneksi import db
import util

col= db["profil"]
dataa = col.find()
# x = '{0} {1}'.format(dataa['_id'], dataa['fullname'], dataa['count_follower'], dataa['post_count'], dataa['category_name'], dataa['verified'], dataa['professional'])
y = ({},{'_id': 0, 'label': 1})

for data in dataa:
    x = '{1} {1} {1} {1}'.format(data['count_follower'], data['post_count'], data['verified'], data['professional'])
    y = (data['label'])
    print(y)

# data = util.get_parser_data('profile.xlsx')

# print (data['bio'])