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
        """
        O(N) time and O(N) space
        :param head:
        :return:
        """
        l = [head.val]
        node = head
        # populate stack
        while node.next:
            node = node.next
            l.append(node.val)
        # read from top and from bottom and compare
        node = head
        while node.next:
            if head.val != l.pop():
                return False
            node = node.next
        return True


class SolutionRecursion:

    def isPalindrome(self, head) -> bool:
        """
        O(N) time and O(N) space
        :param head:
        :return:
        """
        pass
