
def parse_intcode(intcode):

    counter = 0
    while True:

        opcode = intcode[counter]

        if opcode == 99:
            break

        else:

            pos1 = intcode[counter + 1]
            pos2 = intcode[counter + 2]
            pos_out = intcode[counter + 3]

            if opcode == 1:
                intcode[pos_out] = intcode[pos1] + intcode[pos2]
            elif opcode == 2:
                intcode[pos_out] = intcode[pos1] * intcode[pos2]
            else:
                raise ValueError("Invalid opcode.")

            counter += 4

    return intcode


if __name__ == "__main__":

    with open("input.txt") as f:

        text_intcode = f.read()
        list_intcode = text_intcode.split(",")
        intcode = [int(i) for i in list_intcode]

        intcode[1] = 12
        intcode[2] = 2

        out_intcode = parse_intcode(intcode)

        print("At position 0:", out_intcode[0])


