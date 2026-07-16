from math import gcd
'''
Problem: Greatest Common Divisor of Strings
Number: 81
Difficulty: Easy
Time Complexity: O(n+m)
Space Complexity: O(1)
URL: https://leetcode.com/problems/greatest-common-divisor-of-strings
Topics: String, Math
'''
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ''
        else:
            g = gcd(len(str1), len(str2))
            return str1[:g:]
            
        