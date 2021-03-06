import numpy as np
from sklearn.svm import SVC
import pickle

import parsers_windows as mp

# Train and save my model
path = 'Datasets/'
path2 = 'Saved_models/'

protein_ID, sequences, topology, svm2, seconstr, struct_labels = mp.my_par('test.txt',19)

X = np.array(svm2)
print(X.shape)
y = np.array(seconstr)
print(y.shape)

clfr = SVC(kernel = 'linear', C = 1, gamma = 0.01, cache_size = 3000, class_weight = 'balanced')

clfr.fit(X,y)

pickle.dump(clfr, open(path2 + "SVM_new_model.pkl", "wb"))
