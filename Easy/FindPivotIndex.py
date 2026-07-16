from typing import List
'''
Problem: Find Pivot Index
Number: 80
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(1)
URL: https://leetcode.com/problems/find-pivot-index
Topics: Array, Prefix Sum
'''
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left = 0
        summa = sum(nums)
        for i in range(len(nums)):
            right = summa - left - nums[i]
            if left == right:
                return i
            left += nums[i]
        return -1

s = Solution()
n1 = [1,7,3,6,5,6]
n2 = [1,2,3]
n3 = [2,1,-1]
print(s.pivotIndex(n1))
print(s.pivotIndex(n2))
print(s.pivotIndex(n3))
            