##NOTE
##have now realised the below approach relies on each folder having a unique name, which it turns out they don't. rage quitting, might come back to it at some point in the future.

import general_functions
import copy

init_list = general_functions.read_file(r"C:\Users\Tom.Brooks\OneDrive - BJSS Ltd\Documents\Coding\AoC-2022\Day_7.txt")
print(init_list)

mini_list = init_list[:50]
#print(mini_list)

class File:
    def __init__(self, name):
        self.name = name
        self.size = 0
    
    def calculate_size(self):
        self.size = int(self.name.split()[0])
        return self.size
    
    def __repr__(self):
        return self.name

class Dir:
    #example input '$ cd gdjmt'
    def __init__(self, name):
        self.name = name
        file_list = []
        dir_list = []
    
    def __repr__(self):
        return self.name

    #each instance starting with "$ cd" which is followed immediately by "$ ls", sum all the file sizes after it until the next "$ cd"
    def take_cut(self):
        cut_list = []
        for num in range(0,len(init_list)-1):
            #if input_list[num] == self.name and input_list[num + 1] == '$ ls':
            if init_list[num] == self.name and init_list[num + 1] == '$ ls':
                first_index = init_list.index(str(self))
                current_index = copy.deepcopy(first_index) + 2
                current_value = init_list[current_index]
                while current_value[:4] != "$ cd":
                    current_value = init_list[current_index]
                    if current_value[:4] == "$ cd":
                        break
                    cut_list.append(current_value)
                    current_index += 1
        return cut_list

    #make a list of only the files (not subdirectories)
    def list_files(self):
        file_list = []
        for item in Dir.take_cut(self):
            if item[:4] in ["$ cd", "$ ls", "dir "]:
                continue
            else:
                file_list.append(item)
        return file_list

    #return total size of all the files in this dir, not including subdirs
    def total_file_size(self):
        total = 0
        for this_file in Dir.list_files(self):
            new_file = File(this_file)
            total += new_file.calculate_size()
        return total

    #make a list of only the subdirectories, in cd not dir format, to iterate through
    def list_subdirs(self):
        subdir_list = []
        for item in Dir.take_cut(self):
            if item[:4] == "dir ":
                subdir_list.append("$ cd "+item[4:])
            else:
                continue
        return subdir_list

    #return total size of files in all subdirs, not including directly in this folder
    def total_subdir_size(self):
        total = 0
        for item in Dir.list_subdirs(self):
            #print(type(item))
            directory = item
            print(directory)
            #total += Dir.total_file_size(item)
        return total

example_directory = Dir('$ cd fcv')
#print(example_directory.take_cut())
#print(example_directory.list_files())
print(example_directory.total_file_size())
print(example_directory.list_subdirs())
print(example_directory.total_subdir_size())


def list_directories(input_list):
    dir_list = []
    dir_dict = {}
    for item in input_list:
        if item[0] == "d":
            dir_list.append("$ cd "+str(item[4:]))
    unique_set = set(dir_list)
    for item in unique_set:
        dir_dict[item] = 0
    return dir_dict
#print(list_directories(init_list))

#look through initlist
#each instance starting with "$ cd" which is followed immediately by "$ ls", sum all the file sizes after it until the next "$ cd"
#THEN
#need a way to know which dirs are in which dirs

def find_directory_size(string):
    for item in init_list:
        pass