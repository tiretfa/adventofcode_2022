class Folder(object):
    def __init__(self, name, previous):
        self.name = name
        self.previous = previous
        self.children = []
    
    def append_folder(self, name):
        if name not in [child.name for child in self.children]:
            self.children.append(Folder(name, self))

    def append_file(self, name, size):
        if name not in [child.name for child in self.children]:
            self.children.append(File(name, size))

    def get_size(self):
        res = 0
        for child in self.children:
            if isinstance(child, Folder):
                res += child.get_size()
            elif isinstance(child, File):
                res += child.size
        return res

    def cd(self, name):
        for child in self.children:
            if isinstance(child, Folder) and child.name == name:
                return child
        else:
            folder = Folder(name, self)
            self.children.append(folder)
            return folder

    def get_folder_sizes(self):
        res = 0
        for child in self.children:
            if isinstance(child, Folder):
                size = child.get_size()
                if size < 100000:
                    res += size
                res += child.get_folder_sizes()
        return res

class File(object):
    def __init__(self, name, size):
        self.name = name
        self.size = size

with open('data/day7.txt') as f:
    init = Folder('init', None)
    current_folder = init
    for line in f.readlines():
        line = line[:-1]
        if line.startswith('$'):
            if line.split(' ')[1] == 'cd':
                if line.split(' ')[2] == '..':
                    current_folder = current_folder.previous
                else:
                    name = line.split(' ')[2]
                    current_folder = current_folder.cd(name)
        elif line.split(' ')[0] == 'dir':
            name = line.split(' ')[1]
            current_folder.append_folder(name)
        else:
            size = int(line.split(' ')[0])
            name = line.split(' ')[1]
            current_folder.append_file(name, size)
            
print(init.get_folder_sizes())
