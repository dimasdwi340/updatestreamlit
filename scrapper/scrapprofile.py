from scraper import get_data_profile
from stopword import stopword
# import re
import string
# from nltk.tokenize import word_tokenize
# from nltk.tokenize.treebank import TreebankWordDetokenizer
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

factory = StemmerFactory()
stemmer = factory.create_stemmer()

punct = set(string.punctuation)

data_info = []
data_bio = []
# bigdata_caption = []
# datacaption = []
# list_caption = []

f = open("tala-stopwords-indonesia.txt", "r")
stopword_list = []
for line in f:
    stripped_line = line.strip()
    line_list = stripped_line.split()
    stopword_list.append(line_list[0])
f.close()

e = open("stopword-english.txt", "r")
stopword_listenglish = []
for line in e:
    stripped_line = line.strip()
    line_list = stripped_line.split()
    stopword_listenglish.append(line_list[0])
e.close()


def word_count(str):
    counts = dict()
    words = str.split()
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

def get_profile(username):
    data_profile = get_data_profile(username)
    # data_profile = data_profile['seo_category_infos']
    # data_profile = data_profile['graphql']['show_view_shop']
    data_profile = data_profile['graphql']['user']
    username = data_profile['username']
    # username = stopword(username)
    full_name = data_profile['full_name']
    full_name = stopword(full_name)
    follower = data_profile['edge_followed_by']['count']
    following = data_profile['edge_follow']['count']
    post_count = data_profile['edge_owner_to_timeline_media']['count']
    category_name = data_profile['category_name']
    biography = data_profile['biography']
    # stopwordbiography = stopword(biography)
    is_verified = data_profile['is_verified']
    is_profesional = data_profile['is_professional_account']
    data_bio.append(stopword(biography))
    # # data_media_photo = data_profile['edge_owner_to_timeline_media']['edges']
    # # data_media_video = data_profile['edge_felix_video_timeline']['edges']
    
    # #datalike = []
    # #datacomment= []
    # #jumlah_kata = []
    # label = []

    # for data_caption in range (len(data_media_photo)):
    #     # caption = data_media_photo[data_caption]['node']['edge_media_to_caption']['edges'][0]['node']['text']
    #     # caption = stopword(caption)
    #     # caption = caption.lower()
    #     # caption = re.sub("@\S+", "", str(caption))
    #     # caption = re.sub('[^\w\s]', "", str(caption))
    #     # caption = re.sub('[0-9]+', "", str(caption))
    #     # caption = re.sub("#", "", str(caption))
    #     # caption = re.sub("\n", " ", str(caption))
    #     # caption = "".join([ch for ch in caption if ch not in punct])
    #     # caption_tokenized = word_tokenize(caption)
    #     # caption_stopword = [word for word in caption_tokenized if not word in stopword_list]
    #     # captionfiltered_english = [word for word in caption_stopword if not word in stopword_listenglish]
    #     # #caption = lemma.lemmatize(caption)
    #     # caption = TreebankWordDetokenizer().detokenize(captionfiltered_english)
    #     # caption = stemmer.stem(caption)
    #     # count_comment = data_media_photo[data_caption]['node']['edge_media_to_comment']['count']
    #     # count_like = data_media_photo[data_caption]['node']['edge_liked_by']['count']
    #     # datalabel = ""
    #     #date = data_media_photo[data_caption]['node']['taken_at_timestamp']
    #     #date = datetime.fromtimestamp(date)
    #     #data = {'caption' : caption, 'comment_count' : count_comment, 'like_count' : count_like, 'date' : date}
    #     #post = {'post' : data}
    #     #media_data_photo.update(data)
    #     # datacaption.append(caption)
    #     # datalike.append(count_like)
    #     # datacomment.append(count_comment)
    #     # label.append(datalabel)

    # for data_caption in range (len(data_media_video)):
    #     caption = data_media_video[data_caption]['node']['edge_media_to_caption']['edges'][0]['node']['text']
    #     caption = stopword(caption)
    #     # caption = str(caption).lower()
    #     # caption = re.sub("@\S+", "", str(caption))
    #     # caption = re.sub(r'[^\w\s]', "", str(caption))
    #     # caption = re.sub(r'[0-9]+', "", str(caption))
    #     # caption = re.sub("#", "", str(caption))
    #     # caption = re.sub("\n", " ", str(caption))
    #     # caption = "".join([ch for ch in caption if ch not in punct])
    #     # caption_tokenized = word_tokenize(caption)
    #     # caption_stopword = [word for word in caption_tokenized if not word in stopword_list]
    #     # captionfiltered_english = [word for word in caption_stopword if not word in stopword_listenglish]
    #     # #caption = lemma.lemmatize(caption)
    #     # caption = TreebankWordDetokenizer().detokenize(captionfiltered_english)
    #     # caption = stemmer.stem(caption)
    #     # count_comment = data_media_video[data_caption]['node']['edge_media_to_comment']['count']
    #     # count_like = data_media_video[data_caption]['node']['edge_liked_by']['count']
    #     # datalabel = ""
    #     #date = data_media_video[data_caption]['node']['taken_at_timestamp']
    #     # datacaption.append(caption)
    #     # datalike.append(count_like)
    #     # datacomment.append(count_comment)
    #     # label.append(datalabel)
    #     #date = datetime.fromtimestamp(date)
    #     #data = {'caption' : caption, 'comment_count' : count_comment, 'like_count' : count_like, 'date' : date}
    #     #post = {f'post{data_caption}' : data}
    #     #media_data_video.update(data)

    doc = dict(
        # caption = datacaption,
        # like = datalike,
        # comment = datacomment,
        username = username,
        fullname = full_name,
        count_follower = follower,
        post_count = post_count,
        categoryname = category_name,
        bio = biography,
        verified = is_verified,
        professional = is_profesional,
        label = 1
        # dataprofile = data_profile
        )
    data_info.append(doc)
    # bigdata_caption.append(datacaption)
    return doc

    #print (word_count (datacaption))

    # print (doc)

    # with open(f'new_dataset_financial/{username}.json', 'w') as g:
    #     json.dump(doc, g)
    # if doc: #if success 
    #     return True
    # else:
    #     return None

    # with open('test.csv', 'w') as f:
    #     #for key in doc.keys():
    #         #f.write("%s, %s\n" % (key, doc[key]))
    #         writer = csv.DictWriter(f, fieldnames = data_info)
    #         writer.writeheader()
    #         writer.writerows(doc)
# def make_excel ():
#     doc = get_profile()
    
#     jumlah = word_count(str(big_caption))
#     df2 = pd.DataFrame(data = jumlah, index = [0]) 
#     df2 = (df2.T)
#     df2.to_excel ('count.xlsx')
#     if doc:
#         return True
#     else:
#         return None

# get_profile('anyageraldine')
