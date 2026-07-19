from typing import Optional



class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        el_1 = list1
        el_2 = list2
        res = ListNode()
        while (el_1 and el_1.next) and (el_2 and el_2.next):
            if el_1.val < el_2.val:
                res.val = el_1.val
                el_1 = el_1.next