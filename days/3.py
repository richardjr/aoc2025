from libs.loaders import text_2_int_arrays

def part_a(input_data):
    total = 0
    for line in input_data:
        print(line)
        # find the higest value in the line
        highest = 0
        for i in range(1,len(line)-1):
            if line[i] > line[highest]:
                highest = i
        # find then next highest value in the line
        next_highest = highest+1
        for i in range(next_highest+1,len(line)):
            if line[i] > line[next_highest]:
                next_highest = i

        print(f"Highest value in line: {line[highest]}  index {highest} \n")
        print(f"Next highest value in line: {line[next_highest]}  index {next_highest} \n")
        print(f"Total: {line[highest]}{line[next_highest]}\n")
        total += line[highest] * 10 + line[next_highest]
    print(f"Final Total Sum: {total}\n")
    return total


def parse(raw):
    return text_2_int_arrays(raw)