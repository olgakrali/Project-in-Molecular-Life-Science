import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.externals import joblib


import parsers_windows as mp

# Train and save my model
path = "Datasets/"
path2 = "Saved_models/"

protein_ID, sequences, topology, svm2, seconstr, struct_labels = mp.my_par('60_prot.txt',5)

X_train = np.array(svm2)
print(X_train.shape)
y_train = np.array(seconstr)
print(y_train.shape)

clfr = RandomForestClassifier(n_estimators= 300, min_samples_split = 3)

clfr.fit(X_train,y_train)

joblib.dump(clfr, path2 + "RFC.sav")