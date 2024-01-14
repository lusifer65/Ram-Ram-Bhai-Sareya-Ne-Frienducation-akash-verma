class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ans=False
        for i in range(len(matrix)):
            if(matrix[i][0]<=target and matrix[i][len(matrix[0])-1]>=target):
                s=0
                e=len(matrix[0])-1
                while(s<=e):
                    mid=s+(e-s)//2
                    if(matrix[i][mid]==target):
                        return True
                    elif(matrix[i][mid]<target):
                        s=mid+1
                    else:
                        e=mid-1
        return ans