########### creating sliding windows for the sequences of a protein

### Here I will use an example of small sequences

sequences = ['ACDMNPWYPPPAAACCCDEEERST','GHIKLMNAAAACCCCBEDEE','YYYYYAAAWLMNPPPQ']


slide_window = int(input("provide a sliding window: "))  ### add manually the number of windows

zeros = int(slide_window/2)              # it gives us the number of zeros we have to add  at the beginning and
                                         # the end of the sequence to get the same number of windows as the size of sequences

aa_plet = []
for sequence in sequences:
    small_list = []
    sequence = (zeros * '0') + sequence + (zeros * '0')   ##### add the zeros
    for i in range(0, len(sequence)):
        if i + slide_window <= len(sequence):
            amino = sequence[i:i+(slide_window)]
            small_list.append(amino)
    print(small_list)
    aa_plet.append(small_list)

print(aa_plet)## this list will give as an output a list that contains all the window lists (3 lists for the 3 sequences)

###### Check the length of the windows for a sequence as well as the sequence length

print(len(sequences[0]))
print(len(aa_plet[0]))
print('It works!')