import general_functions

########################DOESN'T WORK RIGHT - looked up a solution on Reddit###########################

#input is a series of motions made by the head
init_list = general_functions.read_file(r"C:\Users\Tom.Brooks\OneDrive - BJSS Ltd\Documents\Coding\AoC-2022\Day_9.txt")
#print(init_list)

#rope with knot at each end - knots are head and tail
#grid is a very large (theoretically infinite?) 2 dimensional space for the rope to move in
    #size can be driven by just running the moves and seeing whether I get an index error
    #could do this as eg.
    #grid = [[".",".","#"],[".",".","."],[".",".","."]]
    #print(grid[0][1])
    #just use a loop to make a 500x500 grid and start at the centre?

#grid[x column[y row, y row, y row], x column[y row, y row, y row] etc]
#first number increase = movement to the right
#second number increase = movement down
working_grid = general_functions.create_grid(200,200)
#print(working_grid)

#rules:
#head and tail must always be touching (vert, horiz or diag) OR the head can cover the tail
#if head moves away from tail, tail moves towards it to keep up
#IMPORTANT if the head moves but is still touching (or on top of) the tail, the tail doesn't move
#head can move up down left right
#tail will move diagonally if it needs to, to make sure it stays touching the head
#they move simultaneously, so any move by the head moves the tail at the same time

#9 relative positions of head to tail - above left, above, above right, left, on top, right, below left, below, below right
#4 possible head moves - up, down, left, right
#therefore 36 possible combinations of situation - each one will trigger a tail move
#9 possible tail moves - up left, up, up right, left, (not move), right, down left, down, down right

#work out how to represent each of 9 possible tail moves in code


class Move:
    #dictionary of changes to the head's coordinates based on the move that it makes
    moves = {"L": [-1, 0], "R": [1, 0], "U": [0, -1], "D": [0, 1], "DL": [-1, 1], "DR": [1, 1], "UL": [-1, -1], "UR": [1, -1], "": [0, 0]}
    #print(moves["UL"][0])

    #dictionary of relative positions of head to tail, as xy coordinates
    #first key is relative number on the x axis (-1 is head to the left)
    #second key is relative number on the y axis (-1 is head above)
    relative_positions = {0: {0: "on top", -1: "above", 1: "below"}, -1: {0: "left", -1: "above left", 1: "below left"}, 1: {0: "right", -1: "above right", 1: "below right"}}

    #work out where the head and tail are at the start
    def __init__(self, direction, head_start, tail_start):
        self.direction = direction
        self.head_start = head_start
        self.tail_start = tail_start
        self.head_start_x = head_start[0]
        self.head_start_y = head_start[1]
        self.tail_start_x = tail_start[0]
        self.tail_start_y = tail_start[1]
        self.relative_head_position = Move.relative_positions[self.head_start_x - self.tail_start_x][self.head_start_y - self.tail_start_y]
        self.tail_end_x = self.tail_start_x + Move.moves[self.tail_move()][0]
        self.tail_end_y = self.tail_start_y + Move.moves[self.tail_move()][1]
        self.head_end_x = self.head_start_x + Move.moves[self.direction][0]
        self.head_end_y = self.head_start_y + Move.moves[self.direction][1]
        self.head_finish = [self.head_end_x, self.head_end_y]
        self.tail_finish = [self.tail_end_x, self.tail_end_y]
        
    #move head
    #def head_finish(self):
    #    self.head_end_x = self.head_start_x + Move.moves[self.direction][0]
    #    self.head_end_y = self.head_start_y + Move.moves[self.direction][1]
    #    return [self.head_end_x, self.head_end_y]
    
    #work out which direction the tail moves (based on move and relative position of head and tail before)
    def tail_move(self):
        tail_move = ""
        if self.direction == "U" and self.relative_head_position in ["above left", "above", "above right"]:
            if self.relative_head_position == "above left":
                tail_move = "UL"
            elif self.relative_head_position == "above":
                tail_move = "U"
            else:
                tail_move = "UR"
        elif self.direction == "D" and self.relative_head_position in ["below left", "below", "below right"]:
            if self.relative_head_position == "below left":
                tail_move = "DL"
            elif self.relative_head_position == "below":
                tail_move = "D"
            else:
                tail_move = "DR"        
        elif self.direction == "L" and self.relative_head_position in ["below left", "left", "above left"]:
            if self.relative_head_position == "below left":
                tail_move = "DL"
            elif self.relative_head_position == "left":
                tail_move = "L"
            else:
                tail_move = "UL"
        elif self.direction == "R" and self.relative_head_position in ["below right", "right", "above right"]:
            if self.relative_head_position == "below right":
                tail_move = "DR"
            elif self.relative_head_position == "right":
                tail_move = "R"
            else:
                tail_move = "UR"
        else:
            pass
        return tail_move

    #mark start and end tail coordinates as visited
    def execute(self):
        working_grid[self.tail_start_x][self.tail_start_y] = "#"
        working_grid[self.tail_end_x][self.tail_end_y] = "#"

#example_move = Move("L", [49, 50], [50, 51])
#example_move2 = Move("L", [48, 50], [49, 50])
#print(example_move.relative_head_position)
#print(example_move.head_finish)
#print(example_move.tail_move())
#print(example_move.tail_finish)
#example_move.execute()
#example_move2.execute()

class Move_Set:
    def __init__(self, direction, number_of_moves, head_start, tail_start):
        self.direction = direction
        self.number_of_moves = int(number_of_moves)
        self.head_start = head_start
        self.tail_start = tail_start
        self.head_finish = self.execute_all()[0]
        self.tail_finish = self.execute_all()[1]
    
    def execute_all(self):
        head = self.head_start
        tail = self.tail_start
        for move in range(self.number_of_moves):
            new_move = Move(self.direction, head, tail)
            new_move.execute()
            head = new_move.head_finish
            tail = new_move.tail_finish
        return [head, tail]

#example_set = Move_Set("U", "5", [50, 50], [50, 50])
#print(example_set.head_finish)

def make_all_moves(moves_list):
    head = [50, 50]
    tail = [50, 50]
    for set in moves_list:
        new_set = Move_Set(set[0], set[2:], head, tail)
        head = new_set.head_finish
        tail = new_set.tail_finish
    print(head, tail)
make_all_moves(init_list)

#then loop through entire grid - how many values marked as visited are there
def count_locations_visited(input_grid):
    counter = 0
    for column in input_grid:
        counter += column.count("#")
    return counter
print(count_locations_visited(working_grid))

def count_total_head_moves(moves_list):
    counter = 0
    for set in moves_list:
        counter += int(set[2:])
    return counter
#print(count_total_head_moves(init_list))