import general_functions

#abc = opponent RA, PB, SC (0)
#xyz = you RPS (1RX, 2PY, 3SZ)
#result = 6W, 3D, 0L

#part 1 function - calculate result score based on pre-determined shape
def calculate_result_part_one(game):
    opp = game[0]
    you = game[2]
    if opp == "A":
    #rock
        if you == "X":
            #rock therefore draw
            return 3 + 1
        if you == "Y":
            #paper therefore win
            return 6 + 2
        else:
            #scissors therefore loss
            return 0 + 3
    if opp == "B":
    #paper
        if you == "X":
            #rock therefore loss
            return 0 + 1
        if you == "Y":
            #paper therefore draw
            return 3 + 2
        else:
            #scissors therefore win
            return 6 + 3
    else:
    #scissors
        if you == "X":
            #rock therefore win
            return 6 + 1
        if you == "Y":
            #paper therefore loss
            return 0 + 2
        else:
            #scissors therefore draw
            return 3 + 3

#part 2 function - calculate result score based on pre-determined result
def calculate_result_part_two(game):
    opp = game[0]
    you = game[2]
    if opp == "A":
    #rock
        if you == "X":
            #lose therefore scissors
            return 0 + 3
        if you == "Y":
            #draw therefore rock
            return 3 + 1
        else:
            #win therefore paper
            return 6 + 2
    if opp == "B":
    #paper
        if you == "X":
            #lose therefore rock
            return 0 + 1
        if you == "Y":
            #draw therefore paper
            return 3 + 2
        else:
            #win therefore scissors
            return 6 + 3
    else:
    #scissors
        if you == "X":
            #lose therefore paper
            return 0 + 2
        if you == "Y":
            #draw therefore scissors
            return 3 + 3
        else:
            #win therefore rock
            return 6 + 1

def calculate_scores_one(list):
    running_total = 0
    for game in list:
        running_total += calculate_result_part_one(game)
    return running_total

def calculate_scores_two(list):
    running_total = 0
    for game in list:
        running_total += calculate_result_part_two(game)
    return running_total

init_list = general_functions.read_file(r"C:\Users\Tom.Brooks\OneDrive - BJSS Ltd\Documents\Coding\AoC-2022\Day_2.txt")
part_1_result = calculate_scores_one(init_list)
print(part_1_result)
part_2_result = calculate_scores_two(init_list)
print(part_2_result)