import general_functions

#https://adventofcode.com/2023/day/3

#summary and instructions
#any number adjacent to a symbol, even diagonally, is an engine "part number". any number not adjacent to a symbol is not a part number
#numbers can only be on one line, and read horizontally not vertically or diagonally
#sum all numbers which are part numbers

#find x,y positions of the end two numbers of each number (for 4016 find the x,y of the 4 and the 6)
    #look at chars in the range above and below
    #look at chars left (of the leftmost) and right (of the rightmost) in same row
    #look at chars above and below the L and R chars (or to the right and left of the above and below ranges)
    #set min and max row/column for all the above to stop it erroring out

init_list = general_functions.read_file(r"C:\Users\Tom.Brooks\OneDrive - BJSS Ltd\Documents\Coding\AoC\AoC-2023\Day_3_test.txt")

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]

class Grid:
    def __init__(self, input_list) -> None:
        self.full_grid = input_list
        self.part_sum = self.create_numbers()

    def create_numbers(self):
        sum_part_numbers = 0
        y = 0
        for row in self.full_grid:
            x = 0
            start_new = True
            for char in row:
                if start_new == True:
                    try:
                        test = int(char)
                    except:
                        x += 1
                        continue
                    else:
                        this_number = Number(self.full_grid, x, y)
                        if this_number.part_number == True:
                            sum_part_numbers += int(this_number.number)
                        start_new = False
                        x += 1
                else:
                    try:
                        test = int(char)
                    except:
                        start_new = True
                        x += 1
                    else:
                        x += 1
                        continue
            y += 1
        return sum_part_numbers

class Number:
    min_x = 0
    min_y = 0
    max_x = 9 #139 #9
    max_y = 9 #139 #9

    def __init__(self, grid, x_left, y) -> None:
        self.grid = grid
        self.x_left = x_left
        self.y = y
        self.x_right = self.find_coordinates()[1]
        self.number = self.find_coordinates()[0]
        self.range_here = [[self.x_left, self.x_right], self.y]
        self.range_above = [[self.x_left, self.x_right], max(self.y - 1, Number.min_y)]
        self.range_below = [[self.x_left, self.x_right], min(self.y + 1, Number.max_y)]
        self.range_left = [max(self.x_left - 1, Number.min_x), self.y]
        self.range_right = [min(self.x_right + 1, Number.max_x), self.y]
        self.range_up_left = [max(self.x_left - 1, Number.min_x), max(self.y - 1, Number.min_y)]
        self.range_below_left = [max(self.x_left - 1, Number.min_x), min(self.y + 1, Number.max_y)]
        self.range_up_right = [min(self.x_right + 1, Number.max_x), max(self.y - 1, Number.min_y)]
        self.range_below_right = [min(self.x_right + 1, Number.max_x), min(self.y + 1, Number.max_y)]
        self.surrounding = self.find_surrounding_characters()
        self.part_number = self.is_part_number()

    def find_coordinates(self):
        number = ""
        for char in self.grid[self.y][self.x_left:]:
            try:
                test = int(char)
            except:
                break
            else:
                number += char
        x_right = self.x_left + len(number) - 1
        return [number, x_right]
    
    def find_surrounding_characters(self):
        char_dict = {
            "above": "",
            "below": "", 
            "left": "", 
            "right": "", 
            "diag": "", 
            }
        #above
        string_above = ""
        for x in range(self.range_above[0][0], self.range_above[0][1] + 1):
            char = find_char_at(x, self.range_above[1], self.grid)
            string_above += char
            char_dict["above"] = string_above
        #below
        string_below = ""
        for x in range(self.range_below[0][0], self.range_below[0][1] + 1):
            char = find_char_at(x, self.range_below[1], self.grid)
            string_below += char
            char_dict["below"] = string_below
        #left right
        char_dict["left"] = find_char_at(self.range_left[0], self.range_left[1], self.grid)
        char_dict["right"] = find_char_at(self.range_right[0], self.range_right[1], self.grid)
        #diag
        string_diag = ""
        string_diag += find_char_at(self.range_up_left[0], self.range_up_left[1], self.grid)
        string_diag += find_char_at(self.range_up_right[0], self.range_up_right[1], self.grid)
        string_diag += find_char_at(self.range_below_left[0], self.range_below_left[1], self.grid)
        string_diag += find_char_at(self.range_below_right[0], self.range_below_right[1], self.grid)
        char_dict["diag"] = string_diag
        return char_dict
    
    def is_part_number(self):
        string = "".join(list(self.surrounding.values()))
        symbols = ""
        for char in string:
            if char not in numbers:
                symbols += char
        if len(symbols) > 0:
            return True
        return False      

def find_char_at(x, y, grid):
    return grid[y][x]

example_grid = Grid(init_list)

part_1_answer = example_grid.part_sum
print("Part 1:", part_1_answer)

# part_2_answer = 0
# print(part_2_answer)