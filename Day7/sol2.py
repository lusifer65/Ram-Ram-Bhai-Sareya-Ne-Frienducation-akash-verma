class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha=[chr(i+97) for i in range(26)]
        for i in range(10):
            alpha.append(f'{i}')
        i=0
        j=len(s)-1
        while(i<j):
            if(s[j].lower() in alpha):
                if(s[i].lower() in alpha):
                    if(s[i].lower()!=s[j].lower()):
                        return False
                    else:
                        i+=1
                        j-=1
                else:
                    i+=1
            else:
                j-=1
                        
                
        return True


