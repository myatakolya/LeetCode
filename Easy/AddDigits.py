'''
Problem: Add Digits
Number: 89
Difficulty: Easy
Time Complexity: O(1)
Space Complexity: O(1)
URL: https://leetcode.com/problems/add-digits
Topics: Math, Simulation
'''
class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        return 1 + (num - 1)% 9