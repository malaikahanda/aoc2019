
import copy

def parse_intcode(intcode, my_input):

    c = 0
    counter = 0
    output = None
    while True:
        c += 1

        first_val = str(intcode[counter])
        while len(first_val) != 5:
            first_val = "0" + first_val
        opcode = int(first_val[3:5])
        parameters = [int(i) for i in list(first_val[:3])[::-1]]

        print("\nNew loop!")
        print("opcode:", opcode)
        print("params:", parameters)
        print("intcode:", intcode[counter:])
        print("counter:", counter)

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


if __name__ == "__main__":
    # out = parse_intcode([
    #     3, 21,1008,21,8,20,1005,20,22,107,
    #     8,21,20,1006,20,31,1106,0,36,98,0,
    #     0,1002,21,125,20,4,20,1105,1,46,104,
    #     999,1105,1,46,1101,1000,1,20,4,20,
    #     1105,1,46,98,99], -100)
    # print(out)

    with open("input.txt") as f:
        text_intcode = f.read()
        list_intcode = text_intcode.split(",")
        intcode = [int(i) for i in list_intcode]

    out = parse_intcode(intcode, 5)
    print(out)

        