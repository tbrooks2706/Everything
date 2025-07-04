import general_functions
from copy import deepcopy

#https://adventofcode.com/2024/day/2

#summary and instructions
#puzzle input is a set of reports, one report per line
#each line is a list of numbers called levels, separated by spaces
#work out how many reports are safe
#a report is safe if:
    #levels are all increasing (12789) or all decreasing (86421); AND
    #any two adjacent levels differ by 1-3 (so no duplicates and none more than 3 apart)

class ReportSet:
    def __init__(self, input_list) -> None:
        self.original = input_list
        self.variations = self.find_variations()
        self.any_safe = self.test_variations()

    def find_variations(self):
        ind = 0
        var_list = [self.original]
        for num in self.original:
            orig = deepcopy(self.original)
            orig.pop(ind)
            variation = orig
            var_list.append(variation)
            ind += 1
        return var_list

    def test_variations(self):
        any_true = False
        for var in self.variations:
            this_report = Report(var)
            if this_report.is_safe == True:
                any_true = True
                break
        return any_true

class Report:
    def __init__(self, input_list) -> None:
        self.report = input_list
        self.inc_dec_results = self.check_direction()
        self.is_increasing = self.inc_dec_results[0]
        self.is_decreasing = self.inc_dec_results[1]
        self.diff_match = self.check_diff()
        self.is_safe = self.check_safe()
    
    def check_direction(self):
        inc = True
        dec = True
        ind = 1
        for level in self.report:
            if ind > len(self.report) - 1:
                break
            step = self.report[ind] - self.report[ind-1]
            ind += 1
            if step <= 0:
                inc = False
            if step >= 0:
                dec = False
            if inc == False and dec == False:
                break
        return (inc, dec)
    
    def check_diff(self):
        diff = True
        ind = 1
        while ind < len(self.report):
            level_diff = abs(self.report[ind] - self.report[ind-1])
            if 1 <= level_diff <= 3:
                ind += 1
                continue
            else:
                diff = False
                break
        return diff
    
    def check_safe(self):
        safe = True
        if (self.is_increasing == True or self.is_decreasing == True) and self.diff_match == True:
            pass
        else:
            safe = False
        return safe

def check_reports_1(input_list):
    count_safe = 0
    for report in input_list:
        this_report = Report(report)
        if this_report.is_safe == True:
            count_safe += 1
    return count_safe

def check_reports_2(input_list):
    count_safe = 0
    for report in input_list:
        this_set = ReportSet(report)
        if this_set.any_safe == True:
            count_safe += 1
    return count_safe

def clean_reports(input_list):
    clean = []
    for report in input_list:
        clean.append([int(x) for x in report.split(" ")])
    return clean

init_list = general_functions.read_file(r"C:\Users\tbroo\OneDrive\Documents\Code\Everything\AoC-2024\Day_2.txt")
clean_list = clean_reports(init_list)

#answers
part_1 = check_reports_1(clean_list)
print(part_1)

part_2 = check_reports_2(clean_list)
print(part_2)