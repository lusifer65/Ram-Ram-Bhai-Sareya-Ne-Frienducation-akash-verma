class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if len(digits)==0:
            return []
        alpha=['abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']

        # isFirst=True
        ans=[i for i in alpha[int(digits[0])-2]]
        if(len(digits)==1):
            return ans

        for i in range(1,len(digits)):
            temp=ans
            ans=[]
            for btn in alpha[int(digits[i])-2]:
                for j in temp:
                    ans.append(j+btn)
        
        return ans
                        

                    