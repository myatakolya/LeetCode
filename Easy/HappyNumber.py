'''
Problem: Happy Number
Number: 121
Difficulty: Easy
Time Complexity: O(log(n))
Space Complexity: O(log(n))
URL: https://leetcode.com/problems/happy-number
Topics: Math, Hash Table
'''
import datetime


class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        
        while n!=1 and n not in seen:
            seen.add(n)
            n = sum(int(i)**2 for i in str(n))
        
        if n == 1:
            return True
        return False
    