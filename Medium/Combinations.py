from typing import List
'''
Problem: Combinations
Number: 61
Difficulty: Medium
Time Complexity: O(C(n,k)*k)
Space Complexity: O(C(n,k)*k)
URL: https://leetcode.com/problems/combinations
Topics: Backtracking, Combinatorics
'''
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        
        def backtrack(start, path):
            if len(path) == k:
                res.append(path[:])
                return
            for i in range(start, n + 1):
                path.append(i)
                backtrack(i + 1, path)
                path.pop()
        
        backtrack(1, [])
        return res