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