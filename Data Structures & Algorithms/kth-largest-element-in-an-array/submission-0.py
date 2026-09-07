import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # convert to negative
        for i in range(len(nums)):
            nums[i] = -nums[i]
        
        # make a heap
        heapq.heapify(nums)

        # pop
        for i in range(k):
            n = heapq.heappop(nums)

        return -n 