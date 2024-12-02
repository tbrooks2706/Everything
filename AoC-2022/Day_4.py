import general_functions

class Pair:
    def __init__(self, string):
        self.first_list = string.split(",")
        self.working_list = []
        for item in self.first_list:
            tmplist = item.split("-")
            for num in tmplist:
                self.working_list.append(int(num))

    def range2_contains_range1(self):
        #is bottom of pair 2, less than bottom of pair 1 AND top of pair 2, greater than top of pair 1
        if (self.working_list[2] <= self.working_list[0] and self.working_list[3] >= self.working_list[1]):
            stat1 = True
        else:
            stat1 = False
        return stat1

    def range1_contains_range2(self):
        #is bottom of pair 1, less than bottom of pair 2 AND top of pair 1, greater than top of pair 2
        if (self.working_list[0] <= self.working_list[2] and self.working_list[1] >= self.working_list[3]):
            stat1 = True
        else:
            stat1 = False
        return stat1
    
    def range_contains_range(self):
        if self.range1_contains_range2() == True or self.range2_contains_range1() == True:
            return True
        else:
            return False

    def range_overlap(self):
        test_1 = False
        test_2 = False
        #is either number in pair 1, in range of pair 2
        for num in self.working_list[:1]:
            if num >= self.working_list[2] and num <= self.working_list[3]:
                test_1 = True
        #is either number in pair 2, in range of pair 1
        for num in self.working_list[2:3]:
            if num >= self.working_list[0] and num <= self.working_list[1]:
                test_2 = True
        if test_1 == True or test_2 == True:
            return True
        else:
            return False
#end of class methods

#part 1 calc
def count_duplicating_pairs(list):
    counter = 0
    for item in list:
        two_elves = Pair(item)
        if two_elves.range_contains_range() == True:
            counter += 1
    return counter

#part 2 calc
def count_overlapping_pairs(list):
    counter = 0
    for item in list:
        two_elves = Pair(item)
        if two_elves.range_overlap() == True:
            counter += 1
    return counter

#execute code in one go
init_list = general_functions.read_file(r"C:\Users\Tom\OneDrive\Documents\Tom's Stuff\Hobbies\Coding\AoC-2022\Day_4.txt")
duplicate_count = count_duplicating_pairs(init_list)
overlap_count = count_overlapping_pairs(init_list)

#answer to part 1
print(duplicate_count)

#answer to part 2
print(overlap_count)