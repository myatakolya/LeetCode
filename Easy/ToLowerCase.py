'''
Problem: To Lower Case
Number: 109
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(n)
URL: https://leetcode.com/problems/to-lower-case
Topics: String
'''
class Solution:
    def toLowerCase(self, s: str) -> str:
        return s.lower()
    
    def toLowerCase(self, s: str) -> str:
        lower = []
        for char in s:
            if 65<=ord(char)<=90:
                lower.append(chr(ord(char)+32))
            else:
                lower.append(char)
        return ''.join(lower)