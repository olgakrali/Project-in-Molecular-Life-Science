import numpy as np
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier

import parsers_windows as pw

path = "Datasets/"


classifier = []
for windows in range(5,37,4):
    protein_ID, sequence, topology, svm2, seconstr, struct_labels = pw.my_par('eval_subset.txt', windows)
    X = np.array(svm2)
    #print(X.shape)
    y = np.array(seconstr)
    #print(y.shape)
    for min_samples_split in range(2,10):
        tree =  DecisionTreeClassifier(min_samples_split = min_samples_split)
        tree.fit(X,y)
        scores = cross_val_score(tree, X, y, cv = 5, verbose = True)
        scores2  = np.average(scores)
        print(scores2)
        classifier.append((windows,min_samples_split,scores2))
print(classifier)
