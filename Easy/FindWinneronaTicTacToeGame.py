from typing import List
'''
Problem: Find Winner on a Tic Tac Toe Game
Number: 113
Difficulty: Easy
Time Complexity: O(1)
Space Complexity: O(1)
URL: https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game
Topics: Array, Matrix, Simulation
'''
class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        board = [[''] * 3 for _ in range(3)]
        
        for i, (r, c) in enumerate(moves):
            board[r][c] = 'A' if i % 2 == 0 else 'B'
        
        win_lines = [
            [(0,0), (0,1), (0,2)],  # строки
            [(1,0), (1,1), (1,2)],
            [(2,0), (2,1), (2,2)],
            [(0,0), (1,0), (2,0)],  # столбцы
            [(0,1), (1,1), (2,1)],
            [(0,2), (1,2), (2,2)],
            [(0,0), (1,1), (2,2)],  # диагонали
            [(0,2), (1,1), (2,0)]
        ]
        
        for line in win_lines:
            cells = [board[r][c] for r, c in line]
            if cells[0] and cells[0] == cells[1] == cells[2]:
                return cells[0]
        
        if len(moves) == 9:
            return "Draw"
        return "Pending"

    
