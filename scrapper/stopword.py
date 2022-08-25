from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize.treebank import TreebankWordDetokenizer
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
import re

factory = StemmerFactory()
stemmer = factory.create_stemmer()

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

# caption = "i mau makan di boleh lengkap ikut the lafayete point sama u pilih, ga peduli  bal with they oligarki, temanteman"
# caption = re.sub('[^\w\s]', "", str(caption))
# caption = re.sub('[0-9]+', "", str(caption))
# caption_tokenized = word_tokenize(caption)
# caption_stopword = [word for word in caption_tokenized if not word in stopword_list]
# captionfiltered_english = [word for word in caption_stopword if not word in stopword_listenglish]
#         #caption = lemma.lemmatize(caption)
# caption = TreebankWordDetokenizer().detokenize(captionfiltered_english)

# print (caption)

def stopword(caption):
    caption = caption.lower()
    caption = re.sub('[^\w\s]', "", str(caption))
    caption = re.sub('[0-9]+', "", str(caption))
    caption = re.sub("@\S+", "", str(caption))
    caption = re.sub("#", "", str(caption))
    caption = re.sub("\n", " ", str(caption))
    caption = re.sub("'", " ", str(caption))
    caption = stemmer.stem(caption)
    caption_tokenized = word_tokenize(caption)
    caption_stopword = [word for word in caption_tokenized if not word in stopword_list]
    caption_stopword = stopwords(caption_stopword)
    captionfiltered_english = [word for word in caption_stopword if not word in stopword_listenglish]

    #caption = lemma.lemmatize(caption)
    caption = TreebankWordDetokenizer().detokenize(captionfiltered_english)
    return caption