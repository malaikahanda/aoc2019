from collections import Counter

def is_decreasing(pw):
    return sorted(str(pw)) == list(str(pw))

def has_adjacent(pw):
    prev = pw[0]
    for c in pw[1:]:
        if c == prev:
            return True
        prev = c
    return False

pws = 0
for pw in range (193651, 649729 + 1):
    if is_decreasing(pw) and has_adjacent(str(pw)):
        counter = Counter(str(pw))
        if 2 in counter.values():
            pws += 1

print("{} potential passwords".format(pws))
