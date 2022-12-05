def get_priority(letter):
    if letter.islower():
        return ord(letter) - ord('a') + 1
    else:
        return ord(letter) - ord('A') + 27
        
def get_sim(l1, l2):
    for letter in l1:
        if letter in l2:
            return letter
    else:
        return None

def get_sim2(l1, l2, l3):
    for letter in l1:
        if letter in l2 and letter in l3:
            return letter
    else:
        raise ValueError()

with open('data/day3.txt', 'r+') as f:
    score = 0
    for line in f.readlines():
        length = len(line) -1
        first_part = line[:int(length/2)]
        second_part = line[int(length/2):]
        sim = get_sim(first_part, second_part)
        score += get_priority(sim)
# one star
print(score)

with open('data/day3.txt', 'r+') as f:
    score = 0
    count = 0
    for line in f.readlines():
        if count != 0 and count%3 == 0:
            sim = get_sim2(l1, l2, l3)
            score += get_priority(sim)
        if count % 3 == 0:
            l1 = line[:-1]
        elif count % 3 == 1:
            l2 = line[:-1]
        else:
            l3 = line[:-1]
        count += 1
    sim = get_sim2(l1, l2, l3)
    score += get_priority(sim)
# two star
print(score)
