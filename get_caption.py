from scraper import get_data_profile
from stopword import stopword
from knncaption import caption_knn
import re
import string

def get_caption (username) :
    data_caption = get_data_profile(username)
    data_profile = data_caption['graphql']['user']
    data_media_photo = data_profile['edge_owner_to_timeline_media']['edges']
    data_media_video = data_profile['edge_felix_video_timeline']['edges']
    
    for data_caption in range (len(data_media_photo)):
        caption = data_media_photo[data_caption]['node']['edge_media_to_caption']['edges'][0]['node']['text']
        caption = stopword(caption)
        caption_photo = caption_knn(caption)
        print (caption_photo)

get_caption('anyageraldine')