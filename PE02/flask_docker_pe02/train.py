#train load library for KNN classifier
from sklearn.neighbors import KNeighborsClassifier

#make up some data
X = [[0], [25], [48], [50], [75], [100]]
y = [0, 0, 0, 1, 1, 1]

clf = KNeighborsClassifier()
clf.fit(X, y)

#save trained classifier as joblib file for server to use
import joblib
joblib.dump(clf, "knn_clf.joblib")