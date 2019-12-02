
import copy

def parse_intcode(intcode):

    counter = 0
    while True:

        opcode = intcode[counter]

        if opcode == 99:
            break

        else:

            pos1 = intcode[counter + 1]
            if pos1 >= len(intcode):
                return []

            pos2 = intcode[counter + 2]
            if pos2 >= len(intcode):
                return []

            pos_out = intcode[counter + 3]
            if pos_out >= len(intcode):
                return []

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

        ## Part 1.
        input_intcode = copy.copy(intcode)
        input_intcode[1] = 12
        input_intcode[2] = 2
        out_intcode = parse_intcode(input_intcode)
        print("At position 0:", out_intcode[0])

        ## Part 2:
        for noun in range(100):
            for verb in range(100):

                input_intcode = copy.copy(intcode)
                input_intcode[1] = noun
                input_intcode[2] = verb

                out_intcode = parse_intcode(input_intcode)

                if out_intcode and out_intcode[0] == 19690720:
                    print("noun =", noun)
                    print("verb =", verb)
                    print("100 * noun + verb =", 100 * noun + verb)


