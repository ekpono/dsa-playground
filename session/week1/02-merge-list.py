# https://leetcode.com/problems/merge-two-sorted-lists/description/

"""
MENTAL MODEL
1. Create dummy text and curr to the dummy text (now remember, when curr is updated, dummy is also updated as a result of both of them pointing to the same memory space
2. while the two list have value, if the first val is less than the second value, do the following
    a. point curr.next to the list1
    b. move list1 to next (list1 = list1.next
3. else, do the following
    a. point curr.next to the list2
    b. move list2 to next (list2 = list2.next
4. lastly, move current to next (curr = curr.next
5. return dummy.next since dummy is a fake starter node and the real head of the result list is dummy.next because of point by reference since curr was updating it

"""
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(self, list1, list2):
    dummy = ListNode(0)   # fake starter node
    curr = dummy          # curr walks along the result list

    while list1 and list2:          # while BOTH piles have cards
        if list1.val <= list2.val:
            curr.next = list1       # attach list1's front node
            list1 = list1.next      # advance list1
        else:
            curr.next = list2       # attach list2's front node
            list2 = list2.next      # advance list2
        curr = curr.next            # advance result pointer

    # one pile ran out — attach the rest of the other
    if list1:
        curr.next = list1
    else:
        curr.next = list2

    return dummy.next               # skip the fake starter