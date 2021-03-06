import os
import PSSM_parsing as ps
from sklearn.tree import DecisionTreeClassifier
import pickle
path = "Datasets/"
path2 = "PSSM/train_final/pssm/"
path3 = "Saved_models/"

fnames = os.listdir(path2)

my_names, new_seq, new_top, struct_labels, X_train, y_train =  ps.my_par(path + "test.txt", fnames, 21, path2)

print(X_train.shape)
print(y_train.shape)

clfr = DecisionTreeClassifier(min_samples_split = 2, class_weight = 'balanced')

clfr.fit(X_train,y_train)

pickle.dump(clfr, open(path3 + "Decision_tree_PSSM_final.pkl", "wb"))
