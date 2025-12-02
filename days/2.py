from libs.loaders import  text_2_csv_array

def part_a(input_data):
    total = 0
    for row in input_data:
        for item in row:
            min, max = item.split('-')
            for code in range(int(min), int(max)+1):
                str_code = str(code)
                #print(f"range check for code: {str_code}")
                total_len = len(str(str_code))
                max_dupe_len = total_len / 2
                # if there is a remainder we skip this one
                if max_dupe_len % 1 != 0:
                    #print(f"  skipping odd len code: {str_code}")
                    continue
                max_dupe_len = int(max_dupe_len)
                #print(f"  total_len: {total_len} | max_dupe_len: {max_dupe_len} code checking: {str_code}")
                if str_code[0] == '0':
                    continue
                #print(f"  checking code: {str_code} | first half: {str_code[0:max_dupe_len]} | second half: {str_code[max_dupe_len:]}")
                if str_code[0:max_dupe_len] == str_code[max_dupe_len:]:
                    print(f"  bad code found: {str_code}")
                    total += code


    print(f"Total sum bad codes: {total}\n")
    return total

def part_b(input_data):
    total = 0
    for row in input_data:
        for item in row:
            min, max = item.split('-')
            for code in range(int(min), int(max)+1):
                str_code = str(code)
                #print(f"range check for code: {str_code}")
                total_len = len(str_code)
                max_dupe_len = total_len // 2
                # if there is a remainder we skip this one
                for c in range(0,len(str_code)):
                    for i in range(2,max_dupe_len):
                        print(f"c{c}i{i}")
                        dupe_check = str_code[c:i]
                        compare_check = str_code[c+i:i]
                        print(f"  checking code: {str_code} | dupe_check: {dupe_check} | compare_check: {compare_check} ")
                        #print(f"    checking dupe_check: {dupe_check} in code: {str_code}")

                    #print(f"  total_len: {total_len} | checking dupe len: {c} code checking: {str_code}")



    print(f"Total sum bad codes: {total}\n")
    return total

def parse(raw_input):
    lines = text_2_csv_array(raw_input)
    return lines
