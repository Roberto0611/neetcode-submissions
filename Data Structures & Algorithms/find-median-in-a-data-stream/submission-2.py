'''
For this approach we use a small heap (max heap) amd a large heap (min heap), the rules are the len of the
2 heaps should be equal or just 1 more element, and the values of the large heap should be greater or equal
to the elements of the small heap. And to find the medium if its even we take the top element of both heaps
if its not even we take the top element of the longest heap.
'''

class MedianFinder:
    def __init__(self):
        self.smallHeap = []
        self.largeHeap = []

    def addNum(self, num: int) -> None:
        # first we always add it to the small heap
        heapq.heappush(self.smallHeap,-num)

        # check values
        if self.smallHeap and self.largeHeap:
            if abs(self.smallHeap[0]) > abs(self.largeHeap[0]):
                heapq.heappush(self.largeHeap,heapq.heappop(self.smallHeap) * -1) # move from small

        # check len
        lenDiff = abs(len(self.smallHeap) - len(self.largeHeap))
        
        if lenDiff > 1:
            # find the longest one
            if len(self.smallHeap) > len(self.largeHeap):
                # longest is small heap
                heapq.heappush(self.largeHeap,heapq.heappop(self.smallHeap) * -1) # from small to large
            else:
                # longest is large heap
                heapq.heappush(self.smallHeap,heapq.heappop(self.largeHeap) * - 1) # from large to small

    def findMedian(self) -> float:
        #print(f"heaps: {self.smallHeap} and {self.largeHeap}") -- debug --
        if (len(self.smallHeap) + len(self.largeHeap)) % 2 == 0:
            # if its event we take both tops
            median = (self.smallHeap[0] * -1  + self.largeHeap[0]) / 2
            return median

        # if its not even find longest
        if len(self.smallHeap) > len(self.largeHeap):
            # longest is small heap
            return self.smallHeap[0] * -1 
        else:
            # longest is large heap
            return self.largeHeap[0]
