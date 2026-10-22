# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        first = ""
        cur = l1
        while cur is not None:
            first = str(cur.val) + first
            cur = cur.next
        cur = l2
        second = ""
        while cur is not None:
            second = str(cur.val) + second 
            cur = cur.next
        res = int(first) + int(second)

        res = str(res)[::-1]
        firstres = ListNode(val = res[0])
        cur = firstres
        for digit in res[1:]:
            cur.next = ListNode(val=digit)
            cur = cur.next
        return firstres