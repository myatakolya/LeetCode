from typing import List
'''
Problem: Remove Duplicates from Sorted Array
Number: 125
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(1)
URL: https://leetcode.com/problems/remove-duplicates-from-sorted-array
Topics: Array, Two Pointers
'''
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1
        else:
            last_el = nums[0]
            k = 1
            position = 1
            for right in range(1,n):
                if nums[right] != last_el:
                    nums[position] = nums[right]
                    position += 1
                    k += 1
                    last_el = nums[right]
            return k
            