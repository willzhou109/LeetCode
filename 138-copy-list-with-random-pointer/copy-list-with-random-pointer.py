"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if head is None:
            return
        hm = dict()
        curr = head
        prev = Node(-1)
        # fill in hashmap values (no random yet)
        while curr:
            hm[curr] = Node(curr.val)
            prev.next = hm[curr]
            prev = hm[curr]
            curr = curr.next
        # fill in random pointer for hashmap values
        curr = head
        while curr:
            if curr.random is None:
                (hm[curr]).random = None
            else:
                (hm[curr]).random = hm[curr.random]
            curr = curr.next


        return hm[head]