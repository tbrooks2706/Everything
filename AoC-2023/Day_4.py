import general_functions
from copy import deepcopy

#https://adventofcode.com/2023/day/4

#summary and instructions
#part 1
#numbers before the bar are winning numbers, numbers after the bar are your numbers
#1 match means 1 point, points double for each subsequent match within a line - so 3 matches 4 points, 4 matches 8 points
#part 2
#ignore points 
#card with x matches creates a copy of the next x cards - those copies themselves produce copies
#no card ever produces a copy of itself or a previous card, and no copy goes beyond the end of the list

class Card:
    def __init__(self, string) -> None:
        self.full_string = string
        self.id = int(string.split(":")[0].split()[1])
        self.winning_numbers = self.full_string.split(":")[1].split("|")[0].split()
        self.my_numbers = self.full_string.split(":")[1].split("|")[1].split()
        self.matches = self.match_numbers(self.winning_numbers, self.my_numbers)
        self.points = self.calculate_points(self.matches)
        
    def match_numbers(self, set_1, set_2):
        count = 0
        for num_1 in set_1:
            for num_2 in set_2:
                if num_1 == num_2:
                    count += 1
        return count

    def calculate_points(self, matches):
        points = 1
        if matches < 2:
            points = matches
        else:
            for match in range(2, matches + 1):
                points *= 2
        return points

def create_dict(num):
    blank_dict = {}
    for x in range(1, num + 1):
        blank_dict[x] = 1
    return blank_dict

def create_cards(input_list):
    total_points = 0
    card_dict = create_dict(len(init_list))
    for item in input_list:
        this_card = Card(item)
        total_points += this_card.points
        copies_owned = card_dict[this_card.id]
        cards_to_copy = [x for x in range(this_card.id + 1, this_card.id + this_card.matches + 1)] * copies_owned
        for id in cards_to_copy:
            card_dict[id] += 1
    total_copies = sum(list(card_dict.values()))
    return [total_points, total_copies]

init_list = general_functions.read_file(r"C:\Users\Tom.Brooks\OneDrive - BJSS Ltd\Documents\Coding\AoC\AoC-2023\Day_4.txt")

answers = create_cards(init_list)
print("Part 1:", answers[0])
print("Part 2:", answers[1])