def extract_pairs(line):
    p1_s = line.split(',')[0]
    p2_s = line.split(',')[1][:-1]
    p1 = [int(p1_s.split('-')[0]),int(p1_s.split('-')[1])]
    p2 = [int(p2_s.split('-')[0]),int(p2_s.split('-')[1])]
    return p1, p2

with open('data/day4.txt', 'r+') as f:
    fully_contains = 0
    for line in f.readlines():
        p1, p2 = extract_pairs(line)
        if p1[0] - p2[0] < 0 and p1[1] - p2[1] > 0 or p1[0] - p2[0] > 0 and p1[1] - p2[1] < 0:
            fully_contains += 1
        elif p1[0] == p2[0] or p1[1] == p2[1]: 
            fully_contains += 1

# one star
print(fully_contains)

with open('data/day4.txt', 'r+') as f:
    overlap = 0
    for line in f.readlines():
        p1, p2 = extract_pairs(line)
        if p1[0] == p2[0] or p1[1] == p2[1]:
            overlap += 1
        elif p1[1] >= p2[0] and p1[0] <= p2[0]:
            overlap += 1
        elif p2[1] >= p1[0] and p2[0] <= p1[0]:
            overlap += 1

# two star
print(overlap)
