class Solution:
    def minEatingSpeed(self, piles, h: int) -> int:
        def getDivisions(speed) -> int:
            divisions = 0
            for pile in piles:
                divisions += ceil(pile/speed)
                if divisions > h:
                    return divisions

            return divisions

        beg, end = 0, max(piles)
        
        while beg < end:
            mid = (beg+end) // 2

            if mid > 0:
                divisions = getDivisions(mid)
            else:
                break

            if divisions <= h:
                end = mid
            else:
                beg = mid+1
                
        return end