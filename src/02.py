
f = open("input.txt", "r")
rounds = [x for x in f.read().split('\n') if x != '']

# PART 1

SCORE = {
    'X': ['A', 'C', 1],
    'Y': ['B', 'A', 2],
    'Z': ['C', 'B', 3],
}

total_score = 0
for r in rounds:
    if r[0] == SCORE[r[2]][0]:
        total_score = total_score + 3
    elif r[0] == SCORE[r[2]][1]:
        total_score = total_score + 6
    total_score = total_score + SCORE[r[2]][2]

print(total_score)


# PART 2

SCORE_POINTS = {
    'A': [1, 2, 3],
    'B': [2, 3, 1],
    'C': [3, 1, 2],
}

total_score = 0
for r in rounds :
    if r[2] == 'Y':
        total_score = total_score + 3 + SCORE_POINTS[r[0]][0]
    elif r[2] == 'Z':
        total_score = total_score + 6 + SCORE_POINTS[r[0]][1]
    else:
        total_score = total_score + SCORE_POINTS[r[0]][2]


print(total_score)
