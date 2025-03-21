import heapq
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        fqmap = {}

        for num in nums:
            if num in fqmap:
                fqmap[num] += 1
            else:
                fqmap[num] = 1

        max_heap = []

        for num, frq in fqmap.items():
            heapq.heappush(max_heap, (-frq, num))

        res = []
        for _ in range(k):
            frq, num = heapq.heappop(max_heap)
            res.append(num)

        return res


def test():
    sol = Solution()
    res = sol.topKFrequent([1, 2, 3, 4, 5, 6, 1, 2], 2)
    print(res)


if __name__ == "__main__":
    test()
