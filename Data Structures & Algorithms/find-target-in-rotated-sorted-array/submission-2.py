class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        lo, hi = 1, n

        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] < nums[0]:
                hi = mid
            else:
                lo = mid + 1

        if lo == n:
            lo, hi = 0, n - 1
        else:
            if target <= nums[n - 1]:
                hi = n - 1
            else:
                lo, hi = 0, lo - 1

        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        
        return -1