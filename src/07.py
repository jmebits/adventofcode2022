
# DATA PREP

class FileFolder:
    def __init__(self, name, size):
        self.children = {}
        self.name = name
        self.size = size

    def get_size(self):
        size = 0
        if self.size == 0:
            for _, f in self.children.items():
                size = size + f.get_size()
        else:
            size = self.size
        return size


def explore(data, index, file):
    while(True):
        if index == len(data)-1:
            return index
        index = index + 1
        i = data[index].split(' ')
        if i[0] == "$":
            if i[1] == 'cd':
                if i[2] == '..':
                    return index
                else:
                    index = explore(data=data, index=index, file=file.children[i[2]])
            if i[1] == 'ls':
                continue
        else:
            file.children[i[1]] = FileFolder(name=i[1], size=0 if i[0] == 'dir' else int(i[0]))


f = open("input.txt", "r")
commands = [x for x in f.read().split('\n') if x != '']

folder = FileFolder(name="/", size=0)
explore(commands, 0, folder)

# PART 1

def find_100k(folder, sum):
    for _, f in folder.children.items():
        if f.size == 0:
            sum = find_100k(f, sum)
    if folder.name == "/":
        return sum
    if folder.size == 0:
        if folder.get_size() < 100000:
            return sum + folder.get_size()
    return sum

print(find_100k(folder, 0))


# PART 2

def find_delete(folder, space, choosen_size):
    for _, f in folder.children.items():
        if f.size == 0:
            choosen_size = find_delete(f, space, choosen_size)
    if folder.name == "/":
        return choosen_size
    if folder.size == 0:
        if choosen_size > folder.get_size() > space:
            return folder.get_size()
    return choosen_size


disk = 70000000
update = 30000000
space_needed = update - (disk - folder.get_size())
print(find_delete(folder, space_needed, disk))