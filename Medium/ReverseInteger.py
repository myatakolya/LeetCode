'''
Problem: Reverse Integer
Number: 49
Difficulty: Medium
Time Complexity: O(log n)
Space Complexity: O(1)
URL: https://leetcode.com/problems/reverse-integer
Topics: Math, Simulation
'''
class Solution:
    def reverse(self, x: int) -> int:
        sign = False
        if x < 0:
            sign = True
        N = abs(x)
        R = 0
        while N > 0:
            R = R * 10 + (N % 10)
            N = N//10
        if sign:
            R = R*-1
        if (-2**31 <= R <= 2**31-1):
            return R
        return 0

i = 123
i2 = -123
i3 = 120
s = Solution()
print(s.reverse(i))
print(s.reverse(i2))
print(s.reverse(i3))