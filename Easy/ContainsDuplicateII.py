from typing import List
'''
Problem: Contains Duplicate II
Number: 86
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(n)
URL: https://leetcode.com/problems/contains-duplicate-ii
Topics: Array, Hash Table, Sliding Window
'''
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {}
        for i in range(len(nums)):
            if nums[i] in seen and (i-seen[nums[i]]) <= k:
                return True
            seen[nums[i]] = i
        return False
                