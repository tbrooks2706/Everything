import general_functions

#clean list of line breaks, change str to int
#add a final "" on the end so list_of_totals works below
def clean_list(list):
    new_working = list
    for item in new_working:
        if item != "":
            item = int(item)/1
    new_working.append("")
    return new_working

#create list of running totals, using "" as the separator, and sort values descending
def list_of_totals(list):
    totals = []
    running_total = 0
    for item in list:   
        if item == "":
            totals.append(running_total)
            running_total = 0
        else:
            running_total += int(item)
    totals.sort(reverse=True)
    return totals

#calling the functions all in one go
init_list = general_functions.read_file(r"C:\Users\Tom.Brooks\OneDrive - BJSS Ltd\Documents\Coding\AoC-2022\Day_1.txt")
working_list = clean_list(init_list)
final_totals = list_of_totals(working_list)
final_top_three = sum(final_totals[0:3])

#answer to part 1
print(max(final_totals))

#answer to part 2
print(final_top_three)