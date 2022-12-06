
# PART 1

f = open("input.txt", "r")
elves_calories = []
elves =[x for x in f.read().split('\n\n')]
for e in elves:
    calories = sum([int(x) for x in e.split('\n') if x != ''])
    elves_calories.append(calories)

elves_calories.sort(reverse=True)
print(elves_calories[0])


# PART 2

three_max_elves = sum(elves_calories[0:3])
print(three_max_elves)