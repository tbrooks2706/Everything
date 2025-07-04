#polar bear game
#coop
#4 animals - fox, rabbit, bear, penguin
#6 ice pillars
#3 locations - pool, bridge, igloo
#roll die
    #1/3 chance - ice cube (remove 1 ice pillar support from bridge)
    #1/3 chance - bridge (if >=1 animal on pool, move 1 animal from pool to bridge; else nothing happens)
    #1/3 chance - igloo (if >=1 animal on bridge, move 1 animal from bridge to igloo; else nothing happens)
#keep rolling die till either:
    #victory condition - all 4 animals to igloo
    #defeat condition - all supports removed from bridge

#to track:
    #where is each animal
    #how many supports left in bridge

import random

animals = {0:"Penguin", 1:"Fox", 2:"Rabbit", 3:"Bear"}
die_dict = {4:"Ice Cube", 5:"Bridge", 6:"Igloo"}
locations = {7:"Pool", 8:"Bridge", 9:"Igloo"}
result_type = {10:"Remove a cube!", 11: "Move", 12: "Nothing happens!"}

class Animal:
    def __init__(self, name) -> None:
        self.name = name
        self.location_start = 0
        self.location_now = 0

class Board:
    def __init__(self) -> None:
        #need to set all these once, then not reset them every roll
        self.cubes = 6
        self.pool_animals = [0, 1, 2, 3]
        self.bridge_animals = []
        self.igloo_animals = []

class Roll:
    def __init__(self, cubes, pool, bridge, igloo) -> None:
        self.num = self.roll_die()
        self.face = die_dict[self.num]
        self.cubes = cubes
        self.pool_animals = pool
        self.bridge_animals = bridge
        self.igloo_animals = igloo
        self.result_code = self.resolve_result()[0]
        self.result_description = self.resolve_result()[1]
        self.animal_locations = self.find_animal_locations()
        self.print_result()

    def roll_die(self):
        roll = random.randint(4,6)
        return roll
    
    def resolve_result(self):
        #options:
            #remove one ice cube (how many are there are the start and end?)
            #move one animal to igloo (if animals on bridge, if multiple which animal)
            #move one animal to bridge (if animals on pool, if multiple which animal)
            #nothing
        moved_animal = ""
        moved_to = ""
        result_main_type = ""
        code_result = [result_main_type, moved_animal, moved_to]
        desc_result = ""

        #rolled ice cube
        if self.num == 4:
            self.cubes -= 1
            result_main_type = 0
            desc_result = result_type[10]
        #rolled bridge
        elif self.num == 5:
            if self.pool_animals == []:
                result_main_type = 2
                desc_result = result_type[12]
            else:
                moved_animal = self.pool_animals.pop(0)
                moved_to = 8
                self.bridge_animals.append(moved_animal)
                result_main_type = 1
                desc_result = result_type[11]+" "+animals[moved_animal]+" to "+locations[moved_to]
        #rolled igloo
        else:
            if self.bridge_animals == []:
                result_main_type = 2
                desc_result = result_type[12]
            else:
                moved_animal = self.pool_animals.pop(0)
                moved_to = 9
                self.bridge_animals.append(moved_animal)
                result_main_type = 1
                desc_result = result_type[11]+" "+animals[moved_animal]+" to "+locations[moved_to]

        #return a coded version for use in function, and a descriptive version for printing/debugging
        return [code_result, desc_result]

    def find_animal_locations(self):
        loc_list = []
        for num in [0,1,2,3]:
            if num in self.pool_animals:
                loc_list.append(7)
            elif num in self.bridge_animals:
                loc_list.append(8)
            else:
                loc_list.append(9)
        return loc_list

    def print_result(self):
        print("-----------------------------------")
        print("Roll:",self.face)
        print("Action:",self.result_description)
        #print("Penguin:",self.animal_locations[0],"Fox:",self.animal_locations[1],"Rabbit:",self.animal_locations[2],"Bear:",self.animal_locations[3])
        for num in [0,1,2,3]:
            print(animals[num],":",locations[self.animal_locations[num]])
        pass

this_roll = Roll(6, [0, 1, 2, 3], [], [])
#print(this_roll.face)

# bear_loc = 0
# fox_loc = 0
# rabbit_loc = 0
# penguin_loc = 0

# def roll_die():
#     roll = random.randint(1,3)
#     return roll

# def die_result():


#print(die_dict[roll_die()])
