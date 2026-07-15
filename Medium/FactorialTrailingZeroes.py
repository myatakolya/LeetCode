'''
Problem: Factorial Trailing Zeroes
Number: 63
Difficulty: Easy
Time Complexity: O(log(n))
Space Complexity: O(1)
URL: https://leetcode.com/problems/factorial-trailing-zeroes
Topics: Math
'''
class Solution:
    def trailingZeroes(self, n: int) -> int:
        res = 0
        while n >= 5:
            n //= 5
            res += n
        return res