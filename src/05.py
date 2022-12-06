from copy import deepcopy

# DATA PREP

f = open("input.txt", "r")
data = [x for x in f.read().split('\n\n') if x != '']

init_crates = data[0].replace('[', ' ').replace(']', ' ').split('\n')[:-1]  # clean undesired chars and transform in array
init_crates = ["".join(x)[::-1] for x in zip(*init_crates)]  # rotate matrix
init_crates = [list(x.replace(' ', '')) for x in init_crates if not x.isspace()] # clean undesired lines and whitespaces
rearrangement = [
    [int(x) for x in s.split(' ') if x not in ['move', 'from', 'to']]
    for s in data[1].split('\n') if s != ''
]

# PART 1

crates = deepcopy(init_crates)

for s in rearrangement:
    for _ in range(s[0]):
        crates[s[2]-1].append(crates[s[1]-1].pop(-1))

print("".join([x[-1] for x in crates]))

# PART 2

crates2 = deepcopy(init_crates)

for s in rearrangement:
    crates2[s[2]-1].extend(crates2[s[1]-1][-s[0]:])
    del crates2[s[1]-1][-s[0]:]

print("".join([x[-1] for x in crates2]))
