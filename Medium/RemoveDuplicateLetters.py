'''
Problem: Remove Duplicate Letters
Number: 81
Difficulty: Medium
Time Complexity: O(n)
Space Complexity: O(n)
URL: https://leetcode.com/problems/remove-duplicate-letters
Topics: String, Stack, Greedy
'''
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_occurrence = {c: i for i, c in enumerate(s)}
        stack = []
        seen = set()
        
        for i, c in enumerate(s):
            if c in seen:
                continue
            while stack and c < stack[-1] and i < last_occurrence[stack[-1]]:
                seen.remove(stack.pop())
            stack.append(c)
            seen.add(c)
        
        return ''.join(stack)