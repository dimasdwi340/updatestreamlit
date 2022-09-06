from koneksi_db.koneksi import db
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
from sklearn import metrics, neighbors
from sklearn.model_selection import train_test_split, cross_val_score, cross_val_predict
import vectorize

col = db['caption']
dataa = col.find()

X = []
y = []
le=LabelEncoder()
def caption_knn(caption):
    for data in dataa:
        # print (data['caption'])
        para = X.append(data['caption'])
        label = y.append(data['label'])

    # X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=5)
    # X_train, X_test = vectorize.createBagOfWords(X_train, X_test, remove_stopwords=True, lemmatize=True, stemmer=False)
    # knn = neighbors.KNeighborsClassifier(n_neighbors=5, weights='uniform', algorithm='auto', leaf_size=30, p=2, metric='jaccard', metric_params=None, n_jobs=1)

    # knn.fit(X_train, y_train)
    # predicted = knn.predict(X_test)
    # acc = metrics.accuracy_score(y_test, predicted)
    # print('KNN with BOW accuracy = ' + str(acc * 100) + '%')

    # scores = cross_val_score(knn, X_train, y_train, cv=3)
    # print("Cross Validation Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))
    # print(scores)
    # print('\n')

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=5)
    X_train, X_test = vectorize.createTFIDF(X_train, X_test, remove_stopwords=True, lemmatize=True, stemmer=False)
    knn = neighbors.KNeighborsClassifier(n_neighbors=7, weights='distance', algorithm='brute', leaf_size=30, p=2,
                                            metric='cosine', metric_params=None, n_jobs=1)

    knn.fit(X_train, y_train)
    predicted = knn.predict(caption)
    return predicted
    # acc = metrics.accuracy_score(y_test, predicted)
    # print('KNN with TFIDF accuracy = ' + str(acc * 100) + '%')

    # scores = cross_val_score(knn, X_train, y_train, cv=3)
    # print("Cross Validation Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))
    # print(scores)