
# Part 1

total = 0

with open("input.txt") as f:
    for line in f.readlines():
        i = int(line)
        total += ((i // 3) - 2)

print("Total:", total)


# Part 2

def get_fuel(x, total_so_far=0):

    diminished = (x // 3) - 2

    if diminished <= 0:
        return total_so_far

    else:
        return get_fuel(diminished, total_so_far + diminished)

total = 0

with open("input.txt") as f:
    for line in f.readlines():
        i = int(line)
        total += get_fuel(i)

print("Total:", total)