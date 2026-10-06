class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        length = dict([(num, 1) for num in nums])
        visited = dict([(num, 0) for num in nums])

        result = 0
        for num in nums:
            if not visited.get(num, 0):
                visited.update({num: 1})
                l = 1
                j = num + 1
                while length.get(j, 0) != 0 and not visited.get(j, 0):
                    l += 1
                    visited.update({j: 1})
                    j += 1
                if length.get(j, 0) != 0:
                    l += length.get(j, 0)
                length.update({num: l})
                result = max(result, length.get(num, 0))

        return result

