import general_functions
import copy

#https://adventofcode.com/2023/day/1

#summary and instructions
#every string contains numbers and letters
#use first number and last number from each string to form a single 2 digit number (eg245asgh8 -> 28)
#if there's only one number, repeat it (abc1de -> 11)
#sum all 2 digit numbers from all strings

class CalibrationLine:
    def __init__(self, string) -> None:
        self.full_string = string
        self.edited_string = self.replace_words_with_numbers(self.full_string)
        self.letters1 = self.separate_string(self.full_string)[0]
        self.numbers1 = self.separate_string(self.full_string)[1]
        try:
            self.value1 = int(self.numbers1[0] + self.numbers1[-1])
        except:
            self.value1 = 0
        self.letters2 = self.separate_string(self.edited_string)[0]
        self.numbers2 = self.separate_string(self.edited_string)[1]
        try:
            self.value2 = int(self.numbers2[0] + self.numbers2[-1])
        except:
            self.value2 = 0

    def replace_words_with_numbers(self, input_string):
        new_string = copy.deepcopy(input_string)
        for key, value in number_dict.items():
            new_string = new_string.replace(key, key+value+key)
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
    total1 = 0
    total2 = 0
    for item in input_list:
        this_line = CalibrationLine(item)
        total1 += this_line.value1
        total2 += this_line.value2
    return [total1, total2]

init_list = general_functions.read_file(r"C:\Users\Tom.Brooks\OneDrive - BJSS Ltd\Documents\Coding\AoC\AoC-2023\Day_1.txt")
number_dict = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}

answers = sum_values(init_list)
print(answers)