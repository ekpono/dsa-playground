# https://leetcode.com/problems/middle-of-the-linked-list/description/

"""
MENTAL MODEL
1. initialize slow and fast to head
2. while fast and fast.next are not empty, do the following
    a. move fast to next next (fast = fast.next.next) because fast has to move two steps ahead
    b. move slow to next (slow = slow.next)
3. if the loop ends, it means fast has reached the end of the list and slow is at the middle of the list, return slow
"""

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        slow = head
        fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        return slow