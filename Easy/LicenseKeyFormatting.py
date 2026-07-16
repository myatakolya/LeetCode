'''
Problem: License Key Formatting
Number: 75
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(n)
URL: https://leetcode.com/problems/license-key-formatting
Topics: String, Simulation
'''
class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace('-','').upper()
        res = []
        sub_res = []
        for i in reversed(s):
            sub_res.append(i)
            if len(sub_res) == k:
                res.append(''.join(sub_res))
                sub_res = []
        if sub_res:
            res.append(''.join(sub_res))
        return '-'.join(res)[::-1]
    
s = Solution()
s1,k1 = "5F3Z-2e-9-w", 4
s2,k2 = "2-5g-3-J", 2
print(s.licenseKeyFormatting(s1,k1))
print(s.licenseKeyFormatting(s2,k2))