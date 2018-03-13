
path = ('Datasets/')
path2 = ('PSSM/train/')
#path2 = ('PSSM/test/')
#path2 = ('PSSM/50_new/')
def my_fasta(filename):
    protein_ID = []
    sequences = []
    with open(path + filename) as f: 
        for number, line in enumerate(f, start=1):
            if line.startswith('>'):
                protein_id = line.rstrip()
                protein_ID.append(protein_id)
            else:
                seq = line.rstrip()
                sequences.append(seq)	

    for protein,seq in zip (protein_ID,sequences):
        output = path2 + protein[1:] + '.fasta'
        output_file = output.replace("|","_")
        with open(output_file, 'w') as my_file:
            my_file.write(protein + '\n')
            my_file.write(seq + '\n')

my_fasta('fasta_train.fasta')
#my_fasta('fasta_test.fasta')
#my_fasta('50_new_prot.txt')


