import general_functions
from collections import Counter

#https://adventofcode.com/2024/day/1

#summary and instructions
#puzzle input is two lists held up side by side - they should be the same
#find out how far apart the lists are
#pair up the smallest number in list A with smallest in list B, regardless of position in list
#find out difference (all positive regardless of which side is bigger)
#do the same for second smallest in A with second smallest in B
#add up all differences - answer part 1

def split_lists(input_list):
    list_a = []
    list_b = []
    
    def clean_list(input):
        clean_list = []
        for item in input:
            clean_item = [x for x in item.split("   ")]
            clean_list.append(clean_item)
        return clean_list
    
    def populate_a_and_b(input):
        for pair in input:
            list_a.append(int(pair[0]))
            list_b.append(int(pair[1]))
    
    populate_a_and_b(clean_list(input_list))
    list_a.sort()
    list_b.sort()
    return [list_a, list_b]

def find_difference(list_a, list_b):
    diff_list = []
    ind = 0
    for item in list_a:
        diff = abs(list_a[ind] - list_b[ind])
        diff_list.append(diff)
        ind += 1
    total_diff = sum(diff_list)
    return total_diff

def find_similarity_score(list_a, list_b):
    sim_list = []
    ind = 0
    b_counts = Counter(list_b)
    for item in list_a:
        sim_list.append(b_counts[item] * item)
        ind += 1
    total_score = sum(sim_list)
    return total_score    

init_list = general_functions.read_file(r"C:\Users\tbroo\OneDrive\Documents\Code\Everything\AoC-2024\Day_1.txt")
id_list_a = split_lists(init_list)[0]
id_list_b = split_lists(init_list)[1]

#answers
part_1 = find_difference(id_list_a, id_list_b)
print(part_1)

part_2 = find_similarity_score(id_list_a, id_list_b)
print(part_2)