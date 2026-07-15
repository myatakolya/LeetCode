'''
Problem: Smallest Integer Divisible by K
Number: 56
Difficulty: Medium
Time Complexity: O(k)
Space Complexity: O(1)
URL: https://leetcode.com/problems/smallest-integer-divisible-by-k
Topics: Math, Number Theory
'''
class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 2 == 0 or k % 5 == 0:
            return -1
        elif k == 1:
            return 1
        else:
            n = 11
            lenght = 2
            if n % k == 0:
                return lenght
            else:
                for _ in range(k):
                    n = (n*10 + 1)%k
                    lenght += 1
                    if n % k == 0:
                        return lenght
            return -1
                