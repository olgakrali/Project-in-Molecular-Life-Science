import numpy as np
from sklearn.svm import SVC
from sklearn.model_selection import cross_val_score

import parsers_windows as pw

path = "Datasets/"




classifier = []

for windows in range (3,37,4):
    protein_ID, sequence, topology, svm2, seconstr, struct_labels = pw.my_par('eval_subset.txt', windows)
    X = np.array(svm2)
    print(X.shape)
    y = np.array(seconstr)
    print(y.shape)
    clfr = SVC(kernel='linear', cache_size=3000)
    clfr.fit(X, y)
    score = cross_val_score(clfr, X, y, cv=5, verbose=True)
    print(score)
    # print(clfr.decision_function(X_train))
    classifier.append((windows, clfr, score))
print(classifier)


