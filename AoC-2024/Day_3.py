import general_functions
from collections import Counter
from copy import deepcopy

#https://adventofcode.com/2024/day/3

#summary and instructions
#puzzle input is a computer program, aiming to multiply some numbers
    #only the exact sequence mul(x,y) where x and y are 1-3 digit numbers is valid
    #Sequences like mul(4*, mul(6,9!, ?(12,34), or mul ( 2 , 4 ) do nothing
#find all the valid sequences from the input, multiply the pairs of numbers and add up the result

#use a regex for the recognition bit?

init_list = general_functions.read_file(r"C:\Users\tbroo\OneDrive\Documents\Code\Everything\AoC-2024\Day_2.txt")
regex = r"^mul\(\d{1,3},\d{1,3}\)$"

#answers
# part_1 = check_reports_1(clean_list)
# print(part_1)

# part_2 = check_reports_2(clean_list)
# print(part_2)