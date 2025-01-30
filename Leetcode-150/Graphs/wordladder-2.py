from typing import List
from collections import deque


class Solution:
    def ladderLength(
        self, beginWord: str, endWord: str, wordList: List[str]
    ) -> List[List]:
        ans = []
        wordset = set(wordList)
        q = deque()
        q.append([beginWord])
        lastUsedLevel = [beginWord]
        level = 0

        while q:
            curr = q.popleft()
            last_word = curr[-1]

            if len(curr) > level:
                level += 1
                for s in lastUsedLevel:
                    wordset.remove(s)

            if last_word == endWord:

                if len(ans) == 0:
                    ans.append(curr)
                elif len(curr) == len(ans[0]):
                    ans.append(curr)

            for i in range(len(last_word)):
                for ch in range(ord("a"), ord("z") + 1):
                    new_word = last_word[0:i] + chr(ch) + last_word[i + 1 :]

                    if new_word in wordset:
                        curr.append(new_word)
                        lastUsedLevel.append(new_word)
                        q.append(curr)
                        curr.pop()

        return ans
