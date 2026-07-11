import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
       

        counter = Counter(tasks)
        heap = []
        for task, count in counter.items():
            heapq.heappush(heap, (-count, 0, task))

        num_cycle = 0
        waiting_queue = deque() # To store tasks on cooldown

        while heap or waiting_queue:
            num_cycle += 1
            
            # Move tasks from waiting queue to heap if they are ready
            if waiting_queue and waiting_queue[0][1] <= num_cycle:
                neg_count, ready_at, task = waiting_queue.popleft()
                heapq.heappush(heap, (neg_count, ready_at, task))

            if heap:
                neg_count, available, task = heapq.heappop(heap)
                count = -neg_count - 1
                if count > 0:
                    # Task must wait n cycles after current cycle ends
                    waiting_queue.append((-count, num_cycle + n + 1, task))

        return num_cycle