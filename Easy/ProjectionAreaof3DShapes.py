from typing import List
'''
Problem: Projection Area of 3D Shapes
Number: 65
Difficulty: Easy
Time Complexity: O(n²)
Space Complexity: O(1)
URL: https://leetcode.com/problems/projection-area-of-3d-shapes
Topics: Array, Math, Geometry
'''
class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        n = len(grid)
        XY = 0
        YZ = sum(max(grid[i][j] for i in range(n)) for j in range(n))
        ZX = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] > 0:
                    XY += 1
            ZX += max(grid[i])
        return XY + YZ + ZX