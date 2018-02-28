import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.model_selection import cross_val_score
import matplotlib.pyplot as plt



path = "Datasets/"

# Work on the original big Data set

# Make lists for each element (protein name, amino acid sequence, secondary structure)

protein_ID = []
sequences = []
topology = []

with open(path + "subset_of_50_proteins.txt") as f:
    count = 2                                          # gives me the second line directly
    for number, line in enumerate(f, start = 1):
        if line.startswith('>'):
            protein_id = line[1:].rstrip()
            protein_ID.append(protein_id)
        elif number == count:
            seq = line.rstrip()
            sequences.append(seq)
            count =  count + 3                       ### if you add 3 starting from line 2 you will always get the sequence of a protein as an output
        else:
            feature = line.rstrip()
            topology.append(feature)


aminoacid = list('ACDEFGHIKLMNPQRSTVWY')  ### a list for the 20 amino acids

#Make a list that contains 20 zeros
zeros_list = []

for line in aminoacid:
    n = 20
    zeros = [0]*n
    zeros_list.append(zeros)
#print(zeros_list)

### Make one hot encoders for each amino acid
zero_one = []
i = 0
for zero in zeros_list:
    zero[i] = 1
    i = i + 1
    zero_one.append(zero)
#print(zero_one)


# Make a dictionary to add its keys and values
dictionary = {}
for line, aa in zip(zero_one, aminoacid):     ### it reads simultaneously every row and every amino acid
    dictionary[aa] = line

#print(dictionary)



#### Work in test and train data set



slide_window_size = 3  ### add manually the number of elements for the windows
extra_window = int(slide_window_size//2)         # gives the number of zeros which need to be added at the beginning as well as at the end of the sequence

####### Sliding windows
seq_win = []
for sequence in sequences:
    aa_plet = []
    for i in range(0, len(sequence)-slide_window_size+1):
        aa_win = sequence[i:i+slide_window_size]
        aa_plet.append(aa_win)
   #print(aa_plet)
    seq_win.append(aa_plet)
#print(len(seq_win))
########### Binary Sliding Windows

windows = []
for group in seq_win:
    list_D = []
    for triplets in group:
        list_C = []
        for aa in triplets:
            for key, value in dictionary.items():
                if aa == key:
                    list_C.extend(value)     ### joins the lists of binaries for each window's amino acids
        list_D.append(list_C)
    windows.append(list_D)
#print(windows)

list_zeros = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

################# Add padding windows on left and right of every binary sequence

################## Left padding ####################
## With a window size of 5, the pad will be 2, so 00ABC and 0ABCD (transformed to binaries of course, I just use a simple example of strings)
## The amino acids will be read in every window from left to right by window_extra + i (0: 2+1 for the first pad, and 0: 2+2 for the second pad)
## The zeros will be reduced by window_extra - i (2-0, 2-1)
###The code for the binaries of the amino acids will read the input* 20 (n_amino_acids), since we have binaries and not letters
#### so for the first pad, it would read the first window (from windows) from (0:(2+1)*20) = (0:60)
##### In these 60 binaries  coming from 3 amino acids will be added 2*20 zeros for getting the first pad = 100
###### Similarly happens with the second window.
########Works the same for other window sizes
#####################################################


#### Pad amino acids
extra_aa = []
for window in windows:
    extras = []
    for i in range(1, extra_window+1):
        amino = window[0][0:((extra_window+i)*len(aminoacid))]
        #print(len(amino))
        extras.append(amino)
    extra_aa.append(extras)
#print(extra_aa)
#print(len(extra_aa))


#### Pad zeros
padding = []
for window in windows:
    pads = []
    for j in range(0,extra_window):
        pad = (extra_window-j)*list_zeros
        #print(len(pad))
        pads.append(pad)
    padding.append(pads)
#print(len(padding))

left = []
for binary,am in zip(padding,extra_aa):
    ab = []
    for b,a in zip(binary, am):
        list_pads = b + a
        #print(list_pads)
        ab.append(list_pads)
    left.append(ab)
# print(left)
# print(len(left[0][0]))
#
################## Right padding ####################
## With a window size of 5, the pad will be 2, so ABC0 and BCD00
## The amino acids will be read in every window from left to right by window_extra + i (-(2+2): (end) for the first pad, and -(2+1): (end) for the second pad)
## The zeros will be increased by window_extra minus a counter that gets smaller for every window (2-1, 2-0)
###The code for the binaries of the amino acids will read the input* 20 (n_amino_acids), since we have binaries and not letters
#### so for the last pad, it would read the last window (from windows) from (-(2+1)*20) = (-60: )
##### In these 60 binaries  coming from 3 amino acids will be added 2*20 zeros for getting the last pad = 100
###### Similarly happens with the second to last window.
########Works the same for other window sizes
#####################################################


extra_aa2 = []
for window in windows:
    a_list = []
    c1 = extra_window
    for i in range(1, extra_window+1):
        amino = window[-1][-(extra_window+c1)*len(aminoacid):]   # counts from the last part to the end
        #print(len(amino))
        counts = c1 - 1
        a_list.append(amino)
    extra_aa2.append(a_list)
#print(len(extra_aa2[1][0]))



padding2 = []
for window in windows:
    c = extra_window - 1
    b_list = []
    for j in range(0,extra_window):
        pad = (extra_window-c)*list_zeros
        #print(len(pad))
        counter = c - 1
        b_list.append(pad)
    padding2.append(b_list)
#print(padding2)





right = []
for am,binary in zip(extra_aa2,padding2):
    ab = []
    for extras2,pads2 in zip(am,binary):
        list_pads = extras2 + pads2
        #print(list_pads)
        right.append(list_pads)
#print(right)




####### Get the final binary sequence with the left, right extra windows
svm_input = []
for l,w,r in zip (left, windows, right):
    final = l + w
    final2 = final + [r]
    svm_input.append(final2)
#print(len(svm_input[0]))  # Confirm numbers of windows of a sequence


svm2 = sum(svm_input,[])
print(svm2)
print(len(svm2))
X = np.array(svm2)
print(X.shape)

print(type(X))
print(X)

############# Get the features

struct_labels = {'G': 1, 'S': 2, 'M': 3}

seconstr = []         #this list will contain a list of integers for every protein
for structure in topology:
    list_A = []
    for letter in structure:
        for key, value in struct_labels.items():
            if letter == key:
                list_A.append(value)
    seconstr.extend(list_A)              #### add the topologies from every sequence together in one list

y = np.array(seconstr)
print(y.shape)

print(y)