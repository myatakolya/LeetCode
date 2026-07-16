from collections import deque
'''
Problem: Implement Stack using Queues
Number: 87
Difficulty: Easy
Time Complexity: O(n)|O(1)
Space Complexity: O(n)
URL: https://leetcode.com/problems/implement-stack-using-queues
Topics: Stack, Design, Queue
'''
class MyStack:

    def __init__(self):
        self.__queue = deque()

    def push(self, x: int) -> None:
        self.__queue.append(x)
        for _ in range(len(self.__queue)-1):
            self.__queue.append(self.__queue.popleft())

    def pop(self) -> int:
        return self.__queue.popleft()

    def top(self) -> int:
        return self.__queue[0]

    def empty(self) -> bool:
        return not self.__queue


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()