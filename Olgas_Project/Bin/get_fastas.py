path = 'Datasets/'

def my_fasta(filename,fasta_train):
    protein_ID = []
    sequences = []
    with open(path + filename) as f:
        count = 2 
        for number, line in enumerate(f, start=1):
            if line.startswith('>'):
                protein_id = line[1:].rstrip()
                protein_ID.append(protein_id)
            elif number == count:
                seq = line.rstrip()
                sequences.append(seq)
                count = count + 3
    with open(path + fasta_train, 'w') as file:
        for protein,seq in zip (protein_ID,sequences):
            file.writelines('>' + protein + '\n')
            file.writelines(seq + '\n')


my_fasta('60_prot.txt','fasta_train.fasta')

my_fasta('subset_of_30_proteins.txt','fasta_test.fasta')
