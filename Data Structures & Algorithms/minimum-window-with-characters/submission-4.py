class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t): 
            return ""

        count = dict()
        seen = set()
        for i in range(len(t)):
            seen.add(t[i])
            count[t[i]] = count.get(t[i], 0) + 1 

        i, j = 0, 0
        n = len(s)
        result = None
        
        while i < n:
            count[s[i]] = count.get(s[i], 0) - 1
            while j <= i and count.get(s[j], 0) < 0:
                count[s[j]] = count.get(s[j], 0) + 1
                j += 1
            for ch in seen:
                if count[ch] > 0:
                    break
            else:
                if result == None or i - j + 1 < result[1] - result[0] + 1:
                    result = (j, i)
            i += 1

        return "" if result == None else s[result[0] : result[1] + 1]

        