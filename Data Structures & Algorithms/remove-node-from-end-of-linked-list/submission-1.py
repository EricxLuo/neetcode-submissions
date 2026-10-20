# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        count = 0
        cur = head
        while cur:
            count +=1
            cur = cur.next
        cur = head
        new = cur

        if count-n == 0:
            return head.next

        for i in range(count-n):
            new = cur
            cur = cur.next
            print(new.val,cur.val)
        
        new.next = cur.next
        return head
        
