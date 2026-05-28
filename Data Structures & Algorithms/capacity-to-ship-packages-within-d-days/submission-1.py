class Solution:

    def shipDaysWithLoadingNWeightPerDay(self, weights: List[int], capacity: int):
        used_days = 1
        load = 0
        for weight in weights:
            load += weight
            if load > capacity:
                used_days += 1
                load = weight

        return used_days
                


    def shipWithinDays(self, weights: List[int], days: int) -> int:
        min_load = max(weights)
        max_load = sum(weights)
        min_capacity = -1
        while min_load <= max_load:
            mid_load = (min_load + max_load) // 2
            used_days = self.shipDaysWithLoadingNWeightPerDay(weights, mid_load)
            if used_days > days:
                min_load = mid_load + 1

            else:
                min_capacity = mid_load
                max_load = mid_load - 1

        return min_capacity



        