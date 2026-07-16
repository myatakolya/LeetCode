'''
Problem: Number of Segments in a String
Number: 97
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(1)
URL: https://leetcode.com/problems/number-of-segments-in-a-string
Topics: String, Counting
'''
class Solution:
    def countSegments(self, s: str) -> int:
        parts = 0
        for i in range(len(s)):
            if s[i] != ' ' and (i == 0 or s[i-1] == ' '):
                parts += 1
        return parts
    
    
    #Time Complexity: O(n)
    #Space Complexity: O(n)
    def countSegments(self, s: str) -> int:
        return len(s.split())