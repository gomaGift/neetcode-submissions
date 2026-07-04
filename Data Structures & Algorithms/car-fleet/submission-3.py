class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        fleets = [(p, s) for p, s in zip(position, speed)]

        fleets.sort(reverse=True)

        stc = []
        for p, s in fleets:
            time = (target - p) / s
            if not stc or time > stc[-1]:
                stc.append(time)

        return len(stc)





               