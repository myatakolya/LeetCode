from typing import List
from collections import deque, Counter
'''
Problem: Number of Students Unable to Eat Lunch
Number: 51
Difficulty: Easy
Time Complexity: O(n²)
Space Complexity: O(n)
URL: https://leetcode.com/problems/number-of-students-unable-to-eat-lunch
Topics: Array, Queue, Simulation
'''
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students_counter = Counter(students)
        students = deque(students)
        sandwiches = deque(sandwiches)
        while students and sandwiches:
            if students[0] == sandwiches[0]:
                students_counter[students[0]] -= 1
                students.popleft()
                sandwiches.popleft()  
            elif students[0] != sandwiches[0]:
                students.append(students.popleft())
            if sandwiches and students_counter[sandwiches[0]] == 0:
                break
        return len(students)