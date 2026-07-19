'''
Problem: Count Odd Numbers in an Interval Range
Number: 118
Difficulty: Easy
Time Complexity: O(1)
Space Complexity: O(1)
URL: https://leetcode.com/problems/count-odd-numbers-in-an-interval-range
Topics: Math
'''
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if low % 2 == 0 and high % 2 == 0:
            return  (high - low - 1) - ((high - low - 1) // 2)
        elif (low % 2 != 0 and high % 2 == 0) or (low % 2 == 0 and high % 2 != 0):
            return ((high - low - 1) // 2) + 1
        else:
            return ((high - low - 1) // 2) + 2
            