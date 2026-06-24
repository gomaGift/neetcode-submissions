class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        l, r = 0, len(people) - 1
        boats_needed = 0
        while l <= r:
            if people[l] + people[r] <= limit:
                l += 1
                r -= 1
            else:
                r -= 1

            boats_needed += 1
        return boats_needed