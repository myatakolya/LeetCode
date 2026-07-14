from typing import List
'''
Problem: Maximum Average Subarray I
Number: 50
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(1)
URL: https://leetcode.com/problems/maximum-average-subarray-i
Topics: Array, Sliding Window
'''
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_answer = 0
        for i in range(k):
            window_answer += nums[i]
        
        max_answer = window_answer / k
        for r in range(k,len(nums)):
            l = r-k
            window_answer = window_answer + nums[r] - nums[l]
            max_answer = max(max_answer, window_answer / k)
        return max_answer
        
    

        
        