class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for i in range(len(nums)):
            if i<k:
                heapq.heappush(heap,nums[i])
            else:
                heapq.heappushpop(heap,nums[i])
        return heap[0]
