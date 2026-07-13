'''
Problem: Fizz Buzz
Number: 29
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(n)
URL: https://leetcode.com/problems/fizz-buzz
Topics: String, Simulation
'''
from typing import List
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        for i in range(1,n+1):
            if i % 5 == 0 and i % 3 == 0:
                res.append("FizzBuzz")
            elif i % 5 == 0:
                res.append("Buzz")
            elif i % 3 == 0:
                res.append('Fizz')
            else:
                res.append(str(i))
        return res