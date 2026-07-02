import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # using the ordinal
        # using the ord(a) but this means i need to sweep time and again
        # a heap obvisiouly, but another data structure to cool down the task
        # say i use a queue, i will append to the que
        #  what will happen is for i in range(n)
        # pop from the que process then add to the q again

        counter = Counter(tasks)
        heap = []
        for key,  val in counter.items():
            heapq.heappush(heap, [-val, key])


      
        print(heap)

        num_cycles = 0
        q = deque()
        while heap or q:
            num_cycles += 1
            if not heap:
                num_cycles = q[0][1]
            else:
                task = heapq.heappop(heap)
                task[0] += 1
                available_time = num_cycles + n
                if task[0]:
                    q.append((task, available_time))


            if q and q[0][1] == num_cycles:
                    heapq.heappush(heap, q.popleft()[0])

        return num_cycles

