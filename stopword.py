from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize.treebank import TreebankWordDetokenizer
detokenizer = TreebankWordDetokenizer()
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
import re
from nltk.stem import SnowballStemmer
snow = SnowballStemmer(language='english')
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
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

def cleancapt(caption):
    word = caption.lower()
    word = re.sub('[^\w\s]', "", str(word))
    word = re.sub('[0-9]+', "", str(word))
    word = re.sub("@\S+", "", str(word))
    word = re.sub("#", "", str(word))
    word = re.sub("\n", " ", str(word))
    word = re.sub("'", " ", str(word))
    tokenized = word_tokenize(word)
    indo_stopword = [word for word in tokenized if not word in stopword_list]
    english_stopword = [word for word in indo_stopword if not word in stopword_listenglish]
    word = [snow.stem(word) for word in english_stopword]
    word = detokenizer.detokenize(word)
    word = stemmer.stem(word)
    word = word.split() 
    word = " ".join(sorted(set(word), key=word.index))
    return word