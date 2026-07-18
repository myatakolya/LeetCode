'''
Problem: Find the Index of the First Occurrence in a String
Number: 106
Difficulty: Easy
Time Complexity: O(n*m)
Space Complexity: O(1)
URL: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string
Topics: String, Two Pointers, String Matching
'''
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        try:
            return haystack.index(needle)
        except ValueError:
            return -1