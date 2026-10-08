class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        leftMax = [height[0]] * n
        rightMax = [height[n - 1]] * n
        
        for i in range(1, n):
            leftMax[i]= max(leftMax[i - 1], height[i])
        for i in range(n - 2, -1, -1):
            rightMax[i] = max(rightMax[i + 1], height[i]) 

        result = 0
        for i in range(n):
            result += min(leftMax[i], rightMax[i]) - height[i]
        
        return result
     