import numpy as np
from sklearn import metrics
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.datasets import fetch_20newsgroups
rdata=fetch_20newsgroups()

print(rdata.target_names)
count_vect=CountVectorizer()
rdata_count=count_vect.fit_transform(rdata.data)

tfidf_data=TfidfTransformer()
rdata_tfidf=tfidf_data.fit_transform(rdata_count)



from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(rdata_tfidf,rdata.target,test_size=0.20)

clf=MultinomialNB().fit(x_train,y_train)
predicted=clf.predict(x_test)

print("accuracy := ",np.mean(predicted==y_test))
print(metrics.accuracy_score(predicted,y_test))
print(metrics.confusion_matrix(predicted,y_test))
print(metrics.classification_report(predicted,y_test,target_names=rdata.target_names))




