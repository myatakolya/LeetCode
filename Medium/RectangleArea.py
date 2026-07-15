'''
Problem: Rectangle Area
Number: 67
Difficulty: Medium
Time Complexity: O(1)
Space Complexity: O(1)
URL: https://leetcode.com/problems/rectangle-area
Topics: Math, Geometry
'''
class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        # площади А и B
        a_height = ay2-ay1
        a_weight = ax2-ax1
        area_a = a_height * a_weight
        
        b_height = by2-by1
        b_weight = bx2-bx1
        area_b = b_height * b_weight
        
        # пересечения
        overlap_x = max(0, min(ax2, bx2) - max(ax1,bx1))
        overlap_y = max(0, min(ay2, by2) - max(ay1,by1))
        overlap_A_B = overlap_x * overlap_y
        
        return area_a + area_b - overlap_A_B