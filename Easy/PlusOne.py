from typing import List
'''
Problem: Plus One
Number: 46
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(1)
URL: https://leetcode.com/problems/plus-one
Topics: Array, Math, Simulation
'''
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1,-1,-1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            elif digits[i] == 9:
                digits[i] = 0
        return [1] + digits
                
                
            

        