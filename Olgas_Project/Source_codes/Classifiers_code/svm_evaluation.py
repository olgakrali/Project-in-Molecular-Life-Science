import numpy as np
from sklearn.svm import SVC
from sklearn.model_selection import cross_val_score

import mypars as mp

path = "Datasets/"

protein_ID, sequence, topology = mp.my_par('eval_subset.txt')
print(protein_ID)

svm2 = mp.my_windows(35)
X = np.array(svm2)
print(X.shape)

secstr = mp.my_labels()
y = np.array(secstr)
print(y.shape)


kernels = ['linear','rbf','poly']

def floatrange(start, stop, step):
    i = start
    while i < stop:
        yield i
        i += step

classifier = []

for i in range (3,37,2):
    svm2 = mp.my_windows(i)
    X = np.array(svm2)
    print(X.shape)
    for kernel in kernels:
        for C in range(1,10,1):
            for gamma in floatrange(0.01, 0.1, 0.01):
                clfr = SVC(kernel= kernel, C = C, gamma = gamma, cache_size = 3000)
                clfr.fit(X, y)
                score = cross_val_score(clfr, X, y, cv=5, verbose=True)  ####get scores for the train set
                print(score)
                #print(clfr.decision_function(X_train))

                classifier.append((i,kernel,C,gamma,clfr,score))
print(classifier)

# Save my results on a txt file

my_file = open(path + "eval_out.txt")
for item in classifier:
    my_file.write("%s \n" % item)