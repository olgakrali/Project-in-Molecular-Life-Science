#### Create one-hot encodings with the help of Pandas

import pandas as pd
aminoacid = list('ACDEFGHIKLMNPQRSTVWY')  ### a list for the 20 amino acids

ds = pd.Series(aminoacid)

one_hot_encoding = pd.get_dummies(ds, prefix = None)
one_hot_encoding.index = aminoacid       ### set rownames index as the list of amino acids
print(one_hot_encoding)            ### a pandas DataFrame with the one hot encodings for every amino acid

### Make a dictionary which will contain as keys the amino acids and values the one-hot encodings that corresponds to them

amino = one_hot_encoding.columns.values
zero_one = one_hot_encoding.loc[:,amino].values  #### transforms every row as an array to use it on the for loop

dictionary = {}
for line, aa in zip(zero_one, aminoacid):     ### it reads simultaneously every row and every amino acid
    new = line.tolist()
    dictionary[aa] = new

print(dictionary) ###it is in a form of dict = {A:[1,0,0,0...]...}

