def previous_dir(archi, current_dir):
    if 

with open('data/day7.txt') as f:
    archi = {}
    current_dir = archi
    current_key = ''
    for line in f.readlines():
        line = line[:-1]
        if line.startswith('$'):
            if line.split(' ')[1] == 'cd':
                if line.split(' ')[2] == '..':
                    current_dir = previous_dir()
                else:
                    dir_name = line.split(' ')[2]
                    if not current_dir.get(dir_name):
                        current_dir[dir_name] = {}
                    current_dir = current_dir[dir_name]
        elif line.split(' ')[0] == 'dir':
            dir_name = line.split(' ')[1]
            if not current_dir.get('dir_name'):
                current_dir[dir_name] = {}
        else:
            file_size = int(line.split(' ')[0])
            file_name = line.split(' ')[1]
            if not current_dir.get('dir_name'):
                current_dir[file_name] = file_size
            
print(archi)
