from typing import List
'''
Problem: Gray Code
Number: 101
Difficulty: Medium
Time Complexity: O(2ⁿ)
Space Complexity: O(2ⁿ)
URL: https://leetcode.com/problems/gray-code
Topics: Math, Backtracking, Bit Manipulation
'''
class Solution:
    def grayCode(self, n: int) -> List[int]:
        res = []
        for i in range((1<<n)):
            res.append(i ^ (i >> 1))
        return res