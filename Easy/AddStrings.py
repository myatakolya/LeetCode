from collections import deque
'''
Problem: Add Strings
Number: 27
Difficulty: Easy
Time Complexity: O(max(n,m))
Space Complexity: O(1)
URL: https://leetcode.com/problems/add-strings
Topics: String, Math, Simulation
'''
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        p1,p2 = len(num1) - 1, len(num2) - 1
        carry = 0
        res = deque()
        
        while p1 >= 0 or p2 >= 0 or carry:
            digit1 = ord(num1[p1]) - ord('0') if p1 >= 0 else 0
            digit2 = ord(num2[p2]) - ord('0') if p2 >= 0 else 0
            
            total = digit1 + digit2 + carry
            carry = total // 10
            res.appendleft(chr(total % 10 + ord('0')))
            
            p1 -= 1
            p2 -= 1
        
        return ''.join(res)
                
                
    
n1,n2 = '11', '123'
n3,n4 = '456','77'
n5,n6 = '0','0'
n7,n8 = '571','419'
n9,n10 = '111','999'
s = Solution()
print(s.addStrings(n1,n2))
print(s.addStrings(n3,n4))
print(s.addStrings(n5,n6))
print(s.addStrings(n7,n8))
print(s.addStrings(n9,n10))