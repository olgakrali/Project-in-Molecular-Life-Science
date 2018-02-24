import pandas as pd
import numpy as np
from sklearn.svm import SVC
from sklearn.model_selection import cross_val_score
import matplotlib.pyplot as plt


path = 'Datasets/'

# Work on the original big dataset

# Make lists for each element (protein name, amino acid sequence, secondary structure)

protein_ID = []
sequence = []
topology = []

with open (path + 'globular_signal_tm_3state.3line.txt') as f:
    count = 2                                          # gives me the second line directly
    for number, line in enumerate(f, start = 1):
        if line.startswith('>'):
            protein_id = line[1:].rstrip()
            protein_ID.append(protein_id)
        elif number == count:
            seq = line.rstrip()
            sequence.append(seq)
            count =  count + 3                       ### if you add 3 starting from line 2 you will always get the sequence of a protein as an output
        else:
            feature = line.rstrip()
            topology.append(feature)

############## Get the features

#### Create one-hot encodings with the help of Pandas
aminoacid = list('ACDEFGHIKLMNPQRSTVWY')  ### a list for the 20 amino acids

ds = pd.Series(aminoacid)

one_hot_encoding = pd.get_dummies(ds, prefix = None)
one_hot_encoding.index = aminoacid       ### set rownames index as the list of 20 amino acids
print(one_hot_encoding)            ### a pandas DataFrame with the one hot encodings for every amino acid

### Make a dictionary which will contain as keys the amino acids and values the one-hot encodings that corresponds to them

amino = one_hot_encoding.columns.values
zero_one = one_hot_encoding.loc[:,amino].values  #### transforms every row as an array to use it on the for loop

dictionary = {}
for line, aa in zip(zero_one, aminoacid):     ### it reads simultaneously every row and every amino acid
    new = line.tolist()
    dictionary[aa] = new

print(dictionary) ###it is in a form of dict = {A:[1,0,0,0...]...}


###### Add the list of zeros
dictionary.update({'0':[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]})


#######Sliding windows

slide_window = int(input("provide a sliding window: "))  ### add manually the number of elements for the windows
zeros = int(slide_window/2)              # gives the number of zeros which need to be added at the beginning as well as at the end of the sequence
aa_plet = []

for sequen in sequence:
    small_list = []
    sequen = (zeros * '0') + sequen + (zeros * '0')   ##### add the zeros
    for i in range(0, len(sequen)):
        if i + slide_window <= len(sequen):
            aa_win = sequen[i:i+(slide_window)]
            small_list.append(aa_win)
    #print(small_list)
    aa_plet.append(small_list) #contains windows for all the proteins into a list

####### Transform the windows into arrays of binaries coming from the dictionary

protein_n = aa_plet[int(input('Pick a protein: '))]  ##### choose manually the protein you want to proceed till the end

windows = []
for triplets in protein_n:
    list_C = []
    for aa in triplets:
        for key, value in dictionary.items():
            if aa == key:
                list_C.extend(value)
    windows.append(list_C)


### check if the length of the windows is the same as the number of aminoacids of the sequence.
if len(windows) == len(sequence[int(input('Pick a protein: '))]):
    print('It works!')


## Transform the data into an array

X = np.array(windows)
print(X)



################# Get the labels

struct_labels = {'G': 1, 'S': 2, 'M': 3}

seconstr = []         #this list will contain a list of integers for every protein
for structure in topology:
    list_A = []
    for letter in structure:
        for key, value in struct_labels.items():
            if letter == key:
                list_A.append(value)
    seconstr.append(list_A)

y = np.array(seconstr[int(input('Pick a protein: '))])



################ Now I have ready the data for the SVM


##################Support vector machine classifier

#### Use the cross_val_score function for cross validation, instead of splitting on test and train set to avoid overfitting

clfr= SVC(kernel = 'linear', C =1)
clfr.fit(X,y)

print(clfr.score(X,y))

score = cross_val_score(clfr, X, y, cv = int(input('pick a number of cv set: ')), verbose = True)  ####get scores for the train set

print(score)

predictions = clfr.predict(X)  ### how well can the SVM predict our data?
print(predictions)   ##### it returns predicted values for the topologies (1-3)

plt.scatter(y, predictions)

plt.xlabel('True values')
plt.ylabel('Predicted values')
plt.show()          ###Visualizing the true values versus the predictions






