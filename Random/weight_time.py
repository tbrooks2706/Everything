import csv
from datetime import * 

with open(r"C:\Users\Tom.Brooks\OneDrive - BJSS Ltd\Documents\Coding\Random\weight_time2.csv") as new_csv:
    csv_obj = csv.DictReader(new_csv)
    line_count = 0
    new_dict = {}
    for row in csv_obj:
        new_dict[line_count] = row
        line_count += 1

print(new_dict)

class RunningTime:
    def __init__(self, time, date, weight):
        self.time = time
        self.date = date
        self.weight = weight

#tested and class initialisation works
#time1 = RunningTime("00:29:21", "28/11/2022", "113.7")
#print(time1.date)

#format data so time is time, date is date, weight is int

#create time items as objects of RunningTime class (as per time1 above)

#create function for time per weight inside class

#do some kind of print as part of a sentence "At DATE, your time was X per kg"

#write the sentences to a txt file and export it?

#write the time per weight as a new column inside the original CSV?





