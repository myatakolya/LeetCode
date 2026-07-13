from typing import List
'''
Problem: Shuffle the Array
Number: 31
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(n)
URL: https://leetcode.com/problems/shuffle-the-array
Topics: Array, Simulation
'''
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []
        for i in range(n):
            res.append(nums[i])
            res.append(nums[n+i])
        return res
        
        
        