class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        s=0
        e=len(nums)-1
        first=-1
        mid=s+(e-s)//2
        while(s<=e):
            mid=s+(e-s)//2
            if(nums[mid]<target):
                s=mid+1
            elif(nums[mid]>target):
                e=mid-1
            else:
                first=mid
                e=mid-1          
                
        if(first==-1):
            return [-1,-1]
        s=0
        e=len(nums)-1
        last=-1
        while(s<=e):
            mid=s+(e-s)//2
            if(nums[mid]==target):
                last=mid
                s=mid+1
            elif(nums[mid]<target):
                s=mid+1
            else:
                e=mid-1
        
        return [first,last]