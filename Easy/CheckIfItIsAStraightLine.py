from typing import List
'''
Problem: Check If It Is a Straight Line
Number: 122
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(1)
URL: https://leetcode.com/problems/check-if-it-is-a-straight-line
Topics: Array, Math, Geometry
'''
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        d1,d2 = coordinates[0], coordinates[1]
        for i in range(2,len(coordinates)):
            d3 = coordinates[i]
            if ((d3[0] - d1[0]) * (d2[1] - d1[1])) != ((d3[1] - d1[1]) * (d2[0] - d1[0])):
                return False
        return True