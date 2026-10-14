class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo, hi = 1, len(nums)

        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] < nums[0]:
                hi = mid
            else:
                lo = mid + 1
        
        return nums[lo] if lo < len(nums) else nums[0]