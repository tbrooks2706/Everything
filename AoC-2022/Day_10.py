import general_functions
import math

#part 2 doesn't quite work - displays a grid close but not legible enough. I looked up the answer on Reddit

init_list = general_functions.read_file(r"C:\Users\Tom.Brooks\OneDrive - BJSS Ltd\Documents\Coding\AoC-2022\Day_10.txt")
cut_list = init_list[:10]
init_grid = general_functions.create_grid(40,6)
part2_list = general_functions.create_blank_list(".", 240)

class Cycle_Set:
    def __init__(self, num, start_x, instruction):
        self.start_x = start_x
        self.num = num
        self.instruction = instruction
        if instruction != "noop":
            self.add_x = int(instruction[5:])
    
    def __repr__(self):
        return self.num
    
    def end_x(self):
        new_x = 0
        if self.instruction == "noop":
            new_x = self.start_x
        else:
            new_x = self.start_x + self.add_x
        return new_x

    def cycle_ends(self):
        end_list = []
        cycle_count = self.num
        #optional first item is start_x if it's addx
        if self.instruction != "noop":
            end_list.append(self.start_x)
            cycle_count += 1
        #last item is always end_x
        end_list.append(self.end_x())
        cycle_count += 1
        #increase cycle count by 2 if addx, 1 if noop
        end_list.append(cycle_count)
        return end_list

class Signal:
    def __init__(self, cycle_num, x):
        self.x = int(x)
        self.cycle_num = int(cycle_num)
        self.strength = x * cycle_num
    
    def __repr__(self):
        return str(self.cycle_num)

def create_list_of_cycle_ends(input_list):
    #including starting value of X as index 0
    end_list = [1]
    cycle_count = 1
    for instruction in input_list:
        new_cycles = Cycle_Set(cycle_count, end_list[-1], instruction)
        output_list = new_cycles.cycle_ends()
        cycle_count = output_list.pop()
        for item in output_list:
            end_list.append(item)
    return end_list
list_of_x = create_list_of_cycle_ends(init_list)
#during cycle 1, value is index 0
#value at end of cycle 1 (and during cycle 2), is index 1

def find_signals(cycle_values, cycles_to_check):
    signals = []
    for cycle in cycles_to_check:
        new_signal = Signal(cycle, cycle_values[cycle - 1])
        signals.append(new_signal.strength)
    total = sum(signals)
    return total

total_signal_strength = find_signals(list_of_x, [20, 60, 100, 140, 180, 220])

#answer to part 1
print(total_signal_strength)

#######################PART TWO##########################
def print_grid(grid):
    for index in range(len(grid[0])):
        string = ""
        for num in range(len(grid)):
            string += grid[num][index]
        print(string)
#print_grid(init_grid)
#grid is arranged column then row
    #x then y
    #cycle 2 is grid[1][0]
    #cycle 40 is grid[39][0]
    #cycle 41 is grdi[0][1]
    #cycle 80 is grid[39][1]

#sprite is 3 pixels wide
#x = horizontal position of the middle of the sprite
#CRT draws one pixel per cycle
    #top row is cycles 1-40, second row 41-80 etc - 240 total
    #during cycle 1, draw position 0
#if any of the sprite's 3 pixels cover the dot being drawn in the current cycle, the dot becomes a #
    #if not, it stays a dot
#go through all 240 cycle x positions in list_of_x
    #if cycle_num == x-1, x, or x+1, replace . with #
    #else do nothing
#print out grid and it should form 8 letters

def draw_on_list(input_list, cycle_list):
    index = 0
    for cycle in range(1, len(cycle_list)):
        if cycle < 41:
            target = cycle
        elif cycle < 81:
            target = cycle - 40
        elif cycle < 121:
            target = cycle - 80
        elif cycle < 161:
            target = cycle - 120
        elif cycle < 201:
            target = cycle - 160
        else:
            target = cycle - 200
        target -= 1
        print("cycle",cycle,"index:",index,"target:",target,"x value:",cycle_list[index])
        if target in [cycle_list[index - 1], cycle_list[index], cycle_list[index + 1]]:
            input_list[index] = "#"
        index += 1
    return input_list
draw_on_list(part2_list, list_of_x)

def print_list_as_grid(input_list):
    #shape of grid hard coded for now
    print("".join(input_list[:40]))
    print("".join(input_list[40:80]))
    print("".join(input_list[80:120]))
    print("".join(input_list[120:160]))
    print("".join(input_list[160:200]))
    print("".join(input_list[200:]))
print_list_as_grid(part2_list)

def draw_on_grid(grid, cycle_list):
    column = 0
    row = 0
    for cycle in range(0, len(cycle_list)):
        #print("cycle",cycle,"column:",column,"row:",row)
        if cycle in [cycle_list[column - 1], cycle_list[column], cycle_list[column + 1]]:
            grid[column][row] = "#"
        if column == len(grid) - 1:
            column = 0
            row += 1
        else:
            column += 1
    return grid
#new_grid = draw_on_grid(init_grid, list_of_x)
#print_grid(new_grid)
#print(len(init_grid))
