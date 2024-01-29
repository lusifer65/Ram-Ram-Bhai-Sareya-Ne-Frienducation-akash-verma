class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        h={}
        i=0
        ans=0
        while(i<len(s)):
            if(s[i] not in h):
                h[s[i]]=i
                i+=1
                ans=max(ans,len(h))
            else:
                i=h[s[i]]+1
                h={}
            
        return ans

