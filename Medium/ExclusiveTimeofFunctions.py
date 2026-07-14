from typing import List
'''
Problem: Exclusive Time of Functions
Number: 41
Difficulty: Medium
Time Complexity: O(n)
Space Complexity: O(n)
URL: https://leetcode.com/problems/exclusive-time-of-functions
Topics: Array, Stack
'''
class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        res = [0]*n
        stack = []
        prev_time = 0
        
        for log in logs:
            func_id, action_type, timestamp = log.split(':')
            func_id, timestamp = int(func_id), int(timestamp)
            
            if action_type.lower() == 'start':
                if stack:
                    res[stack[-1]] += timestamp - prev_time
                stack.append(func_id)
                prev_time = timestamp
            else:
                res[stack.pop()] += timestamp - prev_time + 1
                prev_time = timestamp + 1
        return res