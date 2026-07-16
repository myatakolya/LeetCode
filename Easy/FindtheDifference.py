from collections import Counter
'''
Problem: Find the Difference
Number: 95
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(1)
URL: https://leetcode.com/problems/find-the-difference
Topics: String, Hash Table, Bit Manipulation
'''
class Solution:
    def findTheDifference_1(self, s: str, t: str) -> str:
        counter_s = Counter(s)
        counter_t = Counter(t)
        for i in counter_t:
            if counter_t[i] > counter_s[i]:
                return i
     
    def findTheDifference_2(self, s: str, t: str) -> str:
        res = 0
        for i in s:
            res ^= ord(i)
        for i in t:
            res ^= ord(i)
        return chr(res)
    
    def findTheDifference(self, s: str, t: str) -> str:
        sum_s = 0
        sum_t = 0
        for i in s:
            sum_s += ord(i)
        for i in t:
            sum_t += ord(i)
        return chr(sum_t - sum_s)