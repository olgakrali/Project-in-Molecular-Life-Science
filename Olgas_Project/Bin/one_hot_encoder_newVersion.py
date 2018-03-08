######### One hot encoder updated version

def my_one_hot_enc():
    aminoacid = list('ACDEFGHIKLMNPQRSTVWY')  ### a list for the 20 amino acids

    # Make a list that contains 20 zeros
    zeros_list = []

    for i in range(len(aminoacid)):
        n = 20
        zeros = [0] * n
        zeros_list.append(zeros)
    # print(zeros_list)

    ### Make one hot encoders for each amino acid
    zero_one = []
    j = 0
    for zero in zeros_list:
        zero[j] = 1
        j = j + 1
        zero_one.append(zero)
    # print(zero_one)


    # Make a dictionary to add its keys and values
    dictionary = {}
    for line, aa in zip(zero_one, aminoacid):  ### it reads simultaneously every row and every amino acid
        dictionary[aa] = line
    return dictionary

if __name__ == "__main__":
    print(my_one_hot_enc())
