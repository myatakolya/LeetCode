from typing import List
'''
Problem: Longest Common Prefix
Number: 82
Difficulty: Easy
Time Complexity: O(n*m)
Space Complexity: O(m)
URL: https://leetcode.com/problems/longest-common-prefix
Topics: String, Trie
'''
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ''
        if strs:
            for i in strs[0]:
                prefix += i
                if not all(el.startswith(prefix) for el in strs):
                    return prefix[:-1]
        return prefix
    
s = Solution()
n1 = ["flower","flow","flight"]
n2 = ["dog","racecar","car"]
print(s.longestCommonPrefix(n1))
print(s.longestCommonPrefix(n2))
            