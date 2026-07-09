class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        result = ""
        best = len(s) + 1
        counter = len(t)
        needed = {}
        l, r = 0, 0

        for ch in t:
            if ch not in needed:
                needed[ch] = 1
            else:
                needed[ch] += 1
        
        while r < len(s):
            if s[r] in needed:
                if needed[s[r]] > 0:
                    counter -= 1
                needed[s[r]] -= 1
                while counter == 0:
                    if len(s[l:r+1]) < best:
                        result = s[l:r+1]
                        best = len(result)
                    if s[l] in needed:
                        needed[s[l]] += 1
                        if needed[s[l]] > 0:
                            counter += 1
                    l += 1
            r += 1
        
        return result
        