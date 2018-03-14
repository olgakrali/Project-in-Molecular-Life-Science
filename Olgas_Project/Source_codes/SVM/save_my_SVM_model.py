import numpy as np
from sklearn.svm import SVC
import pickle

import parsers_windows as mp

# Train and save my model
path = 'Datasets/'
path2 = 'Saved_models/'

protein_ID, sequences, topology, svm2, seconstr, struct_labels = mp.my_par('60_prot.txt',19)

X = np.array(svm2)
print(X.shape)
y = np.array(seconstr)
print(y.shape)

clfr = SVC(kernel = 'linear', C = 1, gamma = 0.01, cache_size = 3000)

clfr.fit(X,y)

pickle.dump(clfr, open(path2 + "my_test.pkl", "wb"))
