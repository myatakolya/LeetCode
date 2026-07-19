from typing import List
'''
Problem: Average Salary Excluding the Minimum and Maximum Salary
Number: 119
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(1)
URL: https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary
Topics: Array, Math
'''
class Solution:
    def average(self, salary: List[int]) -> float:
        summa = 0
        count_salarys = 0
        max_salary = float('-inf')
        min_salary = float('inf')
        for i in salary:
            summa += i
            count_salarys += 1
            if i > max_salary:
                max_salary = i
            if i < min_salary:
                min_salary = i
        return (summa - max_salary - min_salary) / count_salarys