class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        seen = dict([(nums[i], i) for i in range(n)])
        visited = dict([(i, 0) for i in range(n)])
        length = dict([(i, 1) for i in range(n)])

        result = 0
        for i in range(n):
            if not visited.get(i, 0):
                l = 1
                visited.update({i: 1})
                j = seen.get(nums[i] + 1, -1)
                while j != -1 and not visited.get(j, 0):
                    l += 1
                    visited.update({j: 1})
                    j = seen.get(nums[j] + 1, -1)
                if j != -1:
                    l += length.get(j, 0)
                length.update({i: l})
            result = max(result, length.get(i, 0))

        return result

