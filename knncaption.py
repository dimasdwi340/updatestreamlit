from koneksi_db.koneksi import db
# from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import TfidfVectorizer
from knn_class import KNN_NLC_Classifier
# from sklearn.neighbors import KNeighborsClassifier
import numpy as np
from sklearn import metrics, neighbors
# from sklearn.model_selection import train_test_split
# from sklearn.feature_extraction.text import CountVectorizer
# import vectorize

col = db['caption']
dataa = col.find()

X = []
y = []
# le=LabelEncoder()
def caption_knn(caption):
    for data in dataa:
        X.append(data['caption'])
        y.append(data['label'])
    
    # classifier = KNN_NLC_Classifier(k=1, distance_type='path')
    # classifier.fit(X, y)
    # predict = classifier.predict(caption)
    # print (predict)
    # vectorizer = CountVectorizer(analyzer='word', input='content')
    # X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=5)
    # X_train, X_test = vectorize.createTFIDF(X_train, X_test, remove_stopwords=True, lemmatize=True, stemmer=False)
    # knn = neighbors.KNeighborsClassifier(n_neighbors=7, weights='distance', algorithm='brute', leaf_size=30, p=2,
    #                                         metric='cosine', metric_params=None, n_jobs=1)
    # caption = vectorizer.transform(caption)
    # knn.fit(X_train, y_train)
    # predicted = knn.predict(caption)
    # return predicted
    # acc = metrics.accuracy_score(y_test, predicted)
    # print('KNN with TFIDF accuracy = ' + str(acc * 100) + '%')
    vectorizer = TfidfVectorizer(analyzer='word', ngram_range=(1,4),
                        min_df = 0, stop_words = 'english', sublinear_tf=True)
    response = vectorizer.fit_transform(X)
    classes = y
    # print ("data test : ",response)
    # print (len(X))
    caption = [caption]
    # caption = np.array(caption) 
    caption = vectorizer.fit_transform(caption)
    
    # # print ("Caption : ",caption)
    clf = neighbors.KNeighborsClassifier(n_neighbors=7)
    clf.fit(response, classes)
    clf.predict(caption)
    # print (response.shape, caption.shape)

caption_knn('kabar gembira korea lata wisatawan indonesia syarat lengkap visa korea keta hasil tes pcr negatif tes pcr korea selatan daftar qcode dokumen syarat lengkap libur korea selatan oiya libur hemat kode promo tampaninter terbang rute internasional backpackstay hotel todobackpacker tiketcom ayoo rencana libur tiketcom tiketcom bulat tiket korea korsel koreaselatan southkorea traveler backpacker adventure indonesian travellife')