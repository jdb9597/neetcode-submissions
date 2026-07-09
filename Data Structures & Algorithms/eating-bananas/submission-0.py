class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo, hi = 1, max(piles) 
        while lo < hi:
            mid = (lo + hi) // 2
            if self.can_finish(piles, h, mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
        
    def can_finish(self, piles: list[int], h: int, k: int) -> bool:
        countdown = h
        for pile in piles:
            countdown -= math.ceil(pile / k)
        if countdown >= 0:
            return True
        return False