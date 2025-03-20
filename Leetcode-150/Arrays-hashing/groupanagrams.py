from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = {}

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord("a")] += 1
            key = tuple(count)
            if key in res:
                res[key].append(s)
            else:
                res[key] = [s]
        return list(res.values())


def test():
    sol = Solution()
    inp = ["eat", "tea", "tan", "ate", "nat", "bat"]
    res = sol.groupAnagrams(inp)
    print(res)


if __name__ == "__main__":
    test()
