
with open('data/day2.txt', 'r+') as f:
    score = 0
    for line in f.readlines():
        a = ord(line.split(' ')[0]) - ord('A')
        b = ord(line.split(' ')[1][0]) - ord('X')
        if b == 1:
            score += a + 1
            score += 3
        elif b == 2:
            score += (a+1)%3 + 1
            score += 6
        else:
            score += (a-1)%3 + 1

print(score)


