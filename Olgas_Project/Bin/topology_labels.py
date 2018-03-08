#### Topologies

###### Example of topology sequences for G, S, M found in my dataset

topologies = ['GGGGGGGGGGGGGGGGGGGGGGGGGSSSSSSSS','GGGGGGGGGGGGGGGGGGGGGGGGGGGG','MMMMMMMMMMMMMMMMMMMMMMMMMMM','SSSSSSSSSSMMMMMMMMMMMSSSSSSSSSSS']

def my_labels():
    struct_labels = {'G': 1, 'S': 2, 'M': 3}
    seconstr = []  # this list will contain a list of integers for every protein
    for structure in topologies:
        list_A = []
        for letter in structure:
            for key, value in struct_labels.items():
                if letter == key:
                    list_A.append(value)
        seconstr.extend(list_A)  #### add the topologies from every sequence together in one list
    #print(len(seconstr))
    return seconstr

if __name__ == "__main__":
    print(my_labels())
