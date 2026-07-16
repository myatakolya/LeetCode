from typing import List
'''
Problem: Missing Number
Number: 90
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(1)
URL: https://leetcode.com/problems/missing-number
Topics: Array, Math, Bit Manipulation
'''
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        summa = sum(nums)
        return (n * (n+1))//2 - summa