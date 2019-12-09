
import copy
from itertools import permutations

def parse_intcode(intcode, input1, input2):

    my_input = input1

    counter = 0
    output = None
    c = 0
    while True:
        c += 1
        # if c > 50:
        #     return

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
            # SET STATE TO FINISHED
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
            # SET STATE TO WAITING....

            my_input = input2
            counter += 2

        if opcode == 4:
            if parameters[0] == 0:
                pos = intcode[counter + 1]
                output = intcode[pos]
            else:
                output = intcode[counter + 1]
                return output
            print("OUTPUT:", output)
            counter += 2

        if opcode == 5:
            if parameters[0] == 0:
                pos1 = intcode[counter + 1]
                val1 = intcode[pos1]
            else:
                val1 = intcode[counter + 1]
            if val1 != 0:
                val2 = intcode[counter + 2]
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

    return output


def run_amps(phases, intcode):
    output = 0
    print("\n\n\nNEW PHASE SETTINGS")
    print(phases)
    for phase in phases:
        output = parse_intcode(intcode, int(phase), output)
    return output


if __name__ == "__main__":

    # with open("input.txt") as f:
    #     text_intcode = f.read()
    #     list_intcode = text_intcode.split(",")
    #     intcode = [int(i) for i in list_intcode]

    intcode = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
    # 139629729
    # 9,8,7,6,5

    perms = [''.join(p) for p in permutations("56789")]
    # perms = ["98765"]
    best_val = 0
    best_perm = None
    for p in perms:
        p = list(p)
        ps = [p[0]] + [0] + p[1:] + p + p + p + p + p
        val = run_amps(ps, copy.copy(intcode))
        if val > best_val:
            best_val = val
            best_perm = p

    print("Best thruster signal:", best_val)
    print("Best phase setting:", best_perm)

        