'''
Problem: Robot Return to Origin
Number: 110
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(1)
URL: https://leetcode.com/problems/robot-return-to-origin
Topics: String, Simulation
'''
class Solution:
    #Time Complexity: O(n)
    #Space Complexity: O(1)
    def judgeCircle(self, moves: str) -> bool:
        pos = [0,0]
        for i in moves:
            if i == 'U':
                pos[1] += 1
            elif i == 'D':
                pos[1] -= 1
            elif i == 'L':
                pos[0] -= 1
            elif i == 'R':
                pos[0] += 1
        return pos == [0,0]
    
    #Time Complexity: O(n)
    #Space Complexity: O(1)
    def judgeCircle(self, moves: str) -> bool:
        moves_dict = {
            "U":0,
            'D':0,
            'L':0,
            'R':0
        }
        for i in moves:
            moves_dict[i] += 1
        
        return moves_dict['U']==moves_dict['D'] and moves_dict['L'] == moves_dict['R']