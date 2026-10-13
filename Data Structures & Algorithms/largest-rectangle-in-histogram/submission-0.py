class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        result = 0
        st = []

        for i, h in enumerate(heights):
            start = i
            while st and h < st[-1][1]:
                start, he = st.pop()
                result = max(result, he * (i - start))
            st.append((start, h))

        for i, h in st:
            result = max(result, h * (len(heights) - i)) 

        return result
                
                
