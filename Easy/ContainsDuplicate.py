from typing import List
from collections import Counter
'''
Problem: Contains Duplicate
Number: 85
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(n)
URL: https://leetcode.com/problems/contains-duplicate
Topics: Array, Hash Table, Sorting
'''
class Solution:
    def containsDuplicate_1(self, nums: List[int]) -> bool:
        return not len(set(nums)) == len(nums)
    
    def containsDuplicate_2(self, nums: List[int]) -> bool:
        seen = set()
        for i in nums:
            if i in seen:
                return True
            seen.add(i)
        return False
    
