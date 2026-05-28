class Solution:
    def canEatBananasAtNSpeed(self, piles: List[int], n: int, h: int) -> bool:
        used_time = 0
        for pile in piles:
            used_time += math.ceil(pile/n)
        return used_time <= h

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_speed = 1
        max_speed = max(piles)
        
        min_res_speed = -1

        while min_speed <= max_speed:
            mid_speed = (min_speed + max_speed) // 2
            if self.canEatBananasAtNSpeed(piles, mid_speed, h):
                min_res_speed = mid_speed
                max_speed = mid_speed - 1
            else:
                min_speed = mid_speed + 1
            
        return min_res_speed


        