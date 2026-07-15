'''
Problem: Sum of Two Integers
Number: 69
Difficulty: Medium
Time Complexity: O(1)
Space Complexity: O(1)
URL: https://leetcode.com/problems/sum-of-two-integers
Topics: Bit Manipulation, Math
'''
class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        while b != 0:
            carry = (a & b) << 1
            a = (a ^ b) & mask
            b = carry & mask
        if a > 0x7FFFFFFF:
            a = ~(a ^ mask)
        return a