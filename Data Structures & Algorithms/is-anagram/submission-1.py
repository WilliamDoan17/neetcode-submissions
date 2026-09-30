class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = [0 for i in range(0, 26)] 

        for ch in s:
            seen[ord(ch) - ord('a')] += 1
        
        for ch in t: 
            seen[ord(ch) - ord('a')] -= 1

        for val in seen: 
            if val != 0:
                return False

        return True