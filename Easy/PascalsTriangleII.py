from typing import List
'''
Problem: Pascal's Triangle II
Number: 84
Difficulty: Easy
Time Complexity: O(n²)
Space Complexity: O(n)
URL: https://leetcode.com/problems/pascals-triangle-ii
Topics: Array, Dynamic Programming
'''
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        last_row = [1]
        for _ in range(rowIndex):
            cur_row = [1] + [last_row[i] + last_row[i+1] for i in range(len(last_row)-1)] + [1]
            last_row = cur_row
        return last_row
    
n1 = 3
s = Solution()
print(s.getRow(n1))