from libs.loaders import text_2_2_lists
def part_a(input_data):
    list1 = input_data[0]
    list2 = input_data[1]
    #print(list1)
    #print(list2)
    fresh_items = 0
    range_aray = []
    for item in list1:
        range_start, range_end = item.split('-')
        range_start = int(range_start)
        range_end = int(range_end)
        #print(f"Range start: {range_start} | Range end: {range_end}")
        range_aray.append([range_start, range_end])
    range_aray = sorted(range_aray, key=lambda x: x[0])
    for item in list2:
        item = int(item)
        for range_item in range_aray:
            check_start, check_end = range_item
            if item >= check_start and item <= check_end:
                print(f"Item {item} found in range {check_start}-{check_end} Freash.")
                fresh_items += 1
                break

    print(f"Total fresh items found: {fresh_items}\n")
    #print(f"Final Range String:\n{range_aray}\n")
    return fresh_items

def part_b(input_data):
    list1 = input_data[0]
    fresh_items = 0
    range_aray = []
    for item in list1:
        range_start, range_end = item.split('-')
        range_start = int(range_start)
        range_end = int(range_end)
        range_aray.append([range_start, range_end])
    range_aray = sorted(range_aray, key=lambda x: x[0])
    merged_ranges = []
    for current in range_aray:
        # check if current range overlaps with the last merged range
        if not merged_ranges or current[0] > merged_ranges[-1][1]:
            merged_ranges.append(current)
        else:
            merged_ranges[-1][1] = max(merged_ranges[-1][1], current[1])
    print(f"Merged Ranges: {merged_ranges}\n")
    for i in merged_ranges:
        start, end = i
        fresh_items += (end - start) + 1
    print(f"Total fresh items found: {fresh_items}\n")
    return fresh_items



def parse(raw):
    return text_2_2_lists(raw)