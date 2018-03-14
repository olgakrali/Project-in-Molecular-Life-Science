import numpy as np
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier

import parsers_windows as pw

path = "Datasets/"


classifier = []
for windows in range(5,37,4):
    protein_ID, sequence, topology, svm2, seconstr, struct_labels = pw.my_par('eval_subset.txt', windows)
    X = np.array(svm2)
    #print(X.shape)
    y = np.array(seconstr)
    #print(y.shape)
    for n_estimators in range(100,400,50):
        for min_samples_split in range(2,10):
            forest = RandomForestClassifier(n_estimators = n_estimators, min_samples_split = min_samples_split, 
            class_weight = 'balanced')
            forest.fit(X,y)
            scores = cross_val_score(forest,X, y, cv=5, verbose=True)
            scores2  = np.average(scores)
            print(scores2)
            classifier.append((windows, n_estimators, min_samples_split, scores2))

print(classifier)
