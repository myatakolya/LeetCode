'''
Problem: Valid Parentheses
Number: 83
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(n)
URL: https://leetcode.com/problems/valid-parentheses
Topics: String, Stack
'''
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i in '({[':
                stack.append(i)
            else:
                if not stack:
                    return False
                elif i == ')' and stack[-1] != '(':
                    return False
                elif i == '}' and stack[-1] != '{':
                    return False
                elif i == ']' and stack[-1] != '[':
                    return False
                stack.pop()
        return not stack

s1 = '()'
s2 = '()[]{}'
s3 = '(]'
s4 = '([])'
s5 = '([)]'
s = Solution()
print(s.isValid(s1))
print(s.isValid(s2))
print(s.isValid(s3))
print(s.isValid(s4))
print(s.isValid(s5))