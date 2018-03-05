path = "Datasets/"

from random import shuffle
import itertools
with open(path + "globular_signal_tm_3state.3line.txt") as f:
    lines = []
    for line1,line2,line3 in itertools.zip_longest(*[f]*3):
        line  = line1 + line2 + line3
        lines.append(line)

shuffle(lines)
train = len(lines)* 80 // 100
with open(path + "train.txt", "w") as f:
    f.writelines(lines[:train])
with open(path + "test.txt", 'w') as f:
    f.writelines(lines[train:])


print(len(lines))




