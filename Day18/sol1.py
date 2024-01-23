# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        carry=0
        ans=None
        t=ans
    
        while(l1!=None and l2!=None):
            temp=ListNode()
            temp.val=l1.val+l2.val+carry
            if(temp.val>9):
                carry=1
                temp.val=temp.val%10
            else:
                carry=0
            l1=l1.next
            l2=l2.next
            if(ans==None):
                t=temp
                ans=t
            else:
                t.next=temp
                t=temp
        while(l1!=None):
            temp=ListNode()
            temp.val=l1.val+carry
            if(temp.val>9):
                carry=1
                temp.val=temp.val%10

            else:
                carry=0
            l1=l1.next
            if(ans==None):
                t=temp
                ans=t
            else:
                t.next=temp
                t=temp
        
        while(l2!=None):
            temp=ListNode()
            temp.val=l2.val+carry
            if(temp.val>9):
                carry=1
                temp.val=temp.val%10

            else:
                carry=0
            l2=l2.next
            if(ans==None):
                t=temp
                ans=t
            else:
                t.next=temp
                t=temp
        
        if(carry==1):
             temp=ListNode(1)
             t.next=temp


            
        return ans