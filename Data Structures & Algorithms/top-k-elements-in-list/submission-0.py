from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        sorted_items = sorted(counter.items(), key=lambda item: item[1])
        print(sorted_items)

        res = []
        for i in range(len(sorted_items) - k, len(sorted_items)):
            res.append(sorted_items[i][0])

        return res


        