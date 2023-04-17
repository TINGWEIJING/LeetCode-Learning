# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        prev_node = ListNode(-1)
        result_node = prev_node
        curr_node = None
        curr_node_A = l1
        curr_node_B = l2

        next_inc = 0
        while curr_node_A != None or curr_node_B != None:
            val_1 = curr_node_A.val if curr_node_A else 0
            val_2 = curr_node_B.val if curr_node_B else 0

            new_val = val_1 + val_2 + next_inc
            if new_val >= 10:
                next_inc = 1
                new_val -= 10
            else:
                next_inc = 0

            # print(new_val)
            curr_node = ListNode(val=new_val)
            prev_node.next = curr_node

            prev_node = curr_node
            curr_node_A = curr_node_A.next if curr_node_A else curr_node_A
            curr_node_B = curr_node_B.next if curr_node_B else curr_node_B

        if next_inc > 0:
            curr_node = ListNode(val=next_inc)
            prev_node.next = curr_node

        return result_node.next
