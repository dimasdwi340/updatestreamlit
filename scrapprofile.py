from scraper import get_data_profile

def get_profile(username):
    data_profile = get_data_profile(username)
    data_profile = data_profile['graphql']['user']
    profile_pic = data_profile['profile_pic_url_hd']
    full_name = data_profile['full_name']
    follower = data_profile['edge_followed_by']['count']
    post_count = data_profile['edge_owner_to_timeline_media']['count']
    is_verified = data_profile['is_verified']
    is_profesional = data_profile['is_professional_account']

    doc = dict(
        username = username,
        profile = profile_pic,
        count_follower = follower,
        post_count = post_count,
        verified = is_verified,
        professional = is_profesional,
        )
    failed = dict (pesan = 'Pengguna tidak dapat ditemukan')
    if data_profile:
        return doc
    else :
        return failed
