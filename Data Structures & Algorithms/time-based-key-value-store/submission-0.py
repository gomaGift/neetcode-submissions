class TimeMap:

    def __init__(self):
        self.time_map = defaultdict(list[defaultdict(str)])
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        new_entry = defaultdict(str)
        new_entry[timestamp] = value
        self.time_map[key].append(new_entry)
        

    def get(self, key: str, timestamp: int) -> str:

        key_array = self.time_map[key]

        left, right = 0, len(key_array) - 1
        index = -1
        while left <= right:
            mid = (left + right) // 2

            entry_map = key_array[mid]
            key = next(iter(entry_map))

            if key == timestamp:
                return entry_map[key]

            if key > timestamp:
                right = mid -1

            else:
                index = mid
                left = mid + 1

        return "" if index == -1 else key_array[index][next(iter(key_array[index]))]



        
