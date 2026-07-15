from typing import List
'''
Problem: Two Sum
Number: 55
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(n)
URL: https://leetcode.com/problems/two-sum
Topics: Array, Hash Table
'''
from collections import Counter
class Solution:
    #Time Complexity: O(n²)
    #Space Complexity: O(1)
    def twoSum_1(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        if n == 2:
            return [0,1]
        p1,p2 = 0,1
        while p1 < len(nums)-1:
            cur_sum = target - nums[p1]
            while p2 < len(nums):
                if nums[p2] == cur_sum:
                    return [p1,p2]
                p2 += 1
            p1 += 1
            p2 = p1+1
    
    #Time Complexity: O(n)
    #Space Complexity: O(n)
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()
        for i in range(len(nums)):
            cur_target = target-nums[i]
            if cur_target in seen:
                return [seen[cur_target],i]
            else:
                seen[nums[i]] = i
        
                
        
    