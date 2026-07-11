"""
Problem: Roman To Integer
Number: 1
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(1)
URL: https://leetcode.com/problems/roman-to-integer
"""
class Solution: 
    ROMAN_TABLE = {
        'I':1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000
    }
    
    def romanToInt(self,s) -> int:
        res = 0
        prev = ''
        for symbol in reversed(s):
            now = self.ROMAN_TABLE[symbol]
            if prev:
                last = self.ROMAN_TABLE[prev]
                if now < last:
                    res = res - now
                else:
                    res = res + now
            else:
                res += now
            prev = symbol
        return res
