'''
Problem: Repeated Substring Pattern
Number: 77
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(n)
URL: https://leetcode.com/problems/repeated-substring-pattern
Topics: String, String Matching
'''
class Solution:
    def repeatedSubstringPattern_1(self, s: str) -> bool:
        return s in (s + s)[1:-1]
    
    
    #Time Complexity: O(n²)
    #Space Complexity: O(n)
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        prefix = [s[0]]
        for i in range(1,n//2+1):
            if (''.join(prefix) * (n // len(prefix))) == s:
                return True
            prefix.append(s[i])
        return False
            
            
s = Solution()
s1 = 'abab'
s2 = 'aba'
s3 = 'abcabcabcabc'
print(s.repeatedSubstringPattern(s1))
print(s.repeatedSubstringPattern(s2))
print(s.repeatedSubstringPattern(s3))