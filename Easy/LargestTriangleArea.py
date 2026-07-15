from typing import List
'''
Problem: Largest Triangle Area
Number: 66
Difficulty: Easy
Time Complexity: O(n³)
Space Complexity: O(1)
URL: https://leetcode.com/problems/largest-triangle-area
Topics: Array, Math, Geometry
'''
class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        max_area = 0.0
        for i in range(len(points)-2):
            for j in range(i+1,len(points)-1):
                for k in range(j+1,len(points)):
                    d1,d2,d3 = points[i], points[j],points[k]
                    area = abs(d1[0]*(d2[1]-d3[1]) + d2[0]*(d3[1]-d1[1]) + d3[0]*(d1[1]-d2[1])) / 2.0
                    max_area = max(max_area, area)
        return max_area
                    