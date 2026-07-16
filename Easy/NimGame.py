'''
Problem: Nim Game
Number: 93
Difficulty: Easy
Time Complexity: O(1)
Space Complexity: O(1)
URL: https://leetcode.com/problems/nim-game
Topics: Math, Game Theory
'''
class Solution:
    def canWinNim(self, n: int) -> bool:
        return not n % 4 == 0