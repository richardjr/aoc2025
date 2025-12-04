from libs.loaders import text_2_char_arrays

def part_a(input_data):
    total = 0
    max_x = len(input_data[0])
    max_y = len(input_data)
    # deep copy input data
    copy_input = [list(row) for row in input_data]
    for y in range(0, max_y):
        for x in range(0,max_x):
            if input_data[y][x] == '.':
                continue
            occupied_count = 0
            # check all 8 directions
            for dy in [-1,0,1]:
                for dx in [-1,0,1]:
                    # check out of bounds
                    if y+dy < 0 or y+dy >= max_y or x+dx < 0 or x+dx >= max_x:
                        continue
                    if dy == 0 and dx == 0:
                        continue
                    if input_data[y+dy][x+dx] == '@':
                        occupied_count += 1
            if occupied_count <4:
                total +=1
                copy_input[y][x] = 'x'
    print(f"Total rolls: {total}\n")
    print(f"Final State:\n")
    for line in copy_input:
        print(''.join(line))
    print("\n")
    return total

def part_b(input_data):
    total = 0
    max_x = len(input_data[0])
    max_y = len(input_data)
    # deep copy input data
    found_changes = 0
    while True:
        for y in range(0, max_y):
            for x in range(0,max_x):
                if input_data[y][x] == '.' or input_data[y][x] == 'x':
                    continue
                occupied_count = 0
                # check all 8 directions
                for dy in [-1,0,1]:
                    for dx in [-1,0,1]:
                        # check out of bounds
                        if y+dy < 0 or y+dy >= max_y or x+dx < 0 or x+dx >= max_x:
                            continue
                        if dy == 0 and dx == 0:
                            continue
                        if input_data[y+dy][x+dx] == '@':
                            occupied_count += 1
                if occupied_count <4:
                    total +=1
                    input_data[y][x] = 'x'
                    found_changes += 1
        if not found_changes:
            break
        print(f"Roll changes found: {found_changes}\n")
        found_changes = 0
    print(f"Total rolls: {total}\n")
    print(f"Final State:\n")
    for line in input_data:
        print(''.join(line))
    print("\n")
    return total

def parse(raw):
    return text_2_char_arrays(raw)
