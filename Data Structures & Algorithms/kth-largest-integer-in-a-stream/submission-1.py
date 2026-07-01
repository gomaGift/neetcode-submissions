class KthLargest:

    def __init__(self, k: int, nums: List[int]):
       
        self.heap_arr = nums
        self.heap_size = k
        heapq.heapify(self.heap_arr)
        while len(self.heap_arr) > k:
            heapq.heappop(self.heap_arr)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.heap_arr, val)
        if len(self.heap_arr) >  self.heap_size :
            heapq.heappop(self.heap_arr)

        return self.heap_arr[0]

        
