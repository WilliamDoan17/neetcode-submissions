class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        count = dict()
        for i in range(len(s1)): 
            count[s1[i]] = count.get(s1[i], 0) + 1

        n, m = len(s2), len(s1)
        i, j = 0, 0
        count2 = dict()
        while i < n:
            count2[s2[i]] = count2.get(s2[i], 0) + 1
            while count2.get(s2[i], 0) > count.get(s2[i], 0):
                count2[s2[j]] = count2.get(s2[j], 0) - 1
                j += 1
            if i - j + 1 == m:
                return True
            i += 1
        
        return False

            