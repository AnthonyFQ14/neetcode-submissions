class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # check maximum pile and make it k 
        # check if k works for h
        # keep moving k down until you cant eat all piles in h time 

        l = 1
        r = max(piles)

        lowestK = max(piles)

        while l <= r:
            
            mid = (l + r) // 2

            if self.timeToEat(piles, mid) <= h:
                lowestK = min(lowestK, mid)
                r = mid - 1
            else:
                l = mid + 1


        return lowestK
        

    def timeToEat(self, piles, k) -> int:
        hours = 0
        for pile in piles:

            hours_to_eat_pile = math.ceil(pile / k)
            hours += hours_to_eat_pile

        return hours