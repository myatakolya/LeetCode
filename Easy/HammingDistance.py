'''
Problem: Hamming Distance
Number: 96
Difficulty: Easy
Time Complexity: O(log(n))
Space Complexity: O(log(n))
URL: https://leetcode.com/problems/hamming-distance
Topics: Bit Manipulation
'''
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return f'{(x^y):b}'.count('1')