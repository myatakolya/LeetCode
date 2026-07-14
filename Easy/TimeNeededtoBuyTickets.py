from typing import List
from collections import deque
'''
Problem: Time Needed to Buy Tickets
Number: 52
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(n)
URL: https://leetcode.com/problems/time-needed-to-buy-tickets
Topics: Array, Queue, Simulation
'''
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        tickets = deque(tickets)
        tickets[k] = tickets[k]*-1
        answer = 0
        while tickets:
            if tickets[0] > 0:
                
                answer +=1 
                tickets[0]-= 1
                if tickets[0] == 0:
                    tickets.popleft()
                else:
                    tickets.append(tickets.popleft())
                
            elif tickets[0] < 0:
                answer += 1
                tickets[0] += 1
                if tickets[0] == 0:
                    return answer
                else:
                    tickets.append(tickets.popleft())