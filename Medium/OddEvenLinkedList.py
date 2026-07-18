'''
Problem: Odd Even Linked List
Number: 103
Difficulty: Medium
Time Complexity: O(n)
Space Complexity: O(1)
URL: https://leetcode.com/problems/odd-even-linked-list
Topics: Linked List, Two Pointers
'''
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        odd = head
        even = head.next
        even_head = even
        
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        
        odd.next = even_head
        return head