from typing import List
'''
Problem: Unique 3-Digit Even Numbers
Number: 11
Difficulty: Easy
Time Complexity: O(n) + O(1)
Space Complexity: O(1)
URL: https://leetcode.com/problems/unique-3-digit-even-numbers
Topics: Array, Hash Table, Enumeration, Counting
'''
class Solution:
    def totalNumbers(self, digits: List[int]) -> List[int]:
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