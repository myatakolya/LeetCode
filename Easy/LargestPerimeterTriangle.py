from typing import List
'''
Problem: Largest Perimeter Triangle
Number: 121
Difficulty: Easy
Time Complexity: O(n*log(n))
Space Complexity: O(n)
URL: https://leetcode.com/problems/largest-perimeter-triangle
Topics: Array, Sorting, Greedy
'''
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        max_per = 0
        for a,b,c in zip(nums, nums[1:], nums[2:]):
            if (a + b > c):
                max_per = max(max_per, a+b+c)
        if max_per:
            return max_per
        return 0