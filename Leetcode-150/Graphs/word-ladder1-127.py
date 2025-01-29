from typing import List
from collections import deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)

        # If endWord is not in wordList, return 0 since no transformation is possible
        if endWord not in word_set:
            return 0

        q = deque()
        q.append((beginWord, 1))  # (word, level)
        word_set.remove(beginWord)  # Remove beginWord as it has been visited

        while q:
            word, level = q.popleft()

            # Check if we've reached the endWord
            if word == endWord:
                return level

            # Try changing each character of the word
            for i in range(len(word)):
                for ch in range(ord("a"), ord("z") + 1):
                    new_word = word[:i] + chr(ch) + word[i + 1 :]

                    # If new_word is in the word_set, it's a valid transformation
                    if new_word in word_set:
                        word_set.remove(
                            new_word
                        )  # Remove the word from the set to avoid revisiting
                        q.append((new_word, level + 1))  # Add new word to the queue

        return 0  # If no transformation sequence is found


# Test function
def test_ladderLength():
    solution = Solution()

    # Test Case 1: Basic Test Case
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    print(solution.ladderLength(beginWord, endWord, wordList))  # Expected output: 5

    # Test Case 2: No Possible Transformation
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log"]
    print(solution.ladderLength(beginWord, endWord, wordList))  # Expected output: 0

    # Test Case 3: Single Word Transformation
    beginWord = "a"
    endWord = "c"
    wordList = ["a", "b", "c"]
    print(solution.ladderLength(beginWord, endWord, wordList))  # Expected output: 2

    # Test Case 4: Transformation with Multiple Options
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    print(solution.ladderLength(beginWord, endWord, wordList))  # Expected output: 5

    # Test Case 5: No Transformation Possible (EndWord Not in List)
    beginWord = "hot"
    endWord = "dog"
    wordList = ["hot", "dot", "lot"]
    print(solution.ladderLength(beginWord, endWord, wordList))  # Expected output: 0


if __name__ == "__main__":
    test_ladderLength()
