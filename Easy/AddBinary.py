'''
Problem: Add Binary
Number: 123
Difficulty: Easy
Time Complexity: O(n+m)
Space Complexity: O(n+m)
URL: https://leetcode.com/problems/add-binary
Topics: String, Math, Bit Manipulation
'''
class Solution:
    #Time Complexity: O(n+m)
    #Space Complexity: O(n+m)
    def addBinary(self, a: str, b: str) -> str:
        return f'{(int(a,2) + int(b,2)):b}'