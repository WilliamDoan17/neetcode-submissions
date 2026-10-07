class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []

        n = len(nums)
        nums.sort()

        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target = -nums[i]
            j, k = i + 1, n - 1
            while j < k:
                s = nums[j] + nums[k]
                if s < target:
                    j += 1
                elif s > target:
                    k -= 1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    j, k = j + 1, k - 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
        
        return result
        
        