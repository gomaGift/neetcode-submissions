class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        key_map = defaultdict(int)
        for start, end in intervals:
            key_map[start] += 1
            key_map[end] -= 1

        have = 0
        curr_interval = []
        res = []
        for key in sorted(key_map):
            if not curr_interval:
                curr_interval.append(key)

            have += key_map[key]

            if have == 0:
                curr_interval.append(key)
                res.append(curr_interval)
                curr_interval = []

        return res


            

        




        def merge_interval(interval1, interval2):
            new_end = max(interval1[1], interval2[1])
            return [interval1[0], new_end]

        def should_merge(interval1, interval2):
            return interval2[0] <= interval1[1]


        intervals.sort(key=lambda x: x[0])
        res = [intervals[0]]
        for interval in intervals[1:]:
            if should_merge(res[-1], interval):
                merged = merge_interval(res[-1], interval)
                res[-1] = merged
            else:
                res.append(interval)

        return res

        