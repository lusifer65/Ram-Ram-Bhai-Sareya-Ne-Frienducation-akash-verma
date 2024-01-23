# First solution


# class Solution:
#     def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
#         def sortLL(ans,l1):
#             if(ans==None):
#                 return l1
#             if(l1==None):
#                 return ans
#             ll=None
#             curr=ll
#             while(ans!=None and l1!=None):
#                 temp=ListNode()
#                 if(ans.val>l1.val):
#                     temp.val=l1.val
#                     l1=l1.next
#                 else:
#                     temp.val=ans.val
#                     ans=ans.next 
#                 if(ll==None):
#                     curr=temp
#                     ll=curr
#                 else:
#                     curr.next=temp
#                     curr=temp
#             while(ans!=None):
#                 temp=ListNode()
#                 temp.val=ans.val
#                 ans=ans.next
#                 if(ll==None):
#                     curr=temp
#                     ll=curr
#                 else:
#                     curr.next=temp
#                     curr=temp

#             while(l1!=None):
#                 temp=ListNode()
#                 temp.val=l1.val
#                 l1=l1.next
#                 if(ll==None):
#                     curr=temp
#                     ll=curr
#                 else:
#                     curr.next=temp
#                     curr=temp
            
#             return ll

#         if(len(lists)==0 ): return None   
#         ans=None
#         for i in range(len(lists)):  
#             ans=sortLL(ans,lists[i])
#         return ans

# optimzed Solution

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists):
        if not lists:
            return None
        return self.merge(lists, 0, len(lists) - 1)

    def merge(self, lists, start, end):
        if start == end:
            return lists[start]
        mid = (start + end) // 2
        left = self.merge(lists, start, mid)
        right = self.merge(lists, mid + 1, end)
        return self.merge_two(left, right)

    def merge_two(self, l1, l2):
        dummy = ListNode(None)
        curr = dummy

        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next

        curr.next = l1 or l2

        return dummy.next
