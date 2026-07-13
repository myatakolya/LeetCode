from typing import List
'''
Problem: Set Mismatch
Number: 33
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(n)
URL: https://leetcode.com/problems/set-mismatch
Topics: Array, Hash Table, Math
'''
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        count = [0]*len(nums)
        for i in nums:
            count[i-1] += 1
        return [count.index(2)+1,count.index(0)+1]
        