import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
import matplotlib.pyplot as plt


path = "Datasets/"

# Work on the original big Data set

# Make lists for each element (protein name, amino acid sequence, secondary structure)

protein_ID = []
sequences = []
topology = []

with open (path + "globular_signal_tm_3state.3line.txt") as f:
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



###  Pike a protein


sequence = sequences[int(input('Pick a protein: '))]


slide_window_size = int(input("provide a sliding window: "))  ### add manually the number of elements for the windows
extra_window = int(slide_window_size//2)         # gives the number of zeros which need to be added at the beginning as well as at the end of the sequence
print(extra_window)

####### Sliding windows
aa_plet = []

for i in range(0, len(sequence)-slide_window_size+1):
    aa_win = sequence[i:i+slide_window_size]
    aa_plet.append(aa_win)
print(aa_plet)

########### Binary Sliding Windows

windows = []
for triplets in aa_plet:
    list_C = []
    for aa in triplets:
        for key, value in dictionary.items():
            if aa == key:
                list_C.extend(value)     ### joins the lists of binaries for each window's amino acids
    windows.append(list_C)
print(windows)

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
for i in range(1, extra_window+1):
    amino = windows[0][0:((extra_window+i)*len(aminoacid))]
    #print(amino)
    extra_aa.append(amino)



#### Pad zeros
padding = []
for j in range(0,extra_window):
    pad = (extra_window-j)*list_zeros
    #print(pad)
    padding.append(pad)

left = []
for pads,extras in zip(padding,extra_aa):
    list_pads = pads + extras
    #print(list_pads)
    left.append(list_pads)
#print(left)


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

counts = extra_window
extra_aa2 = []
for i in range(1, extra_window+1):
    amino = windows[-1][-(extra_window+counts)*len(aminoacid):]   # counts from the last part to the end
    print(amino)
    counts = counts - 1
    extra_aa2.append(amino)

counter = extra_window - 1
padding2 = []
for j in range(0,extra_window):
    pad = (extra_window-counter)*list_zeros
    print(pad)
    counter = counter - 1
    padding2.append(pad)

right = []
for pads2,extras2 in zip(padding2,extra_aa2):
    list_pads = extras2 + pads2
    #print(list_pads)
    right.append(list_pads)
print(right)




####### Get the final binary sequence with the left, right extra windows

final = left + windows + right
#print(len(final[-1]))  # Confirm sizes of first and last window
#print(len(final[0]))


X = np.array(final)
print(X.shape)