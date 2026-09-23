''' For this approach we are going to use a max heap with the number of iterations of a task, then we are going to pop the maximum value and add it to a queue in the format [iterations - 1,time_to_leave] when the queue is empty we return time

Its the same as the other one but we use a proper queue
'''

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0
        # counting the elements
        count = {}
        
        for task in tasks:
            count[task] = count.get(task,0) + 1;
        
        # max heap
        heap = []
        heapq.heapify(heap)

        for task in count:
            heapq.heappush(heap,-count[task]) # negative for max heap

        # make queue
        queue = deque()

        # main loop
        while queue or heap:
            time += 1

            if heap:
                task = -heapq.heappop(heap) - 1

                if task > 0:
                    queue.append([task,time + n])

            # check queue
            if queue:
                if queue[0][1] == time:
                    task = queue.popleft()
                    heapq.heappush(heap,-task[0])

        return time
        