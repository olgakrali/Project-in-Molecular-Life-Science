letters = list('ABCDEFG')

#Make a list that contains 7 zeros
zeros_list = []

for letter in letters:
    n = 7
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
print(zero_one)


# Make a dictionary to add its keys and values
dictionary = {}
for line, letter in zip(zero_one, letters):     ### it reads simultaneously every row and every amino acid
    dictionary[letter] = line
print(dictionary)

sequence = 'ABCDFEAAG'



slide_window_size = int(input("provide a sliding window: "))  ### add manually the number of elements for the windows
extra_window = int(slide_window_size//2)         # gives the number of zeros which need to be added at the beginning as well as at the end of the sequence
print(extra_window)

####### Transform the windows into arrays of binaries coming from the dictionary
##### sliding windows from the beginning to the end of the sequence (all are read)
aa_plet = []

for i in range(0, len(sequence)-slide_window_size+1):
    aa_win = sequence[i:i+slide_window_size]
    aa_plet.append(aa_win)
print(aa_plet)



windows = []
for triplets in aa_plet:
    list_C = []
    for aa in triplets:
        for key, value in dictionary.items():
            if aa == key:
                list_C.extend(value)     ### joins the lists of binaries for each window's amino acids
    windows.append(list_C)
print(windows)

list_zeros = [0,0,0,0,0,0,0]


##### Left padding
###### this will add the amino acid binaries to the list of paddings zeros
extra_aa = []
for i in range(1, extra_window+1):
    amino = windows[0][0:((extra_window+i)*len(letters))]
    #print(amino)
    extra_aa.append(amino)

#### for zeros

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


############### Right padding

################ This code adds to the end of the sequence

count = extra_window
extra_aa2 = []
for i in range(1, extra_window+1):
    amino = windows[-1][-(extra_window+count)*len(letters):]   # counts from the last part to the end
    print(amino)
    count = count - 1
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



final = left + windows + right
print(final)
print(len(final[1]))