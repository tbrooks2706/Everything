import general_functions
import numpy

#https://adventofcode.com/2023/day/2

#summary and instructions
#game - bag and cubes
#cubes red green or blue
#each game, elf hides x cubes of each colour in the bag, then grabs a random handful, shows them and puts them bag y number of times

#part 1
#which games would have been possible if the bag only contained:
    #12 red, #13 green, #14 blue
#sum IDs of all possible games

#part 2
#product of the minimum number of cubes in each bag in order to make the game possible

class Game:
    max_cubes = {
        "red": 12,
        "blue": 14,
        "green": 13
        }

    def __init__(self, input_string) -> None:
        self.original_string = input_string
        self.cleaned_data = self.clean_input(self.original_string)
        self.id = int(self.cleaned_data[0].split()[1])
        self.instructions = self.cleaned_data[1:]
        self.revealed = {
            "red": 0, 
            "blue": 0, 
            "green": 0
            }
        self.run_game()
        self.possible = self.determine_possible()
        self.revealed_power = numpy.prod(list(self.revealed.values()))

    def clean_input(self, input_string):
        s1 = input_string.split(":")
        s2 = s1[1].split(";")
        s3 = [s1[0]]
        for x in s2:
            lst = x.split(",")
            lst2 = []
            for a in lst:
                lst2.append(a.strip())
            s3.append(lst2)
        return s3
    
    def run_game(self):
        #do all rounds of game
        for round in self.instructions:
            self.run_next_round(round)

    def run_next_round(self, round):
        #run one round and update revealed values
        for reveal in round:
            colour = reveal.split()[1]
            number = int(reveal.split()[0])
            if number > self.revealed[colour]:
                self.revealed[colour] = number
    
    def determine_possible(self):
        for max_clr, max_num in Game.max_cubes.items():
            if self.revealed[max_clr] > max_num:
                return False
        return True

def sum_possible_games(input_list):
    total_possible_ids = 0
    total_powers = 0
    for game in input_list:
        this_game = Game(game)
        total_powers += this_game.revealed_power
        if this_game.possible == True:
            total_possible_ids += this_game.id
    return [total_possible_ids, total_powers]

init_list = general_functions.read_file(r"C:\Users\Tom.Brooks\OneDrive - BJSS Ltd\Documents\Coding\AoC\AoC-2023\Day_2.txt")
        
answers = sum_possible_games(init_list)
print("Part 1:", answers[0])
print("Part 2:", answers[1])