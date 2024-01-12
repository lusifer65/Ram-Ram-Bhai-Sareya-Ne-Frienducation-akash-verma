class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)!=len(t)):return False

        ans=list(*s.split())
        for i in t:
            if(i in ans):
                ans.remove(i)
            else:
                return False
        if(ans==[]):
            return True
        return False