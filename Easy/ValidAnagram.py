'''
Problem: Valid Anagram
Number: 88
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(1)
URL: https://leetcode.com/problems/valid-anagram
Topics: String, Hash Table, Sorting
'''
from collections import Counter
from string import ascii_lowercase
class Solution:
    def isAnagram_1(self, s: str, t: str) -> bool:
        counter_s = Counter(s)
        counter_t = Counter(t)
        return counter_s == counter_t
    
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_chars = dict().fromkeys(ascii_lowercase, 0)
        pointer = 0
        while pointer < len(s):
            s_chars[s[pointer]] += 1
            s_chars[t[pointer]] -= 1
            pointer += 1
        return not any(s_chars.values())
            
    
s,t = "anagram", "nagaram"
sol = Solution()
print(sol.isAnagram(s,t))
        