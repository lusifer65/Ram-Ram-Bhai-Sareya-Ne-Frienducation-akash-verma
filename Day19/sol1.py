# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(head==None): return None

        temp=None
        while(head!=None):
            t=head
            head=head.next
            t.next=None
            
            if(temp==None):
                temp=t
            else:
                t.next=temp
                temp=t
        return temp