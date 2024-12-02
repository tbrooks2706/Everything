import general_functions
from copy import deepcopy

#https://adventofcode.com/2020/day/6

#each row in file is a person, people are in groups separated by blank lines
#each letter represents a question; if it appears in a string, it means the person answered Yes to that question
#count how many questions were answered Yes by each group (not person) - duplicates are not counted
#if a group contains 4 people, and they all only answer Yes to a, the total Yes questions for that group is 1
#return the sum of counts for every group on the plane

class Group:
    def __init__(self, group_list) -> None:
        self.yes_answers = group_list
        self.people_count = len(group_list)
        self.unique_answers = self.get_unique_answers()
        self.common_answers = self.get_common_answers()
    
    def get_unique_answers(self):
        big_string = ""
        for answer in self.yes_answers:
            big_string += answer
        dedupe = "".join(set(big_string))
        return dedupe

    def get_common_answers(self):
        alphabet = general_functions.alphabet
        everyone_yes = ""
        for letter in alphabet:
            add_it = True
            for person in self.yes_answers:
                if letter not in person:
                    add_it = False
            if add_it == True:
                everyone_yes += letter
        return everyone_yes

def read_file(file_path):
    with open(file_path) as txt_file:
        init_list = []
        group_list = []
        last_group = []
        for line in txt_file:
            if line != "\n":
                group_list.append(line.replace("\n", ""))
                last_group = group_list
            else:
                init_list.append(group_list)
                group_list = []
        init_list.append(last_group)
    return init_list

def sum_all_yes_counts(input_list):
    total_unique_yes = 0
    total_common_yes = 0
    for lst in input_list:
        this_group = Group(lst)
        total_unique_yes += len(this_group.unique_answers)
        total_common_yes += len(this_group.common_answers)
    return [total_unique_yes, total_common_yes]

init_list = read_file(r"C:\Users\Tom.Brooks\OneDrive - BJSS Ltd\Documents\Coding\AoC\AoC-2020\Day_6.txt")

part_1_answer = sum_all_yes_counts(init_list)[0]
print(part_1_answer)

part_2_answer = sum_all_yes_counts(init_list)[1]
print(part_2_answer)