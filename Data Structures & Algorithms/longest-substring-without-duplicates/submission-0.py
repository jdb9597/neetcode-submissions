class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        l, r = 0, 1
        seen = {s[0]: 0}
        result = 1
        while r < len(s):
            if s[r] in seen:
                l = max(seen[s[r]] + 1, l)
            seen[s[r]] = r
            result = max((r - l + 1), result)
            r += 1
        return result
        