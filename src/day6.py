
LENGTH = 14

def find_start(signals):
    diff = []
    init = True
    for i,l in enumerate(signals):
        if len(diff) <= LENGTH and init:
            diff.append(l)
            if len(diff) == LENGTH:
                init = False
                if len(set(diff)) == LENGTH:
                    return i+1
        else:
            del diff[0]
            diff.append(l)
            length = len(set(diff))
            if length == LENGTH:
                return i+1

with open('data/day6.txt') as f:
    signals = f.readline()
    start = find_start(signals)
    print(start)

