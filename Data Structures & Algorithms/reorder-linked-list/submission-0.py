# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        
        new = []
        curr = head

        while curr:
            new.append(curr)
            curr = curr.next
        
        l,r = 0,len(new)-1

        while l < r:
            new[l].next = new[r]
            l +=1
            new[r].next = new[l]
            r-=1

        new[l].next = None


