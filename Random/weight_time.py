import csv

with open(r"C:\Users\Tom.Brooks\OneDrive - BJSS Ltd\Documents\Coding\Random\weight_time2.csv") as new_csv:
    #print(new_csv.read())
    csv_obj = csv.DictReader(new_csv)
    print(csv_obj)
    line_count = 0
    new_dict = {}
    for row in csv_obj:
        new_dict[line_count] = row
        line_count += 1
    #print(new_dict)

print (new_dict)




