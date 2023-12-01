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

def check_max_children(input_list):
    list1 = []
    for rule in input_list:
        this_rule = Rule(rule)
        list1.append(this_rule.number_of_types_inside)
    list1.sort()
    return list1

all_colours = get_colour_list(init_list)
all_adjectives = get_adjective_list(init_list)
all_bag_types = get_bag_types(all_colours, all_adjectives)
#print(all_bag_types)

class Rule:
    def __init__(self, input_string) -> None:
        self.string = input_string
        self.word_list = input_string.split()
        #self.print_words()
        self.container = str(self.word_list[0]+" "+self.word_list[1])
        self.empty = self.check_empty()
        self.number_of_types_inside = self.count_different_types_inside()
        self.list_types_inside = self.set_different_types_inside()

    def check_empty(self):
        if self.word_list[4] == "no":
            return True
        return False
    
    def print_words(self):
        ind = 0
        for word in self.word_list:
            print(ind, ":", word)
            ind += 1

    def count_different_types_inside(self):
        count = 0
        if self.empty == False:
            count = self.string.count("bag") - 1
        return count
    
    def set_different_types_inside(self):
        #pick words out of word list
        #ind 5,6, 9,10, 13,14, 17,18
        child_list = []
        if self.number_of_types_inside >= 1:
            child_list.append(str(self.word_list[5]+" "+self.word_list[6]))
        if self.number_of_types_inside >= 2:
            child_list.append(str(self.word_list[9]+" "+self.word_list[10]))
        if self.number_of_types_inside >= 3:
            child_list.append(str(self.word_list[13]+" "+self.word_list[14]))
        if self.number_of_types_inside == 4:
            child_list.append(str(self.word_list[17]+" "+self.word_list[18]))
        return child_list

class BagType:
    def __init__(self, name, parents=None, children=None):
        self.name = name
        self.parents = parents
        self.children = children
        #print("Parents:",self.parents)
        #print("Children:",self.children)

    def __repr__(self) -> str:
        return self.name
    
node1 = BagType("shiny gold", ["muted yellow", "plain red"], ["dark black", "dull brown"])
    
########## am getting somewhere with this - next step is to make a function which finds all the colour combinations in the rest of the string - not including the container ############
########## put them in a list as the ones this bag type contains ###########
######### each node needs to know about all of its parents AND all of its children #########

example_rule = Rule("light lime bags contain 1 posh silver bag, 5 clear orange bags, 2 light olive bags, 3 dull maroon bags.")
print(example_rule.number_of_types_inside)
#print(example_rule.list_types_inside)

x_parents_dict = {"shiny gold": ["muted yellow", "dull red"]}
x_children_dict = {"muted yellow": ["bright green", "shiny gold"]}

def create_children_dictionary(input_list):
    child_dict = {}
    for rule in input_list:
        this_rule = Rule(rule)
        child_dict[this_rule.container] = this_rule.list_types_inside
    return child_dict

def create_parents_dictionary(input_list):
    par_dict = {}
    for bag_type in all_bag_types:
        parents = []
        for parent, children in children_dict.items():
            if bag_type in children:
                parents.append(parent)
        par_dict[bag_type] = parents
    return par_dict

children_dict = create_children_dictionary(init_list)
parents_dict = create_parents_dictionary(init_list)
#print(parents_dict)

def find_all_parents(bag_type):
    #start with entry in parentsdict
    #for each entry, add parents
    #then add parents of those parents
    full_list = parents_dict[bag_type]
    for parent in full_list:
        for grandparent in parents_dict[parent]:
            if grandparent not in full_list:
                full_list.append(grandparent)
            find_all_parents(grandparent)
    return full_list

print(find_all_parents("shiny gold"))

part_1_answer = len(find_all_parents("shiny gold"))
print("Part 1:",part_1_answer)
        
        

