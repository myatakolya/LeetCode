'''
Problem: Masking Personal Information
Number: 76
Difficulty: Medium
Time Complexity: O(n)
Space Complexity: O(n)
URL: https://leetcode.com/problems/masking-personal-information
Topics: String, Simulation
'''
class Solution:
    def maskPII(self, s: str) -> str:
        s = s.lower().split("@")
        if len(s) > 1:
            return s[0][0] + '*****' + s[0][-1] + '@' + s[1]
        else:
            s = s[0].replace('(','').replace(')','').replace('-','').replace('+','').replace(' ','')
            if len(s) > 10:
                return '+' + ('*' * (len(s)%10)) + '-' + '***' + '-' + '***' + '-' + s[-4::]
            return '***' + '-' + '***' + '-' + s[-4::]

s = Solution()
s1 = 'LeetCode@LeetCode.com'
s2 = 'AB@qq.com'
s3 = '1(234)567-890'
s4 = '111(234)567-890'
print(s.maskPII(s1))
print(s.maskPII(s2))       
print(s.maskPII(s3))        
print(s.maskPII(s4))    