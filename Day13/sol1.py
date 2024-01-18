# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n=0
        temp=head
        while(temp!=None):
            n+=1
            temp=temp.next
        t=n//2
        while(t>0):
            head=head.next
            t-=1
        return head