class Solution:
    def fib(self, n: int) -> int:
        if(n==0):
            return 0
        if(n==1):
            return 1
        dp=[-1]*(n+1)
        dp[0]=0
        dp[1]=1
        def helper(n):
            if(n<=0):
                return 0
            if(dp[n]!=-1):
                return dp[n]
            
            temp=self.fib(n-1)+self.fib(n-2)
            dp[n]=temp
        helper(n)
        return dp[-1]