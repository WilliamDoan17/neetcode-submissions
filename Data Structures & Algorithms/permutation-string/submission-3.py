class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        count = dict()
        for i in range(len(s1)): 
            count[s1[i]] = count.get(s1[i], 0) + 1

        n, m = len(s2), len(s1)
        i, j = 0, 0
        while i < n:
            count[s2[i]] = count.get(s2[i], 0) - 1 
            while count.get(s2[i], 0) < 0:
                count[s2[j]] = count.get(s2[j], 0) + 1
                j += 1
            if i - j + 1 == m:
                return True
            i += 1
        
        return False

            