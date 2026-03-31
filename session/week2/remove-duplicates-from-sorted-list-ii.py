# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy

        while curr.next and curr.next.next:
            if curr.next.val == curr.next.next.val:
                duplicate_value = curr.next.val
                while curr.next and curr.next.val == duplicate_value:
                    curr.next = curr.next.next
            else:
                curr = curr.next
        return dummy.next

    # OLD SOLUTION
    # def deleteDuplicates(self, head):
    #     """
    #     :type head: Optional[ListNode]
    #     :rtype: Optional[ListNode]
    #     """
    #     duplicate_positions = []
    #     already_scanned = []
    #     curr = head
    #
    #     while curr:
    #         value = curr.val
    #         if value in already_scanned:
    #             duplicate_positions.append(value)
    #         already_scanned.append(value)
    #         curr = curr.next
    #
    #     dummy = ListNode(0)
    #     dummy.next = head
    #     curr = dummy
    #
    #
    #     while curr.next:
    #         if curr.next.val in duplicate_positions:
    #             curr.next = curr.next.next
    #         else:
    #             curr = curr.next
    #
    #     return dummy.next




