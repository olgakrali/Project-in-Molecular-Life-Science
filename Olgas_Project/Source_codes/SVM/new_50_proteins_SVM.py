import numpy as np
import pickle
import new_family_proteins as nf

path = "Datasets/"
prot, seq , svm2 = nf.my_par(path + '50_new_prot.txt',19)

X = np.array(svm2)
print(X.shape)

my_model = pickle.load(open(path + "SVM_new_model.pkl","rb"))




predictions = my_model.predict(X)

def my_predictions():
    struct_labels = {'G': 1, 'S': 2, 'M': 3}
    predtopo = []
    for pred in predictions:
        for key, value in struct_labels.items():
            if pred == value:
                predtopo.append(key)
    #print(predtopo)
    i = 0
    predict = []
    for lines in seq:
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

with open(path + 'predicted_topo_50_New_prot.txt', 'w') as file:
    for protn, sequen, pre in zip(prot,seq,my_pred):
        file.writelines('>' + protn + '\n')
        file.writelines(sequen + '\n')
        file.writelines(pre + '\n')
