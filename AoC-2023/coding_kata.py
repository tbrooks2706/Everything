import unittest

class SomeTests(unittest.TestCase):
    def test_arr_1(self):
        self.assertEqual(find_arr([1, -2, 7, 2, 1, 3, 7, 1, 0, 2, 3], [2, -1, 1, 1, 1, 1, 2, 3, 3, 7, 7, 0], [-4, 4], "odd"), [1, 3], "Test 1 failed")
    
    def test_arr_2(self):
        self.assertEqual(find_arr([1, -2, 7, 2, 1, 3, 4, 7, 1, 0, 2, 3, 0, 4], [0, 4, 2, -1, 1, 1, 1, 1, 2, 3, 3, 7, 7, 0, 4], [-4, 4], "even"), [0, 2, 4], "Test 2 failed")

class Number:
    def __init__(self, integer, array_a, array_b, range, odd_even) -> None:
        self.value = integer
        self.array_a = array_a
        self.array_b = array_b
        self.range_limit = range
        self.odd_even = odd_even
        self.is_odd = self.value % 2 != 0
        self.count_in_a = self.array_a.count(self.value)
        self.count_in_b = self.array_b.count(self.value)
        self.in_range = self.range_limit[0] <= self.value <= self.range_limit[1]
        self.returned = self.return_valid()

    def return_valid(self):
        if self.count_in_a > 1 and self.count_in_b > 1 and self.in_range == True and self.meets_odd_criteria() == True:
            return True

    def meets_odd_criteria(self):
        if self.odd_even == "odd":
            return self.is_odd
        return not self.is_odd    

def find_arr(arrA, arrB, rng, wanted):
    #reduce numbers to search through - only search through ones in range, and odd/even
    if wanted == "odd":
        possibles = [x for x in range(rng[0], rng[1] + 1) if x % 2 != 0]
    else:
        possibles = [x for x in range(rng[0], rng[1] + 1) if x % 2 == 0]



    # matches = []
    # for num in possibles:
    #     #don't check number if it's already been added
    #     if num in matches:
    #         continue
    #     count_a = arrA.count(num)
    #     count_b = arrB.count(num)
    #     if count_a > 1 and count_b > 1:
    #         matches.append(num)
        #
        # this_num = Number(num_a, arrA, arrB, rng, wanted)
        # if this_num.returned == True:
        #     matches_in_range.append(this_num.value)
    return sorted(list(set(possibles)))

unittest.main()

#for x in range(0, 10)