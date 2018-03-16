import os
import numpy as np
from sklearn.metrics import confusion_matrix
from sklearn import preprocessing
import matplotlib.pyplot as plt
import pickle
import PSSM_parsing as ps

path = "Saved_models/"
path2 = "PSSM/test_final/pssm/"
path3 = "Datasets/"

fnames = os.listdir(path2)

my_names, new_seq, new_top, struct_labels, X_test, y_test =  ps.my_par(path3 + "test_final.txt", fnames, 21, path2)

print(X_test.shape)
print(y_test.shape)

# Load the model
my_model = pickle.load(open(path + "Decision_tree_PSSM_final.pkl","rb"))

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
plt.title('Confusion Matrix for the 89 predicted sequences PSSM (window = 21)')
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
    for lines in new_seq:
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

with open(path3 + 'true_vs_predicted_topo_DT_PSSM_final.txt', 'w') as file:
    for prot, sequen, top, pre in zip(my_names,new_seq,new_top,my_pred):
        id = prot.replace('|', '_')
        file.writelines('>' + id + '\n')
        file.writelines(sequen + '\n')
        file.writelines(top + '\n')
        file.writelines(pre + '\n')
