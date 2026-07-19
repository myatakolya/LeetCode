'''
Problem: Sqrt(x)
Number: 127
Difficulty: Easy
Time Complexity: O(log(n))
Space Complexity: O(1)
URL: https://leetcode.com/problems/sqrtx
Topics: Math, Binary Search
'''
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return x
        x_i = x / 2 if x >= 1.0 else 1.0
        while True:
            nx = 0.5 * (x_i + x / x_i)
            if abs(nx - x_i) < 1:
                return int(nx)
            x_i = nx