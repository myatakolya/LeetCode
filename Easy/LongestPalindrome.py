
'''
Problem: Longest Palindrome
Number: 28
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(1)
URL: https://leetcode.com/problems/longest-palindrome
Topics: String, Greedy, Hash Table
'''
class Solution:
    def longestPalindrome(self, s: str) -> int:
        seen_dict = {}
        for i in s:
            try:
                seen_dict[i] += 1
            except KeyError:
                seen_dict[i] = 1
        res = 0
        is_any_odd = False
        for i in seen_dict:
            res += seen_dict[i] // 2 * 2
            if (seen_dict[i] // 2*2) != seen_dict[i]:
                is_any_odd = True
        if is_any_odd == True:
            res += 1    
        return res
            
        
    
s1 = 'abccccdd'
s2 = 'a'
s = Solution()
print(s.longestPalindrome(s1))
print(s.longestPalindrome(s2))