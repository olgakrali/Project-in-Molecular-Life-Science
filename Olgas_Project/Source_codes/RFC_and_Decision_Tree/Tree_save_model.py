import numpy as np
from sklearn.tree import DecisionTreeClassifier
import pickle


import parsers_windows as mp

# Train and save my model
path = "Datasets/"
path2 = "Saved_models/"

protein_ID, sequences, topology, svm2, seconstr, struct_labels = mp.my_par("test.txt", 21) # '60_prot.txt' was also tried

X_train = np.array(svm2)
print(X_train.shape)
y_train = np.array(seconstr)
print(y_train.shape)

clfr = DecisionTreeClassifier(min_samples_split = 2, class_weight = 'balanced')

clfr.fit(X_train,y_train)

pickle.dump(clfr, open(path2 + "Decision_tree_largerdataset.pkl", "wb")) 
