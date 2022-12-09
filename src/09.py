
# DATA PREP

f = open("input.txt", "r")
motions = [x for x in f.read().split('\n') if x != '']
motions = [(m.split(' ')[0], int(m.split(' ')[1])) for m in motions]


# PART 1

head_pos = (0, 0)
new_pos = (0, 0)
log = [(0, 0)]

for m in motions:
    for s in range(m[1]):
        if m[0] == 'L':
            new_pos = (head_pos[0], head_pos[1]+1)
        if m[0] == 'R':
            new_pos = (head_pos[0], head_pos[1]-1)
        if m[0] == 'U':
            new_pos = (head_pos[0]+1, head_pos[1])
        if m[0] == 'D':
            new_pos = (head_pos[0]-1, head_pos[1])

        # print(f"{head_pos}-{log[-1]}-{new_pos}")
        if (abs(new_pos[0] - log[-1][0]) > 1 or abs(new_pos[1] - log[-1][1]) > 1):
            log.append(head_pos)

        head_pos = new_pos

print(len(set(log)))

