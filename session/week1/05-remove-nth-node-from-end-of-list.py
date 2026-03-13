# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

"""
MENTAL MODEL
1. Initialize three elements
    a. dummy head (dummy = ListNode(0)
    b. dummpy head's next to head (dummy.next = head)
    c. fast pointer to dummy head (fast = dummy)
    d. slow pointer to dummy head (slow = dummy)
2. Move fast pointer n steps ahead (for _ in range(n): fast = fast.next)
3. Move both fast and slow pointer until fast reaches the end of the list (while fast.next: slow = slow.next; fast = fast.next)
4. At this point, slow is at the node before the target node, so we can skip the target node by pointing slow.next to slow.next.next (slow.next = slow.next.next)
5. Return dummy.next as the new head of the list since dummy is a fake starter node and the real head of the result list is dummy.next because of point by reference since slow was updating it

"""

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head
        fast = dummy
        slow = dummy

        for _ in range(n):
            fast = fast.next

        while fast.next:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return dummy.next