'''
Problem: Robot Bounded In Circle
Number: 111
Difficulty: Medium
Time Complexity: O(n)
Space Complexity: O(1)
URL: https://leetcode.com/problems/robot-bounded-in-circle
Topics: String, Simulation
'''
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x,y = 0,0
        dir = 0 #0-север, 1-восток, 2-юг, 3-запад
        for i in instructions:
            if i == 'G':
                if dir == 0:
                    y += 1
                elif dir == 1:
                    x -= 1
                elif dir == 2:
                    y -= 1
                elif dir == 3:
                    x += 1
            elif i == 'L':
                dir = (dir + 3) % 4
            elif i == 'R':
                dir = (dir + 1) % 4
        if (x,y) == (0,0):
            return True
        elif dir != 0:
            return True
        return False    