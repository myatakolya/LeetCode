'''
Problem: Ugly Number
Number: 54
Difficulty: Easy
Time Complexity: O(log n)
Space Complexity: O(1)
URL: https://leetcode.com/problems/ugly-number
Topics: Math, Number Theory
'''
class Solution:

    def isUgly(self, n: int) -> bool:
        if n < 1:
            return False
        elif n == 1:
            return True
        else:
            factors = []
            if n % 2 == 0:
                factors.append(2)
                while n % 2 == 0:
                    n //= 2
            if n % 3 == 0:
                factors.append(3)
                while n % 3 == 0:
                    n //= 3
            d = 5
            step = 2
            while d * d <= n:
                if n % d == 0:
                    factors.append(d)
                    while n % d == 0:
                        n //= d
                d += step
                step = 6 - step
            if n > 1:
                factors.append(n)
            if factors[-1] > 5:
                return False
            return True