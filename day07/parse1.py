
import copy
from itertools import permutations

def parse_intcode(intcode, input1, input2):

    my_input = input1

    counter = 0
    output = None
    while True:

        first_val = str(intcode[counter])
        while len(first_val) != 5:
            first_val = "0" + first_val
        opcode = int(first_val[3:5])
        parameters = [int(i) for i in list(first_val[:3])[::-1]]

        # print("\nNew loop!")
        # print("opcode:", opcode)
        # print("params:", parameters)
        # print("intcode:", intcode[counter:])
        # print("counter:", counter)

        if opcode == 99:
            return output

        if opcode == 1:
            if parameters[0] == 0:
                pos1 = intcode[counter + 1]
                val1 = intcode[pos1]
            else:
                val1 = intcode[counter + 1]
            if parameters[1] == 0:
                pos2 = intcode[counter + 2]
                val2 = intcode[pos2]
            else:
                val2 = intcode[counter + 2]
            pos_out = intcode[counter + 3]
            intcode[pos_out] = val1 + val2
            counter += 4
            
        if opcode == 2:
            if parameters[0] == 0:
                pos1 = intcode[counter + 1]
                val1 = intcode[pos1]
            else:
                val1 = intcode[counter + 1]
            if parameters[1] == 0:
                pos2 = intcode[counter + 2]
                val2 = intcode[pos2]
            else:
                val2 = intcode[counter + 2]
            pos_out = intcode[counter + 3]
            intcode[pos_out] = val1 * val2
            counter += 4

        if opcode == 3:
            pos = intcode[counter + 1]
            intcode[pos] = my_input
            my_input = input2
            counter += 2

        if opcode == 4:
            if parameters[0] == 0:
                pos = intcode[counter + 1]
                output = intcode[pos]
            else:
                output = intcode[counter + 1]
            print("OUTPUT:", output)
            counter += 2

        if opcode == 5:
            if parameters[0] == 0:
                pos1 = intcode[counter + 1]
                val1 = intcode[pos1]
            else:
                val1 = intcode[counter + 1]
            if val1 != 0:
                if parameters[1] == 0:
                    pos2 = intcode[counter + 2]
                    val2 = intcode[pos2]
                else:
                    val2 = intcode[counter + 2]
                counter = val2
            else:
                counter += 3

        if opcode == 6:
            if parameters[0] == 0:
                pos1 = intcode[counter + 1]
                val1 = intcode[pos1]
            else:
                val1 = intcode[counter + 1]
            if val1 == 0:
                if parameters[1] == 0:
                    pos2 = intcode[counter + 2]
                    val2 = intcode[pos2]
                else:
                    val2 = intcode[counter + 2]
                counter = val2
            else:
                counter += 3

        if opcode == 7:
            if parameters[0] == 0:
                pos1 = intcode[counter + 1]
                val1 = intcode[pos1]
            else:
                val1 = intcode[counter + 1]
            if parameters[1] == 0:
                pos2 = intcode[counter + 2]
                val2 = intcode[pos2]
            else:
                val2 = intcode[counter + 2]
            # if parameters[2] == 0:
            #     pos3 = intcode[counter + 3]
            #     val3 = intcode[pos3]
            # else:
            #     val3 = intcode[counter + 3]
            val3 = intcode[counter + 3]
            if val1 < val2:
                intcode[val3] = 1
            else:
                intcode[val3] = 0
            counter += 4

        if opcode == 8:
            if parameters[0] == 0:
                pos1 = intcode[counter + 1]
                val1 = intcode[pos1]
            else:
                val1 = intcode[counter + 1]
            if parameters[1] == 0:
                pos2 = intcode[counter + 2]
                val2 = intcode[pos2]
            else:
                val2 = intcode[counter + 2]
            # if parameters[2] == 0:
            #     pos3 = intcode[counter + 3]
            #     val3 = intcode[pos3]
            # else:
            #     val3 = intcode[counter + 3]
            val3 = intcode[counter + 3]
            if val1 == val2:
                intcode[val3] = 1
            else:
                intcode[val3] = 0
            counter += 4

    return intcode


def run_amps(phases, intcode):
    output = 0
    for phase in phases:
        output = parse_intcode(copy.copy(intcode), int(phase), output)
    return output


if __name__ == "__main__":

    with open("input.txt") as f:
        text_intcode = f.read()
        list_intcode = text_intcode.split(",")
        intcode = [int(i) for i in list_intcode]

    # intcode = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0] # 43210

    perms = [''.join(p) for p in permutations("01234")]
    best_val = 0
    best_perm = None
    for p in perms:
        val = run_amps(list(p), copy.copy(intcode))
        if val > best_val:
            best_val = val
            best_perm = p

    print("Best thruster signal:", best_val)
    print("Best phase setting:", best_perm)

        