from collections import Counter

HEIGHT = 6
WIDTH = 25
LAYER_LEN = HEIGHT * WIDTH

def calculate_answer(layer):
    c = Counter(layer)
    ones = c["1"]
    twos = c["2"]
    return ones * twos

def count_zeroes(layer):
    c = Counter(layer)
    return c["0"]

with open("input.txt") as f:
    
    image = list(f.read().strip())

    best_zeros = 1000000000000000000000000000
    best_layer = None
    for i in range(0, len(image), LAYER_LEN):
        layer = image[i : i + LAYER_LEN]
        zeros = count_zeroes(layer)
        if zeros < best_zeros:
            best_zeros = zeros
            best_layer = layer

    print("Answer:", calculate_answer(best_layer))



