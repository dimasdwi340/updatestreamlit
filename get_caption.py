from scraper import get_data_profile
from stopword import cleancapt


def get_caption (username) :
    capt2doc = []
#     lab2doc = []
    data_caption = get_data_profile(username)
    data_profile = data_caption['graphql']['user']
    data_media_photo = data_profile['edge_owner_to_timeline_media']['edges']
    data_media_video = data_profile['edge_felix_video_timeline']['edges']
    
    for data_caption in range (len(data_media_photo)):
        caption = data_media_photo[data_caption]['node']['edge_media_to_caption']['edges'][0]['node']['text']
        caption = cleancapt(caption)
        capt2doc.append(caption)
    for data_caption in range (len(data_media_video)):
        caption = data_media_photo[data_caption]['node']['edge_media_to_caption']['edges'][0]['node']['text']
        caption = cleancapt(caption)
        capt2doc.append(caption)
    return capt2doc
