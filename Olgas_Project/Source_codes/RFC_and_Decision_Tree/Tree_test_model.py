import numpy as np
import pickle
from sklearn.metrics import confusion_matrix
from sklearn import preprocessing
import matplotlib.pyplot as plt

import parsers_windows as mp


path = "Datasets/"
path2 = "Saved_models/"

protein_ID, sequences, topology, svm2, seconstr, struct_labels = mp.my_par("subset_of_30_proteins.txt", 21)
print(len(protein_ID))

#Prepare the X and y for the svm
X_test = np.array(svm2)
print(X_test.shape)

y_test = np.array(seconstr)
print(y_test.shape)
#####SVM

# Load the model
my_model = pickle.load(open(path2 + "Decision_tree.pkl","rb"))

result = my_model.score(X_test,y_test)
print(result)

predictions = my_model.predict(X_test)
#print(predictions)


#Build a confusion matrix
conf = confusion_matrix(y_test, predictions)
# Data normalization

conf_m = preprocessing.normalize(conf, norm = 'l1')
### Then plot


print(conf_m)

fig = plt.figure(figsize = (8,8))


ax = fig.add_subplot(1,1,1)

#ax.set_aspect(1)
residues = ax.imshow(np.array(conf_m), cmap=plt.get_cmap('jet'),
                interpolation='nearest')

hor, ver = conf_m.shape

for i in range(hor):
    for j in range(ver):
        ax.annotate(str(conf_m[i][j]), xy=(j, i),
                    horizontalalignment='center',
                    verticalalignment='center')

bar = fig.colorbar(residues)
labels = ['Globular', 'Signal Peptide', 'Membrane']
plt.xticks(range(hor), labels[:hor])
plt.yticks(range(ver), labels[:ver])
plt.title('Confusion Matrix for the predicted sequences Decision Tree (window = 21)')
plt.xlabel('Predicted Topologies')
plt.ylabel('True Topologies')
plt.show()


#### Save a file with sequence ID, sequence, topology and predicted topology


# With this function the predictions (integers) are transformed to their states, then they are split from the big list of strings to sizes equal to each
# sequence of this dataset to form a list of predicted topologies.
def my_predictions():
    predtopo = []
    for pred in predictions:
        for key, value in struct_labels.items():
            if pred == value:
                predtopo.append(key)
    #print(predtopo)
    i = 0
    predict = []
    for lines in sequences:
        j = len(lines)+ i
        #print(len(line))
        new = predtopo[i:j]
        #print(new)
        predict.append(new)
        i = j
    #print(len(predict))
    my_pred = []
    for k in range(0,len(predict)):
        final = ''.join(predict[k])
        my_pred.append(final)
        #print(final)
    #print(my_pred)
    return my_pred

my_pred = my_predictions()


with open(path + 'true_vs_predicted_topo_DT.txt', 'w') as file:
    for prot, sequen, top, pre in zip(protein_ID,sequences,topology,my_pred):
        file.writelines('>' + prot + '\n')
        file.writelines(sequen + '\n')
        file.writelines(top + '\n')
        file.writelines(pre + '\n')
