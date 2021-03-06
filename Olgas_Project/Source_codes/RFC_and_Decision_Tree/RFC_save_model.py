import numpy as np
from sklearn.ensemble import RandomForestClassifier
import pickle


import parsers_windows as mp

# Train and save my model
path = "Saved_models/"

protein_ID, sequences, topology, svm2, seconstr, struct_labels = mp.my_par('test.txt', 13)

X_train = np.array(svm2)
print(X_train.shape)
y_train = np.array(seconstr)
print(y_train.shape)

clfr = RandomForestClassifier(n_estimators= 300, min_samples_split = 9, class_weight = 'balanced')

clfr.fit(X_train,y_train)

pickle.dump(clfr, open(path + "RFC_final.pkl", "wb"), protocol = -1)
