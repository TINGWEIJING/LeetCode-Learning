# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, node: ListNode):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        curr_node = node
        while curr_node.next:
            curr_node.val = curr_node.next.val
            if curr_node.next.next == None:
                curr_node.next = None
                break
            curr_node = curr_node.next

    # best solution
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next

