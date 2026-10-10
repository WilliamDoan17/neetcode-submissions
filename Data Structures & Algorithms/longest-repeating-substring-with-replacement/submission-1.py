class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        def getKey(s: str) -> int:
            return ord(s) - ord('A')

        count = [0] * 26 
        j = 0 
        result = 0
        
        for i in range(len(s)):
            count[getKey(s[i])] = count[getKey(s[i])] + 1

            while i - j + 1 - max(count) > k:
                count[getKey(s[j])] = count[getKey(s[j])] - 1
                j += 1
            result = max(result, i - j + 1)

        return result 

            