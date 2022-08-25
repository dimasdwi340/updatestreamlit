import requests
import browser_cookie3

def get_related(username):
    cookiejar = browser_cookie3.firefox(domain_name='instagram.com')
    data = requests.get(f'https://www.instagram.com/{username}/?__a=1', cookies = cookiejar).json()
    return data

def get_data_profile(username):
    cookiejar = browser_cookie3.opera(domain_name='instagram.com')
    data = requests.get(f'https://www.instagram.com/{username}/?__a=1&__d=dis', cookies = cookiejar).json()
    return data

# get_related('anyageraldine')
# get_data_profile('anyageraldine')   