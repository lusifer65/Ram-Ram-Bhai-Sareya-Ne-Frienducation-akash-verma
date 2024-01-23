# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if(list1==None and list2==None): return None
        if(list1==None):return list2
        if(list2==None):return list1
        root=None;
        temp=None
        while(list1!=None and list2!=None):
            if(list1.val<list2.val):
                if(root==None):
                    root=list1
                    temp=root
                else:
                    temp.next=list1
                    temp=temp.next
                list1=list1.next
            else:
                if(root==None):
                    root=list2
                    temp=root
                else:
                    temp.next=list2
                    temp=temp.next

                list2=list2.next
                
            if(list1!=None):
                temp.next=list1
            if(list2!=None):
                temp.next=list2

        return root
