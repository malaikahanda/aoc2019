
import copy

def parse_intcode(intcode, my_input):

    counter = 0
    output = None
    while True:

        first_val = str(intcode[counter])
        while len(first_val) != 5:
            first_val = "0" + first_val
        opcode = int(first_val[3:5])
        parameters = [int(i) for i in list(first_val[:3])[::-1]]

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
            counter += 2

        if opcode == 4:
            pos = intcode[counter + 1]
            output = intcode[pos]
            print(output)
            counter += 2

    return intcode


if __name__ == "__main__":

    with open("input.txt") as f:
        text_intcode = f.read()
        list_intcode = text_intcode.split(",")
        intcode = [int(i) for i in list_intcode]

    out = parse_intcode(intcode, 1)

        