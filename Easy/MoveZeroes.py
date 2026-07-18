from typing import List
'''
Problem: Move Zeroes
Number: 100
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(1)
URL: https://leetcode.com/problems/move-zeroes
Topics: Array, Two Pointers
'''

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        write = 0
        for read in range(n):
            if nums[read] != 0:
                nums[write], nums[read] = nums[read], nums[write]
                write += 1
            

s = Solution()
nums = [0,1,0,3,12]
nums2 = [0]
nums3 = [1,0,2]
print(s.moveZeroes(nums))
print(s.moveZeroes(nums2))
print(s.moveZeroes(nums3))
print(nums)
print(nums2)
print(nums3)