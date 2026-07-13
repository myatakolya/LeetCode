
'''
Problem: Valid Palindrome
Number: 25
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(1)
URL: https://leetcode.com/problems/valid-palindrome
Topics: Two Pointers, String
'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        p1,p2 = 0,len(s)-1
        while p1 < p2:
            
            while p1 < p2 and not s[p1].isalnum():
                p1 += 1
            
            while p1 < p2 and not s[p2].isalnum():
                p2 -= 1
            
            if s[p1].lower() != s[p2].lower():
                return False
            p1 += 1
            p2 -= 1
            
        return True
