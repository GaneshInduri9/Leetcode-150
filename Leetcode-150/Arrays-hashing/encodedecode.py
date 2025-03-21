from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for s in strs:
            n = len(s)
            res = str(n) + "#" + s
            encoded_string += res
        return encoded_string

    def decode(self, s: str) -> List[str]:

        res = []
        i = 0
        n = len(s)

        while i < n:
            j = s.index("#", i)
            m = int(s[i:j])
            decode_string = s[(j + 1) : (j + 1 + m)]
            res.append(decode_string)
            i = j + 1 + m

        return res


def test():
    sol = Solution()
    input1 = ["ganesh", "#induri", "interview"]
    response = sol.encode(input1)
    decode_res = sol.decode(response)

    if input1 == decode_res:
        print("Test case passed")

    else:
        print("Test case failed")


if __name__ == "__main__":
    test()
