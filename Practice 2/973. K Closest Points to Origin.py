class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = [sqrt(x**2 + y**2) for x, y in points]
        minHeap = [(d, point) for d, point in zip(distances, points)]
        heapq.heapify(minHeap)

        return [heapq.heappop(minHeap)[1] for i in range(k)] 
