from typing import List
class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        seen_digits = [0]*10
        for i in digits:
            seen_digits[i] += 1
        seen = [False]*1000
        for i in range(100,1000,2):
            copy = seen_digits.copy()
            hundreds = i//100
            dozens = (i%100)//10
            units = i % 10
            copy[hundreds] -= 1
            copy[dozens] -= 1
            copy[units] -= 1
            if copy[hundreds] >= 0 and copy[dozens] >= 0 and copy[units] >= 0:
                seen[i] = True
            
        return seen.count(True)