import os
import PSSM_parsing as ps
from sklearn.ensemble import RandomForestClassifier
import pickle

path = "Datasets/"
path2 = "PSSM/train_final/pssm/"
path3 = "Saved_models/"

fnames = os.listdir(path2)

my_names, new_seq, new_top, struct_labels, X_train, y_train =  ps.my_par(path + "test.txt", fnames, 13, path2)

print(X_train.shape)
print(y_train.shape)

clfr = RandomForestClassifier(n_estimators= 300, min_samples_split = 9, class_weight = 'balanced')

clfr.fit(X_train,y_train)

pickle.dump(clfr, open(path3 + "RFC_PSSM_final.pkl", "wb"))
