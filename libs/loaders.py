from aocd import data

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



def text_2_line_array(file_path):
    print(f"Converting {file_path} to line array format...\n")
    # Read the entire content of the file split into lines
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return lines