#########One hot encoder updated version


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
print(zero_one)


# Make a dictionary to add its keys and values
dictionary = {}
for line, aa in zip(zero_one, aminoacid):     ### it reads simultaneously every row and every amino acid
    dictionary[aa] = line

print(dictionary)