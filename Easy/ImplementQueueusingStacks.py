'''
Problem: Implement Queue using Stacks
Number: 53
Difficulty: Easy
Time Complexity: O(1)
Space Complexity: O(n)
URL: https://leetcode.com/problems/implement-queue-using-stacks
Topics: Stack, Design, Queue
'''
class MyQueue:

    def __init__(self):
        self.__input_stack = []
        self.__output_stack = []

    def push(self, x: int) -> None:
        self.__input_stack.append(x)
        return None

    def pop(self) -> int:
        if not self.__output_stack:
            while self.__input_stack:
                self.__output_stack.append(self.__input_stack.pop())
        return self.__output_stack.pop()

    def peek(self) -> int:
        if not self.__output_stack:
            while self.__input_stack:
                self.__output_stack.append(self.__input_stack.pop())
        return self.__output_stack[-1]

    def empty(self) -> bool:
        return not self.__input_stack and not self.__output_stack
    
