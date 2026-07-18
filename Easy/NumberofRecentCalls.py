'''
Problem: Number of Recent Calls
Number: 105
Difficulty: Easy
Time Complexity: O(1)
Space Complexity: O(n)
URL: https://leetcode.com/problems/number-of-recent-calls
Topics: Queue, Design
'''
from collections import deque
class RecentCounter:
    def __init__(self):
        self.requests = deque()

    def ping(self, t: int) -> int:
        self.requests.append(t)
        while self.requests[0] < t-3000:
            self.requests.popleft()
        return len(self.requests)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)