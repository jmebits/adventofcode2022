
# DATA PREP

f = open("input.txt", "r")
forest = [[int(y) for y in x] for x in f.read().split('\n') if x != '']


# PART 1

count = 0

for x, row in enumerate(forest):
    for y, tree in enumerate(row):
        if x == 0 or y == 0 or x == len(row)-1 or y == len(forest)-1:
            count = count + 1
        else:
            column = [i[y] for i in forest]
            edges = [row[:y], row[y+1:], column[:x], column[x+1:]]
            for e in edges:
                if all(i < tree for i in e):
                    count = count + 1
                    break

print(count)


# PART 2

max_score = 0

def tree_filter(tree_flag, trees):
    result = []
    for t in trees:
        result.append(t)
        if t >= tree_flag:
            break
    return result


for x, row in enumerate(forest):
    for y, tree in enumerate(row):

        if x == 0 or y == 0 or x == len(row)-1 or y == len(forest)-1:
            continue
        else:
            column = [i[y] for i in forest]
            edges = [row[0:y][::-1], row[y+1:], column[0:x][::-1], column[x+1:]]
            filtered_edges = [tree_filter(tree, i) for i in edges]
            scores = [len(f) for f in filtered_edges]

            scenic_score = 1
            for s in scores:
                scenic_score = scenic_score * s

            if scenic_score > max_score:
                max_score = scenic_score

print(max_score)
