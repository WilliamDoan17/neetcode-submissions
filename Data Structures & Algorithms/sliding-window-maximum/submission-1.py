from sortedcontainers import SortedList
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = SortedList()
        n = len(nums)
        i, j = 0, 0
        result = []
        for i in range(n):
            window.add(nums[i])
            if (i - j + 1 == k):
                result.append(window[-1])
                window.discard(nums[j])
                j += 1
        return result