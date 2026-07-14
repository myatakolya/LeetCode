from typing import List
'''
Problem: Kids With the Greatest Number of Candies
Number: 38
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(n)
URL: https://leetcode.com/problems/kids-with-the-greatest-number-of-candies
Topics: Array, Greedy
'''
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        return [(i+extraCandies) >= max_candies for i in candies]