class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        result = 0 
        i, j = 0, n - 1
        lmax, rmax = 0, 0
        while i <= j:
            lmax = max(lmax, height[i])
            rmax = max(rmax, height[j])

            if lmax < rmax:
                result += lmax - height[i]
                i += 1
            else:
                result += rmax - height[j]
                j -= 1

        return result
     