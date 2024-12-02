import general_functions

init_list = general_functions.read_file(r"C:\Users\Tom.Brooks\OneDrive - BJSS Ltd\Documents\Coding\AoC-2022\Day_6.txt")
init_string = str(init_list[0])

#look through string
#find the first time four characters occur which are all different
#the marker occurs AFTER the fourth character
#in bvwbjplbgvb the first unique four are vwbj, which requires 5 chars to be processed, answer 5
def find_different_set(string, check_num_chars):
    unique_four = False
    temp_str = ""
    end_ind = check_num_chars
    start_ind = end_ind - check_num_chars
    for num in range(len(string)):
        temp_str = string[start_ind:end_ind]
        test_set = set(temp_str)
        if len(test_set) == check_num_chars:
            return end_ind
            break
        else:
            end_ind += 1
            start_ind += 1

#answer to part 1
print(find_different_set(init_string, 4))

#answer to part 2
print(find_different_set(init_string, 14))