from libs.loaders import get_file_with_mode, cmd_line_arguments
from aocd import submit


if __name__ == "__main__":
    day, mode, part, sub = cmd_line_arguments()
    input_data = get_file_with_mode(day=day, mode=mode)

    day_module = __import__(f'days.{day}', fromlist=[''])

    parsed = day_module.parse(input_data)
    module_name = f"part_{part}"
    func = getattr(day_module, module_name)
    result = func(parsed)
    if sub == True and mode == 'live':
        submit(result, part=part, day=day, year=2025)