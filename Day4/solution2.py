class Solution:
    def maxScore(self, card: List[int], k: int) -> int:
        
        n=len(card)
        tSum=sum(card)
        if(n==k):
            return tSum
        m=0
        
        sumA=[0]
        sumB=[0]
        for i in range(n):
            sumA.append(sumA[i]+card[i])
            sumB.append(sumB[i]+card[n-i-1])
    
        i=0
        while(k>=i):
            m=max(m,sumA[i]+sumB[k-i])
            print(sumA[i]+sumB[k-i])
            i+=1
        return m
        