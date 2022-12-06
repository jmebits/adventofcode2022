# DATA PREP

f = open("input.txt", "r")
data = f.read()

# PART 1

PACKET = 4
def detect(data, length):
    for i in range(1, len(data)):
        if len(set(data[i: i+length])) == len(data[i: i+length]):
            return i+length

print(detect(data, PACKET))

# PART 2

MESSAGE = 14
print(detect(data, MESSAGE))
