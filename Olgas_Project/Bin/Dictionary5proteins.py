

path = 'Datasets/'

#Start with the subdataset of the 5 proteins

#Make an empty dictionary (it will be a nested dictionary)

protein = {}

with open (path + 'subset_of_5_proteins.txt') as f:
	for line in f:
		if line.startswith('>'):
			protein_ID = line[1:].rstrip()
			protein[protein_ID] = {}	
		elif line.startswith('M'):
			sequence = line.rstrip()
			protein[protein_ID]['sequence'] = sequence
		else:   
			feature = line.rstrip()
			protein[protein_ID]['topology'] = feature

print(protein)
		


