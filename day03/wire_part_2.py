
import copy

def mark_grid(wire):
    # Takes in a list of wire steps
    # Returns a list of (x, y) indicating where the wire lies
    
    # Don't include the starting point
    coords = []
    last_coord = [0, 0, 0]

    index = 0
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
            next_coord[2] = index
            coords.append(next_coord)
            last_coord = copy.copy(next_coord)

            index += 1

    return [(x, y, z) for [x, y, z] in coords]

def get_overlaps(wire1, wire2):

    condensed1 = set([(x, y) for (x, y, z) in wire1])
    condensed2 = set([(x, y) for (x, y, z) in wire2])

    overlaps = dict()
    for (x, y, z) in wire1:
        if (x, y) in condensed2:
            overlaps[(x, y)] = [z + 1]
    for (x, y, z) in wire2:
        if (x, y) in condensed1:
            overlaps[(x, y)].append(z + 1)

    return overlaps


def get_best_overlap(overlaps):
    
    best = None
    best_distance = 1000000000000000000000

    for ((x, y), (dist1, dist2)) in overlaps.items():
        distance = dist1 + dist2
        if distance < best_distance:
            best = x, y
            best_distance = distance

    return best, best_distance


with open("input.txt") as f:

    lines = list(f.readlines())
    [wire1, wire2] = lines
    wire1 = wire1.split(",")
    wire2 = wire2.split(",")

    wire_grid_1 = mark_grid(wire1)
    print("Got wire grid 1, len =", len(wire_grid_1))
    wire_grid_2 = mark_grid(wire2)
    print("Got wire grid 2, len = ", len(wire_grid_2))

    overlaps = get_overlaps(set(wire_grid_1), set(wire_grid_2))
    print("Got overlaps: len =", len(overlaps))

    best, best_distance = get_best_overlap(overlaps)
    print("Best overlap:", best)
    print("Distance:", best_distance)