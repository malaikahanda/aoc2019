# Part 1

total = 0

with open("input.txt") as f:
    for line in f.readlines():
        i = int(line)
        total += ((i // 3) - 2)

print("Total:", total)