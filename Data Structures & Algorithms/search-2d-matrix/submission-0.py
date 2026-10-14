class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])
        lo, hi = -1, n - 1

        while lo < hi:
            mid = lo + (hi - lo + 1) // 2  
            if target >= matrix[mid][0]:
                lo = mid
            else:
                hi = mid - 1

        if lo == -1: 
            return False

        i = lo
        print(f"{i}")
        lo, hi = 0, m - 1

        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if target == matrix[i][mid]:
                return True
            elif matrix[i][mid] < target:
                lo = mid + 1 
            else:
                hi = mid - 1
        
        return False