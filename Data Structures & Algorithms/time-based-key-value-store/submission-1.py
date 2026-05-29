class TimeMap:

    def __init__(self):
        self.time_map = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.time_map:
            self.time_map[key] = []
        self.time_map[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:

        key_array = self.time_map[key]

        left, right = 0, len(key_array) - 1
        index = -1
        while left <= right:
            mid = (left + right) // 2

            if key_array[mid][0] == timestamp:
                return key_array[mid][1]

            if key_array[mid][0] > timestamp:
                right = mid -1

            else:
                index = mid
                left = mid + 1

        return "" if index == -1 else key_array[index][1]



        
