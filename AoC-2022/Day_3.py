import general_functions

init_list = general_functions.read_file(r"C:\Users\Tom.Brooks\OneDrive - BJSS Ltd\Documents\Coding\AoC-2022\Day_3.txt")

#cut_list = init_list[:12]
#print(cut_list)

#tried OOP at first but couldn't get it to work - come back later
#class Rucksack:
#    def __init__(self, contents):
#        self.contents = contents
#        self.split = len(contents)
#        self.first_half = contents[0]

#rucksack1 = Rucksack("fsHtVbjtqstBghhwwPBw")
#print(rucksack1.first_half())

#split each string into halves and find the character common to both halves
#part 1 only
def find_common_character(string):
    split_point = int(len(string) / 2)
    first_half = string[:split_point]
    second_half = string[split_point:]
    for char in first_half:
        if char in second_half:
            common = char
    return common

#find the common character for every string in the list, and concat them together
#part 1 only
def string_common_characters(list):
    common_string = ""
    for item in list:
        common_string += find_common_character(item)
    return common_string

#find the common characters from each group of 3 and concat them together
#part 2 only 
def find_group_string(big_list):
    ind = 0
    common = ""
    while ind <= (len(big_list) - 3):
        new_list = []
        new_list.append(big_list[ind])
        new_list.append(big_list[ind + 1])
        new_list.append(big_list[ind + 2])
        ind += 3
        for char in new_list[0]:
            if char in new_list[1] and char in new_list[2]:
                common += char
                break
        continue
    return common

#return scores based on a string of characters
#part 1 and part 2
def get_scores(string):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    full_alphabet = alphabet
    total_score = 0
    for letter in alphabet:
        full_alphabet += letter.upper()
    for char in string:
        score = full_alphabet.index(char) + 1
        total_score += score
    return total_score

#execute functions
common_characters_1 = string_common_characters(init_list)
common_characters_2 = find_group_string(init_list)
final_score = get_scores(common_characters_1)
group_score = get_scores(common_characters_2)

#answer to part 1
print(final_score)

#answer to part 2
print(group_score)