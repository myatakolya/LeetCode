from typing import List
'''
Problem: Majority Element
Number: 119
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(n)
URL: https://leetcode.com/problems/majority-element
Topics: Array, Hash Table, Divide and Conquer, Sorting
'''
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        seen = {}
        n = len(nums)/2
        for i in nums:
            if i in seen:
                seen[i] += 1
                if seen[i] > n:
                    return i
            else:
                seen[i] = 1
                if seen[i] > n:
                    return i
        
        