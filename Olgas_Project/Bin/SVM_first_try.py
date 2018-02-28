
from feature_label_inputSVM_multipleSeq import *  # import the python file with the input in module form

from sklearn.svm import SVC
from sklearn.model_selection import cross_val_score
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier

########## The input is a set of multiple proteins merged into a X array of binary windows and the y is the sequences' topologies

############################ SVM ###############


####### Running SVM classification

print("Classifier fitting to training set")

clfr = SVC(gamma = 0.01, C =1)

clfr.fit(X,y)


score = cross_val_score(clfr, X, y, cv = 5, verbose = True)  ####get scores for the train set
print(score)

##### Predict the same data just to check if the SVM is actually accurate
(print("Predict the topology of each window on the same set of data"))

predictions = clfr.predict(X)  ### how well can the SVM predict our data?
print(predictions)   ##### it returns predicted values for the topologies (1-3)
print(clfr.score(X, y))  ## score for svm predictions over test set

plt.scatter(y, predictions)

plt.xlabel('True values')
plt.ylabel('Predicted values')
plt.show()          ###Visualizing the true values versus the predictions



# #####Random forest classifier

from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier(max_depth = 2, random_state = 0)
clf.fit(X, y)
print(clf.feature_importances_)
print(clf.predict(X))
print(clf.score(X, y))
