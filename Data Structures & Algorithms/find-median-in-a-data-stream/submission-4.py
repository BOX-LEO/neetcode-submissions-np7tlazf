class MedianFinder:

    def __init__(self):
        self.left_maxheap = []
        self.right_minheap = []
        self.median = None
        self.odd = False
        

    def addNum(self, num: int) -> None:
        self.odd = not self.odd
        if self.median is None:
            self.right_minheap.append(num)
            self.median = num
        elif num >=self.median:
            if self.odd:
                heapq.heappush(self.right_minheap,num)
                self.median = self.right_minheap[0]
            else:
                heapq.heappush(self.left_maxheap,-heapq.heappop(self.right_minheap))
                heapq.heappush(self.right_minheap,num)
                self.median = (self.median+self.right_minheap[0])/2
        else:
            if self.odd:
                heapq.heappush(self.right_minheap,-heapq.heappop(self.left_maxheap))
                heapq.heappush(self.left_maxheap,-num)
                self.median = self.right_minheap[0]
            else:
                heapq.heappush(self.left_maxheap,-num)
                self.median = (self.median-self.left_maxheap[0])/2


    def findMedian(self) -> float:
        return self.median
        