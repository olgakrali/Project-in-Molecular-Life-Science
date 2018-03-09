import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.externals import joblib
from sklearn.metrics import confusion_matrix
from sklearn import preprocessing
import matplotlib.pyplot as plt

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

joblib.dump(clfr, path2 + "my_test.sav")