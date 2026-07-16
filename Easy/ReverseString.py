from typing import List
'''
Problem: Reverse String
Number: 94
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(1)
URL: https://leetcode.com/problems/reverse-string
Topics: String, Two Pointers
'''
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        p1,p2 = 0,len(s)-1
        while p1 < p2:
            s[p1], s[p2] = s[p2],s[p1]
            p1 += 1
            p2 -= 1

