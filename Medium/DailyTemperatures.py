from typing import List
'''
Problem: Daily Temperatures
Number: 43
Difficulty: Medium
Time Complexity: O(n)
Space Complexity: O(n)
URL: https://leetcode.com/problems/daily-temperatures
Topics: Array, Stack, Monotonic Stack
'''
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)-1,-1,-1):
            
            while stack and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()
            
            if stack:
                res[i] = abs(stack[-1] - i)
            
            stack.append(i)
        return res
        