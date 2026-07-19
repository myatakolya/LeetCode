from typing import List
'''
Problem: Search Insert Position
Number: 126
Difficulty: Easy
Time Complexity: O(log(n))
Space Complexity: O(1)
URL: https://leetcode.com/problems/search-insert-position
Topics: Array, Binary Search
'''
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left,right = 0,len(nums)
        while left < right:
            mid = (left + right)//2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left
