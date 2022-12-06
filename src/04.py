import re

# DATA PREP

f = open("input.txt", "r")
data = [x for x in f.read().split('\n') if x != '']
sections = [[int(x) for x in re.split(',|-', s)] for s in data]

# PART 1

pairs = 0
for s in sections:

    l1 = set(range(s[0], s[1]+1))
    l2 = set(range(s[2], s[3]+1))

    if l1 <= l2 or l2 <= l1:
        pairs = pairs + 1

print(pairs)


# PART 2

pairs = 0
for s in sections:

    l1 = set(range(s[0], s[1]+1))
    l2 = set(range(s[2], s[3]+1))

    if len(l1 & l2) > 0:
        pairs = pairs + 1

print(pairs)

