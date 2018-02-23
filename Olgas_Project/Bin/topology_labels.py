#### Topologies

###### Example of topology sequences for G, S, M found in my dataset

topologies = ['GGGGGGGGGGGGGGGGGGGGGGGGGSSSSSSSS','GGGGGGGGGGGGGGGGGGGGGGGGGGGG','MMMMMMMMMMMMMMMMMMMMMMMMMMM','SSSSSSSSSSMMMMMMMMMMMSSSSSSSSSSS']

# Assign a number to each of the three structures

struct_labels = {'G': 0, 'S': 1, 'M': 2}

structure = []         #this list will contain a list of integers for every protein ( 5 lists in this case)
for topology in topologies:
    list_A = []
    for letter in topology:
        for key, value in struct_labels.items():
            if letter == key:
                list_A.append(value)
    structure.append(list_A)
    print(list_A)   ##prints out each topology sequence transformed into integers
print(structure)    ## list of all numeric topologies in a larger list