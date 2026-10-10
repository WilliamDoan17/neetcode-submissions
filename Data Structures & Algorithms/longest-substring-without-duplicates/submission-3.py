class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash = dict()
        n = len(s)
        l = 0
        j = 0
        for i in range(len(s)):
            hash.update({s[i]: hash.get(s[i], 0) + 1}) 
            while j < i and hash[s[i]] > 1:
                hash.update({s[j]: hash.get(s[j], 0) - 1})
                j += 1
            l = max(l, i - j + 1)
        return l