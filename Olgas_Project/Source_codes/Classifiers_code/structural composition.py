# Get compositional percentages for each state. Test code to avoid biases, while subsetting

import mypars as mp

protein_ID, sequence, topology = mp.my_par("globular_signal_tm_3state.3line.txt")

stG = []
stM = []
stS = []
for letters in topology:
    for letter in letters:
        if letter == 'G':
            stG.append(letter)
        elif letter == 'M':
            stM.append(letter)
        else:
            stS.append(letter)

def comp_per(a,b,c):
    compA = (a/(a+b+c)*100)
    compB = (b/(a+b+c)*100)
    compC = (c/(a+b+c)*100)
    return compA, compB, compC

print(comp_per(len(stG),len(stM),len(stS)))


