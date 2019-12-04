
import copy

def mark_grid(wire):
    # Takes in a list of wire steps
    # Returns a list of (x, y) indicating where the wire lies
    
    # Don't include the starting point
    coords = []
    last_coord = [0, 0]

    for e in wire:

        direction = e[0]
        steps = int(e[1:])

        if direction == "R":
            i = 0
            delta = 1
        elif direction == "L":
            i = 0
            delta = -1
        elif direction == "U":
            i = 1
            delta = 1
        elif direction == "D":
            i = 1
            delta = -1

        for j in range(steps):
            next_coord = copy.copy(last_coord)
            next_coord[i] += delta
            coords.append(next_coord)
            last_coord = copy.copy(next_coord)

    return [(x, y) for [x, y] in coords]


def get_best_overlap(overlaps):
    
    best = overlaps[0]
    best_distance = abs(best[0]) + abs(best[1])

    for (x, y) in overlaps:
        distance = abs(x) + abs(y)
        if distance < best_distance:
            best = x, y
            best_distance = distance

    return best


with open("input.txt") as f:

    lines = list(f.readlines())
    [wire1, wire2] = lines
    wire1 = wire1.split(",")
    wire2 = wire2.split(",")

    wire_grid_1 = mark_grid(wire1)
    print("Got wire grid 1, len =", len(wire_grid_1))
    wire_grid_2 = mark_grid(wire2)
    print("Got wire grid 2, len = ", len(wire_grid_2))

    overlaps = set(wire_grid_1).intersection(set(wire_grid_2))
    print("Got overlaps: len =", len(overlaps))

    best = get_best_overlap(list(overlaps))
    print("Best overlap:", best)

    print("Distance:", abs(best[0]) + abs(best[1]))