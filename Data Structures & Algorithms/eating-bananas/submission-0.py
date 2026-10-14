class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = 0

        for pile in piles:
            n = max(n, pile)

        lo, hi = 1, n

        while lo < hi: 
            mid = lo + (hi - lo) // 2
            s = 0
            for pile in piles:
                s += math.ceil(pile / mid)
            if s <= h:
                hi = mid
            else:
                lo = mid + 1
        
        return lo