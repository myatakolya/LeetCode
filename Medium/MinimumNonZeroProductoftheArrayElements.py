'''
Problem: Minimum Non-Zero Product of the Array Elements
Number: 18
Difficulty: Medium
Time Complexity: O(n + log n)
Space Complexity: O(1)
URL: https://leetcode.com/problems/minimum-non-zero-product-of-the-array-elements
Topics: Math, Bit Manipulation, Exponentiation
'''
class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        maximum = (1 << p) - 1
        count = (maximum - 1) // 2
        MOD = 10**9 + 7
        return (maximum * pow(maximum-1, count, MOD)) % MOD