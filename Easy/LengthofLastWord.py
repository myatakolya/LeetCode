'''
Problem: Length of Last Word
Number: 108
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(1)
URL: https://leetcode.com/problems/length-of-last-word
Topics: String, Simulation
'''
class Solution:
    #Time Complexity: O(n)
    #Space Complexity: O(n)
    def lengthOfLastWord_1(self, s: str) -> int:
        return len(s.strip().split(' ')[-1])
    
    #Time Complexity: O(n)
    #Space Complexity: O(1)
    def lengthOfLastWord(self, s: str) -> int:
        res = 0
        word = False
        for i in range(len(s)-1,-1,-1):
            if s[i] == ' ' and word == False:
                continue
            elif s[i] != ' ':
                res += 1
                word = True
            elif s[i] == ' ' and word == True:
                return res
        return res
            