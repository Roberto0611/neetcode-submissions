import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums

        for i in range(len(nums)):
            nums[i] = -nums[i]
        
        heapq.heapify(self.nums)
        
    def add(self, val: int) -> int:
        heapq.heappush(self.nums,-val)
        copy = []

        # create a copy
        for i in self.nums:
            copy.append(i)

        for i in range(self.k):
            if copy:
                n = heapq.heappop(copy)
                        
        return -n

        
