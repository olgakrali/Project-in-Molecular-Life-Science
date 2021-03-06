import os
import PSSM_parsing as ps
from sklearn.svm import SVC
import pickle
path = "Datasets/"
path2 = "PSSM/train_final/pssm/"
path3 = "Saved_models/"

fnames = os.listdir(path2)

my_names, new_seq, new_top, struct_labels, X_train, y_train =  ps.my_par(path + "test.txt",fnames, 19, path2)

print(X_train.shape)
print(y_train.shape)

clfr = SVC(kernel = 'linear', C = 1, gamma = 0.01, cache_size = 3000, class_weight = 'balanced')

clfr.fit(X_train,y_train)

pickle.dump(clfr, open(path3 + "my_pssm_SVM_final.pkl", "wb"))
