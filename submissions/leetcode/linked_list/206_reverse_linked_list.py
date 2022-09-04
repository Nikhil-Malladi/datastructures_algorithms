# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        ptr1,ptr2=None,head
        
        while ptr2:
            nxt=ptr2.next
            ptr2.next=ptr1
            ptr1=ptr2
            ptr2=nxt
        return ptr1
