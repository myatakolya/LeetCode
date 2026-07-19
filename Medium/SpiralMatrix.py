from typing import List
'''
Problem: Spiral Matrix
Number: 116
Difficulty: Medium
Time Complexity: O(m*n)
Space Complexity: O(1)
URL: https://leetcode.com/problems/spiral-matrix
Topics: Array, Matrix, Simulation
'''
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        res = []
        top, bottom = 0, len(matrix)-1
        left, right = 0, len(matrix[0])-1
        while top <= bottom and left <= right:
            #слева направо
            for j in range(left, right+1):
                res.append(matrix[top][j])
            top += 1
            #сверху вниз
            for i in range(top,bottom+1):
                res.append(matrix[i][right])
            right -= 1
            
            if top <= bottom:
                for j in range(right,left-1,-1):
                    res.append(matrix[bottom][j])
                bottom -= 1
            
            if left <= right:
                for i in range(bottom,top-1, -1):
                    res.append(matrix[i][left])
                left += 1
        return res
             
            

