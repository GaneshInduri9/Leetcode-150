from typing import List
import math


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        speed = 1
        while True:
            totalTime = 0
            for pile in piles:
                totalTime += math.ceil(pile / speed)

            if totalTime <= h:
                return speed
            speed += 1

    def minEatingSpeedOptimal(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        ans = float("inf")
        while l <= r:
            totalTime = 0
            rate = l + (r - l) // 2
            for pile in piles:
                totalTime += math.ceil(pile / rate)

            if totalTime <= h:
                ans = min(ans, rate)
                r = rate - 1
            else:
                l = rate + 1
        return ans


def test():
    sol = Solution()
    basket = [1, 4, 3, 2]
    res = sol.minEatingSpeedOptimal(basket, 9)
    print(res)


if __name__ == "__main__":
    test()
