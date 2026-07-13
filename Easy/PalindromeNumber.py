''' 
Problem: Palindrome Number
Number: 24
Difficulty: Easy
Time Complexity: O(log n)
Space Complexity: O(1)
URL: https://leetcode.com/problems/palindrome-number
Topics: Math
'''

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or x % 10 == 0:
            return False
        elif 0<=x<=9:
            return True
        else:
            R = 0
            N = x
            while N > 0:
                R = R * 10 + (N % 10)
                N = N//10
            if R == x:
                return True
            return False
            

            
i1 = 121
i2 = -121
i3 = 10
s = Solution()
print(s.isPalindrome(i1))
print(s.isPalindrome(i2))
print(s.isPalindrome(i3))