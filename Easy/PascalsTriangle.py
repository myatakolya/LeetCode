from typing import List
'''
Problem: Pascal's Triangle
Number: 59
Difficulty: Easy
Time Complexity: O(n²)
Space Complexity: O(n²)
URL: https://leetcode.com/problems/pascals-triangle
Topics: Array, Dynamic Programming
'''
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for row in range(1,numRows):
            prew_row = row-1
            new_row = [1] + [res[prew_row][i] + res[prew_row][i+1] for i in range(len(res[prew_row])-1)] + [1]
            res.append(new_row)
        return res

s = Solution()
n1 = 5
n2 = 1
n3 = 3
print(s.generate(n1))
print(s.generate(n2))
print(s.generate(n3))