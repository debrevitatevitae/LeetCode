# Definition for singly-linked list.
from typing import Optional


class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        node = head
        l = []
        while True:
            l.append(node.val)
            if node.next:
                node = node.next
            else:
                break
        for i, j in zip(l, l[::-1]):
            if i != j:
                return False
        return True


class SolutionStack:

    def isPalindrome(self, head) -> bool:
        l = [head.val]
        while head.next:
            head = head.next
            l.append(head.val)
