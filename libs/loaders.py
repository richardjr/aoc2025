from aocd import get_data
import argparse


def cmd_line_arguments():
    parser = argparse.ArgumentParser(description="Advent of Code Data Loader")
    parser.add_argument('--day', type=int, required=True, help='Day of the challenge (1-12)')
    parser.add_argument('--mode', type=str, choices=['test', 'live'], default='test', help='Mode to load data: test or live')
    parser.add_argument('--part', type=str, choices=['a', 'b'], default='a', help='Part of the challenge: a or b')
    parser.add_argument('--submit', action='store_true', help='Submit the answer to AoC (only in live mode)')
    args = parser.parse_args()
    return args.day, args.mode, args.part, args.submit

def get_file_with_mode(day, mode='test'):
    print(f"Loading data for Day {day}, Mode: {mode}...\n")
    file_path = f'data/{day}-{mode}.txt'
    # does it exist and is test? If so error out
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        if mode == 'test':
            raise FileNotFoundError(f"Test file not found: {file_path}")
        else:
            print("Fetching real data from AoC...")
            real_data = get_data(day=day, year=2025)
            with open(file_path, 'w') as file:
                file.write(real_data)
            return real_data



def text_2_line_array(data):
    print("Converting text to line array...\n")
    return data.strip().split('\n')

def text_2_csv_array(data):
    print("Converting text to CSV array...\n")
    return [line.split(',') for line in data.strip().split('\n')]

def text_2_int_arrays(data):
    print("Converting text to integer arrays...\n")
    lines = data.strip().split('\n')
    int_arrays = []
    for line in lines:
        int_array = [int(x) for x in line]
        int_arrays.append(int_array)
    return int_arrays

def text_2_char_arrays(data):
    print("Converting text to character arrays...\n")
    lines = data.strip().split('\n')
    char_arrays = []
    for line in lines:
        char_array = [x for x in line]
        char_arrays.append(char_array)
    return char_arrays

def text_2_2_lists(data):
    # file has two sections separated by blank line
    print("Converting text to 2 lists...\n")
    lines = data.strip().split('\n')
    list1 = []
    list2 = []
    current_list = list1
    for line in lines:
        if line.strip() == '':
            current_list = list2
            continue
        current_list.append(line)
    return list1, list2

def text_2_line_fixed(data):
    print("Converting text to fixed line array...\n")
    data=data.split('\n')
    #kill last empty line if exists
    if data[-1] == '':
        data = data[:-1]
    return data
