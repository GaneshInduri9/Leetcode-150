from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxLc = 0
        for num in nums:
            c = 0
            while num+1 in nums:
                c += 1
                num = num + 1
            maxLc = max(c, maxLc)
        return maxLc
    def longestConsecutiveOptimal(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        maxLc = 1
        st = set(nums)
        for num in nums:
            c = 1
            if num-1 not in st:
                while num+1 in st:
                    c += 1
                    num = num + 1
            maxLc = max(c, maxLc)
        return maxLc