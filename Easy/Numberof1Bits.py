'''
Problem: Number of 1 Bits
Number: 68
Difficulty: Easy
Time Complexity: O(1)
Space Complexity: O(1)
URL: https://leetcode.com/problems/number-of-1-bits
Topics: Bit Manipulation, Math
'''
class Solution:
    def hammingWeight(self, n: int) -> int:
        return n.bit_count()
    
    def hammingWeight_2(self, n: int) -> int:
        res = 0
        while n > 0:
            if n % 2 == 1:
                res += 1
            n = n // 2
        return res