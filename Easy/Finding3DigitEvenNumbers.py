from typing import List
'''
Problem: Finding 3-Digit Even Numbers
Number: 9
Difficulty: Easy
Time Complexity: O(n) + O(1)
Space Complexity: O(1)
URL: https://leetcode.com/problems/finding-3-digit-even-numbers
Topics: Array, Hash Table, Enumeration, Sorting
'''

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
            
        return [i for i in range(len(seen)) if seen[i] == True]
            
        

i1 = [2,1,3,0]
i2 = [2,2,8,8,2]
i3 = [3,7,5]
solver = Solution()
print(solver.findEvenNumbers(i1))
print(solver.findEvenNumbers(i2))
print(solver.findEvenNumbers(i3))
