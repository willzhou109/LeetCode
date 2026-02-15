class Solution(object):
    def reorderList(self, head):
        if not head or not head.next:
            return

        # find middle
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # split the list
        second = slow.next
        slow.next = None

        # reverse second half
        prev = None
        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt
        second = prev

        # merge
        first = head
        while second:
            tmp1 = first.next
            tmp2 = second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2
