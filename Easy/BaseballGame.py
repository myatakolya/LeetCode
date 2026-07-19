from typing import List
'''
Problem: Baseball Game
Number: 112
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(n)
URL: https://leetcode.com/problems/baseball-game
Topics: Array, Stack, Simulation
'''
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = []
        summa = 0
        for i in operations:       
            if i == '+' and len(scores) > 1:
                summa += scores[-1] + scores[-2]
                scores.append(scores[-1] + scores[-2])
                
            elif i == 'D' and len(scores) > 0:
                summa += scores[-1]*2
                scores.append(scores[-1]*2)
            elif i == 'C' and scores:
                summa -=scores.pop()  
            else:
                scores.append(int(i))
                summa += int(i)
        return summa