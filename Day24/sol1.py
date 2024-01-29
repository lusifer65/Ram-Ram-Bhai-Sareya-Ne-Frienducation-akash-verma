class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        counts = {}
        for char in t:
            counts[char] = counts.get(char, 0) + 1

        required_chars = len(counts)
        chars = 0
        left, right = 0, 0
        ans = float('inf'), 0, 0  # (length, left, right)

        curr = {}

        while right < len(s):
            char = s[right]
            curr[char] = curr.get(char, 0) + 1

            if char in counts and curr[char] == counts[char]:
                chars += 1

            while chars == required_chars:
                if right - left + 1 < ans[0]:
                    ans = (right - left + 1, left, right + 1)

                char = s[left]
                curr[char] -= 1

                if char in counts and curr[char] < counts[char]:
                    chars -= 1

                left += 1

            right += 1

        return "" if ans[0] == float('inf') else s[ans[1]:ans[2]]