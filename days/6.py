from libs.loaders import text_2_line_fixed

def part_a(input_data):
    last_line = input_data[-1]
    print(f"Last line: '{last_line}'\n")
    # find the range between any non space characters in the last line
    start = 0
    columns = []
    operations = []
    while start < len(last_line):
        for i in range(start+1,len(last_line)+1):
            #print(f"Checking for start at index {i} | char '{last_line[i]}'")
            if i == len(last_line) or last_line[i] != ' ':
                end = i -1
                print(f"Start: {start} | End: {end}\n")
                columns.append( (start, end) )
                operations.append(last_line[start])
                start = end +1
                break


    print(f"Columns found: {columns}\n")
    print(f"Operations found: {operations}\n")

    total = 0
    index = 0
    for col in columns:
        start, end = col
        col_total = 0
        for line in input_data[:-1]:
            number = int(line[start:end+1])
            print(number)
            if operations[index] == '+':
                col_total += number
            elif operations[index] == '*':
                if col_total == 0:
                    col_total = number
                else:
                    col_total = col_total * number
            else:
                print(f"Unknown operation: {operations[index]}")
        print(f"Column total for operation '{operations[index]}': {col_total}\n")
        index += 1
        total += col_total
    print(f"Final Total Sum: {total}\n")
    return total


def part_b(input_data):
    last_line = input_data[-1]
    print(f"Last line: '{last_line}'\n")
    # find the range between any non space characters in the last line
    start = 0
    columns = []
    operations = []
    while start < len(last_line):
        for i in range(start+1,len(last_line)+1):
            #print(f"Checking for start at index {i} | char '{last_line[i]}'")
            if i == len(last_line) or last_line[i] != ' ':
                end = i -1
                print(f"Start: {start} | End: {end}\n")
                columns.append( (start, end) )
                operations.append(last_line[start])
                start = end +1
                break


    print(f"Columns found: {columns}\n")
    print(f"Operations found: {operations}\n")

    total = 0
    index = 0
    for col in columns:
        start, end = col
        col_total = 0
        for line in input_data[:-1]:
            # build the number from right to left within the slice
            digits = []
            for char in reversed(line[start:end+1]):
                if char.isdigit():
                    digits.append(char)
            number_str = ''.join(reversed(digits))  # keep numeric order, taken from right
            if not number_str:
                continue
            number = int(number_str)
            print(number)
            if operations[index] == '+':
                col_total += number
            elif operations[index] == '*':
                if col_total == 0:
                    col_total = number
                else:
                    col_total = col_total * number
            else:
                print(f"Unknown operation: {operations[index]}")
        print(f"Column total for operation '{operations[index]}': {col_total}\n")
        index += 1
        total += col_total
    print(f"Final Total Sum: {total}\n")
    return total
def parse(raw):
    return text_2_line_fixed(raw)