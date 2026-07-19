from typing import List
'''
Problem: Matrix Diagonal Sum
Number: 115
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(1)
URL: https://leetcode.com/problems/matrix-diagonal-sum
Topics: Array, Matrix
'''
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        total = 0
        n = len(mat)
        for i in range(n):
            total += mat[i][i]
            total += mat[i][n - 1 - i]
        if n % 2 != 0:
            total -= mat[n//2][n//2]
        return total    