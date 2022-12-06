
f = open("input.txt", "r")
rucksacks = [x for x in f.read().split('\n') if x != '']

# PART 1

points = 0

for r in rucksacks:
    compartment1 = r[0: len(r)//2]
    compartment2 = r[len(r)//2:]
    c1 = set(compartment1)
    c2 = set(compartment2)

    common = c1 & c2

    for c in common:
        points = points + (ord(c)-(38 if c.isupper() else 96))

print(points)


# PART 2

points = 0
subarraylen = 3
for i in range(0, len(rucksacks), subarraylen):
    subarr = rucksacks[i:i+subarraylen]
    print(subarr)
    sets = [set(s) for s in subarr]
    print(sets)
    common2 = sets[0] & sets[1] & sets[2]
    for c in common2:
        print(c)
        points = points + (ord(c) - (38 if c.isupper() else 96))

print(points)