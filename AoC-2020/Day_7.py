import general_functions
from copy import deepcopy

#https://adventofcode.com/2020/day/7

#input file is a list of rules about which types of bags are allowed to contain which other bags
#it is nested - bag a can contain bags b and c, and bag b can contain d e and f - bag a can therefore contain all of bcdef indirectly
#find how many different bag 

#automate a full map of what can contain what, from the input
    #do it first as a dict, then class from the dict

#pattern - <adjective> <colour> bags contain <int> <adjective> <colour> bag/bags, <int> <adjective> <colour> bag/bags [ up to 4 repeats ]

init_list = general_functions.read_file(r"C:\Users\Tom.Brooks\OneDrive - BJSS Ltd\Documents\Coding\AoC\AoC-2020\Day_7_test.txt")
print(init_list)

def get_colour_list(input_list):
    colours = []
    for rule in input_list:
        colours.append(rule.split()[1])
    return list(set(colours))

def get_adjective_list(input_list):
    adjectives = []
    for rule in input_list:
        adjectives.append(rule.split()[0])
    return list(set(adjectives))

def get_bag_types(colours, adjectives):
    type_list = []
    for colour in colours:
        for adjective in adjectives:
            type_list.append(""+adjective+" "+colour)
    return type_list

all_colours = get_colour_list(init_list)
all_adjectives = get_adjective_list(init_list)
all_bag_types = get_bag_types(all_colours, all_adjectives)
#print(all_bag_types)

class Rule:
    def __init__(self, input_string) -> None:
        self.string = input_string
        self.word_list = input_string.split()
        self.container = str(self.word_list[0]+" "+self.word_list[1])
        self.empty = self.check_empty()
        self.number_of_types_inside = self.set_different_types_inside()

    def check_empty(self):
        if self.word_list[4] == "no":
            return True
        return False

    def set_different_types_inside(self):
        count = 0
        if self.empty == False:
            count = self.string.count("bag") - 1
        return count
    
########## am getting somewhere with this - next step is to make a function which finds all the colour combinations in the rest of the string - not including the container ############
########## put them in a list as the ones this bag type contains ###########

##### can I use class inheritance to solve this problem? #########

example_rule = Rule("dotted black bags contain no other bags")
print(example_rule.number_of_types_inside)