import re

RE_MOVE = re.compile(r'move ([0-9]+) from ([0-9]+) to ([0-9]+)\n')

def extract_stacks(lines):
    stacks = {}
    for line in lines:
        for i in range(0, 9):
            if not stacks.get(i+1):
                stacks[i+1] = []
            if line[i*4+1] != ' ':
                stacks[i+1].insert(0,line[i*4+1])
    return stacks

def apply_move2(line, stacks):
    count = int(RE_MOVE.match(line).group(1))
    st1 = int(RE_MOVE.match(line).group(2))
    st2 = int(RE_MOVE.match(line).group(3))
    stacks[st2].extend(stacks[st1][-count:])
    stacks[st1] = stacks[st1][:-count]

def apply_move(line, stacks):
    count = int(RE_MOVE.match(line).group(1))
    st1 = int(RE_MOVE.match(line).group(2))
    st2 = int(RE_MOVE.match(line).group(3))
    for i in range(count):
        crate = stacks[st1].pop()
        stacks[st2].append(crate)

def print_res(stacks):
    res = ''
    for i in range(1,10):
        res = res + stacks[i][len(stacks[i])-1]
    print(res)

with open('data/day5.txt') as f:
    lines = []
    for i, line in enumerate(f.readlines()):
        if i < 8:
            lines.append(line)
        elif i == 8:
            stacks = extract_stacks(lines)
        elif line == '\n':
            continue
        else:
            apply_move2(line, stacks)
# one star
print_res(stacks)
