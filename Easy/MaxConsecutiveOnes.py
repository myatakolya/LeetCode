from typing import List

'''
Problem: Max Consecutive Ones
Number: 32
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(1)
URL: https://leetcode.com/problems/max-consecutive-ones
Topics: Array, Sliding Window
'''

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ones = 0
        current_ones = 0
        for i in nums:
            if i == 1:
                current_ones += 1
            else:
                max_ones = max(max_ones,current_ones)
                current_ones = 0
        return max(max_ones,current_ones)
    