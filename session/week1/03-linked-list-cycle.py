# https://leetcode.com/problems/linked-list-cycle/description/

"""
MENTAL MODEL
1. if head is empty, return False
2. initialize fast to head.next and slow to head
3. while fast and fast.next are not empty, do the following
    a. if fast and slow are the same, return True that means the fast has caught up with the slow and cycle has been detected
    b. move slow to next (slow = slow.next)
    c. move fast to next next (fast = fast.next.next) because fast has to move two steps ahead
4. if the loop ends, it means there is no cycle, return False
"""
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        if head is None:
            return False
        fast = head.next
        slow = head

        while fast and fast.next:
            if fast == slow:
                return True
            slow = slow.next
            fast = fast.next.next


        return False