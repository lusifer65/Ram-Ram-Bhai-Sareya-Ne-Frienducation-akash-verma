class Solution:
    def longestPalindrome(self, s: str) -> str:

        def helper(s, l, r):
            while( l>=0 and r<len(s) and s[l]==s[r]):
                l-= 1
                r+= 1
            return r-l-1


        if not s:
            return ""

        start, end = 0, 0

        for i in range(len(s)):
            len1 = helper(s, i, i)
            len2 = helper(s, i, i + 1)
            m = max(len1, len2)

            if m > end - start:
                start = i - (m - 1) // 2
                end = i + m // 2

        return s[start:end + 1]