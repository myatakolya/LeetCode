'''
Problem: Detect Capital
Number: 74
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(1)
URL: https://leetcode.com/problems/detect-capital
Topics: String, Iteration
'''
class Solution:
    def detectCapitalUse_1(self, word: str) -> bool:
        return (word == word.lower()) or (word == word.upper()) or (word == word.capitalize())
    
    def detectCapitalUse(self, word: str) -> bool:
        upper = 0
        lowwer = 0
        n = len(word)
        # Строчные буквы - 97-122
        # Заглавные буквы - 65-90
        capitalized = 65<=ord(word[0])<=90
        for i in word:
            if 65 <= ord(i) <= 90:
                upper += 1
            elif 97<=ord(i)<=122:
                lowwer += 1
        
        return (upper == n) or (lowwer == n) or (upper == 1 and capitalized)
