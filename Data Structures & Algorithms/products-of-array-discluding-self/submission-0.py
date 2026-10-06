class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums) 
        pref = [1] * n
        suf = [1] * n

        for i in range(n - 1):
            pref[i + 1] = pref[i] * nums[i]
        for i in range(n - 1, 0, -1):
            suf[i - 1] =  suf[i] * nums[i]
        
        result = [pref[i] * suf[i] for i in range(n)]

        return result
        

        
