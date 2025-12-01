
from libs.loaders import  text_2_line_array

min = 0
max = 99

def part_a(input_data):
    total_lines = 0
    position = 50
    total_zeros = 0

    for line in input_data:
        total_lines += 1
        direction = line[0] == 'L' and -1 or 1
        print(f"Processing line: {line} | Current position: {position}")
        print(f"Direction: {'Left' if direction == -1 else 'Right'}")
        steps = int(line[1:])
        position += direction * steps
        # clamp until position is within min/max
        while position < min or position > max:
            if position < min:
                position = max + ( position +1 )
                print("Hit minimum clap.")
            elif position > max:
                position = 0 + ((position -1) - max)
                print("Hit maximum clap.")
            print(f"Steps: {steps} | New position: {position}\n")
        if position == 0:
            print("Reached position 0, count.\n")
            total_zeros += 1


    print(f"Total lines counted: {total_lines}\n")
    print(f"Total times position 0 reached: {total_zeros}\n")
    return total_zeros

def part_b(input_data):
    total_lines = 0
    position = 50
    total_zeros = 0

    for line in input_data:
        total_lines += 1
        direction = line[0] == 'L' and -1 or 1
        print(f"Processing line: {line} | Current position: {position}")
        print(f"Direction: {'Left' if direction == -1 else 'Right'}")
        steps = int(line[1:])

        # clamp until position is within min/max
        for i in range(steps):
            position += direction
            if position < min:
                position = max + ( position +1 )
                print("Hit minimum boundary.")
            elif position > max:
                position = 0 + ((position -1) - max)
                print("Hit maximum boundary.")
            if position == 0:
                print("Reached position 0, count.\n")
                total_zeros += 1


    print(f"Total lines counted: {total_lines}\n")
    print(f"Total times position 0 reached: {total_zeros}\n")
    return total_zeros

def parse(raw_input):
    lines = text_2_line_array(raw_input)
    return lines


