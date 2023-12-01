import general_functions
import copy

#https://adventofcode.com/2023/day/1

#summary and instructions
#every string contains numbers and letters
#use first number and last number from each string to form a single 2 digit number (eg245asgh8 -> 28)
#if there's only one number, repeat it (abc1de -> 11)
#sum all 2 digit numbers from all strings

init_list = general_functions.read_file(r"C:\Users\Tom.Brooks\OneDrive - BJSS Ltd\Documents\Coding\AoC\AoC-2023\Day_1_test_pt2.txt")
print(init_list)

number_dict = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}

class CalibrationLine:
    def __init__(self, string) -> None:
        self.full_string = string
        self.edited_string = self.replace_words_with_numbers(self.full_string)
        self.letters = self.separate_string(self.edited_string)[0]
        self.numbers = self.separate_string(self.edited_string)[1]
        self.value = int(self.numbers[0] + self.numbers[-1])

    #######need to change this function so it runs through the string left to right, instead of looking for the numbers in number order#######
    ######"zoneight" changes to "z1ight", "eightwothree" -> "8wo3", "xtwone3" -> "x2ne3" (it picks up the "two" not the "one") ########
    
    def replace_words_with_numbers(self, input_string):
        new_string = copy.deepcopy(input_string)
        for key, value in number_dict.items():
            new_string = new_string.replace(key, value)
        return new_string

    def separate_string(self, input_string):
        letters = ""
        numbers = ""
        for char in input_string:
            try:
                test = int(char)
            except:
                letters += char
            else:
                numbers += char
        return [letters, numbers]

def sum_values(input_list):
    total = 0
    for item in input_list:
        this_line = CalibrationLine(item)
        total += this_line.value
    return total

part_1_answer = sum_values(init_list)
print(part_1_answer)

# part_2_answer = pass
# print(part_2_answer)