from typing import List
'''
Problem: Largest Rectangle in Histogram
Number: 44
Difficulty: Hard
Time Complexity: O(n)
Space Complexity: O(n)
URL: https://leetcode.com/problems/largest-rectangle-in-histogram
Topics: Array, Stack, Monotonic Stack
'''
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0
        n = len(heights)
        
        for i in range(n):
            while stack and heights[stack[-1]] > heights[i]:
                height = heights[stack.pop()]
                width = i - stack[-1] - 1 if stack else i
                res = max(res,height*width)
            stack.append(i)
        
        while stack:
            height = heights[stack.pop()]
            width = n - stack[-1] - 1 if stack else n
            res = max(res,height*width)
        return res