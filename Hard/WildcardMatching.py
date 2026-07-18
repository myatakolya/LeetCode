from fnmatch import fnmatch
'''
Problem: Wildcard Matching
Number: 22
Difficulty: Hard
Time Complexity: O(n*m)
Space Complexity: O(1)
URL: https://leetcode.com/problems/wildcard-matching
Topics: String
'''
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return fnmatch(s,p)
