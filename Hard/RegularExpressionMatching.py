
'''
Problem: Regular Expression Matching
Number: 21
Difficulty: Hard
Time Complexity: O(n*m)
Space Complexity: O(1)
URL: https://leetcode.com/problems/regular-expression-matching
Topics: String, Regex
'''


import re
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return bool(re.fullmatch(p,s))
    
i1 = 'aa'
p1 = 'a'
i2 = 'aa'
p2 = 'a*'
i3 = 'ab'
p3 = '.*'
s = Solution()
print(s.isMatch(i1,p1))
print(s.isMatch(i2,p2))
print(s.isMatch(i3,p3))
