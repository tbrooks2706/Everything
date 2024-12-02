import general_functions
import copy

class Tree: 
    def __init__(self, row_number, column_number):
        self.row_number = int(row_number)
        self.column_number = int(column_number)
        self.row_column = [self.row_number, self.column_number]
        #hard coded the input lists for now - can parameterise later
        self.row_string = init_list[self.row_number]
        self.column_string = column_list[self.column_number]
        self.height = int(self.row_string[self.column_number])
        self.trees_to_left = self.row_string[:self.column_number]
        self.trees_to_right = self.row_string[self.column_number+1:]
        self.trees_above = self.column_string[:self.row_number]
        self.trees_below = self.column_string[self.row_number+1:]
    
    def __repr__(self):
        return self.row_column
        
    def visible_up(self):
        if self.row_number == 0:
            return True
        else:
            max_tree = 0
            for char in self.trees_above:
                if int(char) > max_tree:
                    max_tree = int(char)
            return self.height > max_tree

    def visible_down(self):
        if self.row_number == 98:
            return True
        else:
            max_tree = 0
            for char in self.trees_below:
                if int(char) > max_tree:
                    max_tree = int(char)
            return self.height > max_tree

    def visible_right(self):
        if self.column_number == 98:
            return True
        else:
            max_tree = 0
            for char in self.trees_to_right:
                if int(char) > max_tree:
                    max_tree = int(char)
            return self.height > max_tree

    def visible_left(self):
        if self.column_number == 0:
            return True
        else:
            max_tree = 0
            for char in self.trees_to_left:
                if int(char) > max_tree:
                    max_tree = int(char)
            return self.height > max_tree

    def is_visible(self):
        results = [self.visible_up(), self.visible_down(), self.visible_right(), self.visible_left()]
        if True in results:
            return True
        else:
            return False
    
    #calculate scenic score for tree - look backwards along the string for left and up directions 
    def scenic_score(self):
        score_left = 0
        score_right = 0
        score_up = 0
        score_down = 0
        if self.column_number != 0:
            for num in general_functions.reverse_string(self.trees_to_left):
                tree = int(num)
                score_left += 1
                if tree >= self.height:
                    break
        if self.column_number != 98:
            for num in self.trees_to_right:
                tree = int(num)
                score_right += 1
                if tree >= self.height:
                    break
        if self.row_number != 0:
            for num in general_functions.reverse_string(self.trees_above):
                tree = int(num)
                score_up += 1
                if tree >= self.height:
                    break
        if self.row_number != 98:
            for num in self.trees_below:
                tree = int(num)
                score_down += 1
                if tree >= self.height:
                    break
        return score_down * score_up * score_right * score_left
        
class Row:
    def __init__(self, row_number):
        self.row_number = int(row_number)
        self.name = init_list[self.row_number]
        self.length = len(self.name)
    
    def __repr__(self):
        return self.name

    def number_visible(self):
        iteration_counter = 0
        visible_counter = 0
        for num in self.name:
            new_tree = Tree(self.row_number, iteration_counter)
            if new_tree.is_visible() == True:
                visible_counter += 1
            iteration_counter += 1  
        return visible_counter
    
    def max_score_in_row(self):
        iteration_counter = 0
        max_score = 0
        for num in self.name:
            new_tree = Tree(self.row_number, iteration_counter)
            max_score = max(max_score, new_tree.scenic_score())
            iteration_counter += 1  
        return max_score

#create columns for use with the Row class to create trees
def create_columns(input_list):
    list_of_columns = []
    #assumes same number of rows as columns
    for item in range(len(input_list[0])):
        list_of_columns.append("")
    for string in input_list:
        char_index = 0
        for char in string:
            list_of_columns[char_index] += char
            char_index += 1
    return list_of_columns

#go through each row and add up how many in that row are visible
def find_visible_trees(list_of_rows):
    total = 0
    for num in range(len(list_of_rows)):
        this_row = Row(num)
        visible_in_row = this_row.number_visible()
        total += visible_in_row
    return total

#go through each row's highest scenic score, and return the highest scenic score in any row
def find_max_score(list_of_rows):
    max_score = 0
    for num in range(len(list_of_rows)):
        this_row = Row(num)
        row_top_score = this_row.max_score_in_row()
        max_score = max(max_score, row_top_score)
    return max_score

#execute functions
init_list = general_functions.read_file(r"C:\Users\Tom.Brooks\OneDrive - BJSS Ltd\Documents\Coding\AoC-2022\Day_8.txt")
column_list = create_columns(init_list)
total_visible_trees = find_visible_trees(init_list)
highest_scenic_score = find_max_score(init_list)

#answer to part 1
print(total_visible_trees)

#answer to part 2
print(highest_scenic_score)