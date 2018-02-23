####  Add each proteins' elements (ID, Sequence, Topology) into lists

######### Work on a sample of 5 proteins

path = 'Datasets/'

protein_ID = []
sequence = []
topology = []

with open (path + "subset_of_5_proteins.txt") as f:
    count = 2                                          # the counter will give me the 2nd line
    for number, line in enumerate(f, start = 1):
        if line.startswith('>'):
            protein_id = line[1:].rstrip()
            protein_ID.append(protein_id)
        elif number == count:
            seq = line.rstrip()
            sequence.append(seq)
            count =  count + 3        ### count starts from line 2 and will add 3 (that line of code will give as an output every protein sequence only)
        else:
            feature = line.rstrip()
            topology.append(feature)
print(protein_ID)
print(sequence)
print(topology)
