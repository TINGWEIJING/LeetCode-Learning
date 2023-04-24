#!/bin/python3

import math
import os
import random
import re
import sys


class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node


def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

#
# Complete the 'insertNodeAtPosition' function below.
#
# The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
# The function accepts following parameters:
#  1. INTEGER_SINGLY_LINKED_LIST llist
#  2. INTEGER data
#  3. INTEGER position
#

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#


def insertNodeAtPosition(llist, data, position):
    count = 0
    prev_node = None
    curr_node = llist
    while curr_node != None:
        if count == position:
            new_node = SinglyLinkedListNode(node_data=data)
            new_node.next = curr_node
            if prev_node != None:
                prev_node.next = new_node
            break
        prev_node = curr_node
        curr_node = curr_node.next
        count += 1
    return new_node if position == 0 else llist


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    llist_count = int(input())

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist.insert_node(llist_item)

    data = int(input())

    position = int(input())

    llist_head = insertNodeAtPosition(llist.head, data, position)

    print_singly_linked_list(llist_head, ' ', fptr)
    fptr.write('\n')

    fptr.close()


## best
def insertNodeAtPosition(llist, data, position):
    # Write your code here
    
    i = 0
    curr = llist
    new_node = SinglyLinkedListNode(data)
    while curr.next is not None:
        if i == position - 1:
            new_node.next = curr.next
            curr.next = new_node
            break
        
        i += 1
        curr = curr.next
        
    return llist