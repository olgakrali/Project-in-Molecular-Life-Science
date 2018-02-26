######## Create sliding windows

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



# Try on an example first
sequence = 'ACDMNP'


slide_window = int(input("provide a sliding window: "))  ### add manually the number of elements for the windows
extra_win = slide_window//2            # gives the number of zeros which need to be added at the beginning as well as at the end of the sequence
print(extra_win)

####### Transform the windows into arrays of binaries coming from the dictionary
print(sequence[0:3])
aa_plet = []

for i in range(1, len(sequence)-1):
    aa_win = sequence[i-extra_win:i+extra_win+1]
    aa_plet.append(aa_win)
print(aa_plet)

windows = []
for triplets in aa_plet:
    list_C = []
    for aa in triplets:
        for key, value in dictionary.items():
            if aa == key:
                list_C.extend(value)
    windows.append(list_C)
print(windows)