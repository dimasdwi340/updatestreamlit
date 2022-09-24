from koneksi_db.koneksi import db
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfTransformer
import gensim
from get_caption import get_caption


col = db['caption']
dataa = col.find()
vectorizer = TfidfVectorizer(analyzer = 'word', stop_words = 'english')
count_vect = CountVectorizer()

def classification_caption (username):
    X = []
    y = []
    for data in dataa:
        X.append(data['caption'])
        y.append(data['label'])
    X_train_counts = count_vect.fit_transform(X)
    X_train_counts.shape
    tf_transformer = TfidfTransformer(use_idf=False).fit(X_train_counts)
    X_train_tf = tf_transformer.transform(X_train_counts)
    X_train_tf.shape
    clf = MultinomialNB().fit(X_train_tf, y)
    list_capt = get_caption(username)
    X_new_counts = count_vect.transform(list_capt)
    X_new_tfidf = tf_transformer.transform(X_new_counts)
    predicted = clf.predict(X_new_tfidf)
    return predicted



