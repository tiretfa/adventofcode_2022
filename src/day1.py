elves = []
with open('data/day1.txt', 'r+') as f:
    cur_weight = 0
    for line in f.readlines():
        if line == '\n' and cur_weight !=0:
            elves.append(cur_weight)
            cur_weight = 0
        else:
            cur_weight += int(line)
max1 = max(elves)
elves.remove(max1)
max2 = max(elves)
elves.remove(max2)
max3 = max(elves)
print(max1+max2+max3)
