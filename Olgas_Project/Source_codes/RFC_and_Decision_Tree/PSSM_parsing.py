import numpy as np

def my_par(filename, fnames, slide_window_size, path2):
    protein_ID = []
    sequences = []
    topology = []
    with open(filename) as f:
        count = 2  # gives me the second line directly
        for number, line in enumerate(f, start=1):
            if line.startswith('>'):
                protein_id = line[1:].rstrip()
                id = protein_id.replace('|', '_')
                protein_ID.append(id)
            elif number == count:
                seq = line.rstrip()
                sequences.append(seq)
                count = count + 3  ### if you add 3 starting from line 2 you will always get the sequence of a protein as an output
            else:
                feature = line.rstrip()
                topology.append(feature)
    my_evolution = []
    my_names = []
    for fname in fnames:
        my_dat = np.genfromtxt(path2 + fname, skip_header = 3, skip_footer= 5, dtype = None, usecols = range(22,42))
        my_data = my_dat/100
        #print(my_data)
        evols = my_data.tolist()
        names = fname.split('.')[0]
        my_evolution.append(evols)
        my_names.append(names)
    #print(len(my_evolution))
    #print(my_names)

    #### Put the topologies and the sequences on the fasta files names order
    new_seq = []
    new_top = []
    for name in my_names:
        for id, sequence, topo in zip(protein_ID,sequences,topology):
            if id == name:
                new_seq.append(sequence)
                new_top.append(topo)

    #### put the list of 20 numbers of each aminoacid in the same list for every sequence

    my_evol = []
    for pre,seq in zip(my_evolution,new_seq):
        new_list  = []
        for pred in pre:
            new_list.extend(pred)
        #print(new_list)
        my_evol.append(new_list)
    #print(len(my_evol[0]))  # 712 aminos * 20 = 14240 numbers for this sequence

    ### Let's make the windows
    n = 20   # total number of integers for every aninoacid
    extra_window = int(slide_window_size // 2)  # gives the number of zeros which need to be added at the beginning as well as at the end of the sequence
    ####### Sliding windows
    windows = []
    for sequence in my_evol:
        aa_plet = []
        for i in range(0, len(sequence) - (slide_window_size)*n + n, n): # read every 20 steps
            aa_win = sequence[i:i + (slide_window_size)*n]
            aa_plet.append(aa_win)
            # print(aa_plet)
        windows.append(aa_plet)
    #print(len(windows[0][0]))



    list_zeros = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    ################# Add padding windows on left and right of every binary sequence

    ################## Left padding ####################
    ## With a window size of 5, the pad will be 2, so 00ABC and 0ABCD (transformed to binaries of course, I just use a simple example of strings)
    ## The amino acids will be read in every window from left to right by window_extra + i (0: 2+1 for the first pad, and 0: 2+2 for the second pad)
    ## The zeros will be reduced by window_extra - i (2-0, 2-1)
    ###The code for the binaries of the amino acids will read the input* 20 (n_amino_acids), since we have binaries and not letters
    #### so for the first pad, it would read the first window (from windows) from (0:(2+1)*20) = (0:60)
    ##### In these 60 binaries  coming from 3 amino acids will be added 2*20 zeros for getting the first pad = 100
    ###### Similarly happens with the second window.
    ########Works the same for other window sizes
    #####################################################


    #### Pad amino acids
    extra_aa = []
    for window in windows:
        extras = []
        for i in range(1, extra_window + 1):
            amino = window[0][0:((extra_window + i) * n)]
            # print(len(amino))
            extras.append(amino)
            # print(len(extras[2]))
        extra_aa.append(extras)
        # print(extra_aa)
        # print(len(extra_aa))

    #### Pad zeros
    padding = []
    for window in windows:
        pads = []
        for j in range(0, extra_window):
            pad = (extra_window - j) * list_zeros
            # print(len(pad))
            pads.append(pad)
            # print(len(pads))
        padding.append(pads)
        # print(len(padding))

    left = []
    for binary, am in zip(padding, extra_aa):
        ab = []
        for b, a in zip(binary, am):
            list_pads = b + a
            # print(list_pads)
            ab.append(list_pads)
            # print(len(ab))
        left.append(ab)
    #print(left)
    #print(len(left[0]))



    ################## Right padding ####################
        ## With a window size of 5, the pad will be 2, so ABC0 and BCD00
        ## The amino acids will be read in every window from left to right by window_extra + i (-(2+2): (end) for the first pad, and -(2+1): (end) for the second pad)
        ## The zeros will be increased by window_extra minus a counter that gets smaller for every window (2-1, 2-0)
        ###The code for the binaries of the amino acids will read the input* 20 (n_amino_acids), since we have binaries and not letters
        #### so for the last pad, it would read the last window (from windows) from (-(2+1)*20) = (-60: )
        ##### In these 60 binaries  coming from 3 amino acids will be added 2*20 zeros for getting the last pad = 100
        ###### Similarly happens with the second to last window.
        ########Works the same for other window sizes
        #####################################################


    extra_aa2 = []
    for window in windows:
        c1 = extra_window
        a_list = []
        for i in range(1, extra_window + 1):
            amino = window[-1][-(extra_window + c1) * n:]  # counts from the last part to the end
            # print(len(amino))
            c1 = c1 - 1
            a_list.append(amino)
            # print(a_list)
        extra_aa2.append(a_list)
    # print(len(extra_aa2))


    padding2 = []
    for window in windows:
        c = extra_window - 1
        b_list = []
        for j in range(0, extra_window):
            pad = (extra_window - c) * list_zeros
            # print(len(pad))
            c = c - 1
            b_list.append(pad)
        padding2.append(b_list)
    # print(len(padding2))

    right = []
    for am2, binary2 in zip(extra_aa2, padding2):
        ab2 = []
        for extras2, pads2 in zip(am2, binary2):
            list_pads = extras2 + pads2
            # print(list_pads)
            ab2.append(list_pads)
        right.append(ab2)
    #print(len(right[0]))

    ####### Get the final binary sequence with the left, right extra windows
    lef_input = []
    for l, w in zip(left, windows):
        fin = l + w
        lef_input.append(fin)
    # print(len(lef_input[1]))
    # print(len(lef_input[1][0]))
    svm_input = []
    for lf, r in zip(lef_input, right):
        final = lf + r
        svm_input.append(final)
    # print(len(svm_input[1][970]))

    svm2 = []
    for inp in svm_input:
        svm2.extend(inp)

    #print(len(svm2))

    X = np.array(svm2)
    #print(X.shape)

    #My states
    struct_labels = {'G': 1, 'S': 2, 'M': 3}
    seconstr = []  # this list will contain a list of integers for every protein
    for structure in new_top:
        list_A = []
        for letter in structure:
            for key, value in struct_labels.items():
                if letter == key:
                    list_A.append(value)
        seconstr.extend(list_A)  #### add the topologies from every sequence together in one list
    #print(len(seconstr))

    y  = np.array(seconstr)
    #print(y.shape)

    return my_names, new_seq, new_top, struct_labels, X, y

if __name__ == "__main__":
    print("it works")