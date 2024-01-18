class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        front=[0]*n
        back=[0]*n
        front[0]=height[0]
        back[n-1]=height[n-1]
        for i in range(1,n):
            front[i]=max(front[i-1],height[i])
            back[n-i-1]=max(back[n-i],height[n-i-1])
        # print(front,back)

        c=0
        for i in range(n):
            c+=(min(front[i],back[i])-height[i])

        return c
