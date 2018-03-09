import numpy as np
from sklearn.svm import SVC
from sklearn.model_selection import cross_val_score

import parsers_windows as mp

path = "Datasets/"

protein_ID, sequence, topology,svm2,seconstr = mp.my_par('eval_subset.txt', 19)
print(protein_ID)

X = np.array(svm2)
print(X.shape)

y = np.array(seconstr)
print(y.shape)



def floatrange(begin, end, steps):
    i = begin
    while i < end:
        yield i
        i += steps

classifier = []


for C in range(1,10,1):
    for gamma in floatrange(0.01, 0.1, 0.02):
        clfr = SVC(kernel= 'linear', C = C, gamma = gamma, cache_size = 3000)
        clfr.fit(X, y)
        score = cross_val_score(clfr, X, y, cv=5, verbose=True)  ####get scores for the train set
        print(score)
        #print(clfr.decision_function(X_train))
        classifier.append((C,gamma,clfr,score))
print(classifier)

