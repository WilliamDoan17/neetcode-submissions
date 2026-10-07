class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        i, j = 0, n - 1
        result = 0

        while i < j:
            d = j - i
            h = min(heights[i], heights[j]) * d
            result = max(result, h) 
            if heights[i] < heights[j]:
                i += 1
            else: 
                j -= 1
            
        return result