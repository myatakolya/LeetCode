from typing import List
'''
Problem: Max Points on a Line
Number: 67
Difficulty: Hard
Time Complexity: O(n²)
Space Complexity: O(n)
URL: https://leetcode.com/problems/max-points-on-a-line
Topics: Array, Hash Table, Geometry
'''
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 2:
            return n
        
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        def normalize(dx, dy):
            if dx == 0:
                return (0, 1)
            if dy == 0:
                return (1, 0)
            g = gcd(abs(dx), abs(dy))
            dx //= g
            dy //= g
            if dx < 0:
                dx, dy = -dx, -dy
            elif dx == 0 and dy < 0:
                dy = -dy
            return (dx, dy)
        
        max_count = 1
        for i in range(n):
            slopes = {}
            duplicate = 0
            for j in range(n):
                if i == j:
                    continue
                dx = points[j][0] - points[i][0]
                dy = points[j][1] - points[i][1]
                if dx == 0 and dy == 0:
                    duplicate += 1
                    continue
                key = normalize(dx, dy)
                slopes[key] = slopes.get(key, 0) + 1
            local_max = 1 + duplicate
            if slopes:
                local_max += max(slopes.values())
            max_count = max(max_count, local_max)
        return max_count