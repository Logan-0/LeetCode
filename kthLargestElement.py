import heapq

class Solution:

    def __init__(self, k: int, nums: list[int]):
        self.min_heap = []
        self.k = k

        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        if len(self.min_heap) < self.k or self.min_heap[0] < val:
            heapq.heappush(self.min_heap, val)
            if len(self.min_heap) > self.k:
                heapq.heappop(self.min_heap)
        return self.min_heap[0]
        

def main() -> None:
    obj = Solution(5, [16,54,13,22,11,99,67,54])
    kth = obj.add(42)
    print(kth)
    kth = obj.add(55)
    print(kth)

if __name__ == "__main__":
    main()