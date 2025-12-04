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
                if str_code[0:max_dupe_len] == str_code[max_dupe_len:]:
                    print(f"  bad code found: {str_code}")
                    total += code

                for c in range(0,len(str_code)):
                   #print(f"  total_len: {total_len} | checking pos: {c} code checking: {str_code}")
                    #if str_code[c] == '0':
                    #    continue
                    for i in range(1,total_len-1):
                        print(f"    checking dupe len: {i} at pos: {c} code checking: {str_code}")
                        dupe_check = str_code[c:c+i]
                        # keep checking forward
                        for j in range(0,total_len):
                            cc = c+i+(j*i)

                            compare_check = str_code[cc:cc+i+(j*i)]
                            print(f"code: {code} comparing dupe_check: {dupe_check} with compare_check: {compare_check} at pos: {cc}")
                            if dupe_check == compare_check:
                                print(f"  bad code found: {str_code} dupe_check: {dupe_check} | compare_check: {compare_check}")
                                total += code
                        #print(f"checking code: {str_code} | dupe_check: {dupe_check} | compare_check: {compare_check} ")
                        #print(f"    checking dupe_check: {dupe_check} in code: {str_code}")

                    #print(f"  total_len: {total_len} | checking dupe len: {c} code checking: {str_code}")



    print(f"Total sum bad codes: {total}\n")
    return total

def parse(raw_input):
    lines = text_2_csv_array(raw_input)
    return lines
