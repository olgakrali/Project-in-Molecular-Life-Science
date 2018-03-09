
######### Work on a sample of 5 proteins

path = 'Datasets/'

def my_par(filename):

    protein_ID = []
    sequences = []
    topology = []
    with open(path + filename) as f:
        count = 2  # gives me the second line directly
        for number, line in enumerate(f, start=1):
            if line.startswith('>'):
                protein_id = line[1:].rstrip()
                protein_ID.append(protein_id)
            elif number == count:
                seq = line.rstrip()
                sequences.append(seq)
                count = count + 3  ### if you add 3 starting from line 2 you will always get the sequence of a protein as an output
            else:
                feature = line.rstrip()
                topology.append(feature)
    return protein_ID, sequences, topology


if __name__ == "__name__":
    print('This is my function for parsing my files')
