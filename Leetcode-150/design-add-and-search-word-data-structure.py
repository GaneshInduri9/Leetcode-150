class TrieNode:
    def __init__(self):
        self.child = [None] * 26
        self.endOfString = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            index = ord(c) - ord('a')
            node = curr.child[index]

            if node is None:
                node = TrieNode()
                curr.child[index] = node
            curr = node
        curr.endOfString = True

    """
        The only tricky party to this problem is the '.', when ever there is '.' it can
        match with any letter if it can be matched with any letter why don't we check for
        every letter for the curr root and do this recursevly for every child of curr if anything 
        returnd true that means we can exit and don't need to see other problems for the current 
        child

        Nice :)
    """

    def search(self, word: str) -> bool:
        curr = self.root
        return self.searchHelper(word, curr, 0)

    def searchHelper(self, word, curr, start):
        n = len(word)
        for i in range(start, n):
            letter = word[i]
            if letter == '.':
                for j in range(26):
                    if curr.child[j] is not None:
                        if self.searchHelper(word, curr.child[j], i + 1):
                            return True
                return False
            else:
                index = ord(letter) - ord('a')
                node = curr.child[index]
                if not node:
                    return False
                curr = node
        return curr.endOfString


# Test cases
if __name__ == "__main__":
    # Create the WordDictionary object
    wd = WordDictionary()

    # Add words to the dictionary
    wd.addWord("apple")
    wd.addWord("app")
    wd.addWord("bat")
    wd.addWord("bad")
    wd.addWord("dad")

    # Test cases
    print(wd.search("apple"))  # True
    print(wd.search("app"))    # True
    print(wd.search("appl"))   # False
    print(wd.search("bat"))    # True
    print(wd.search("b.t"))    # True ('.' matches 'a')
    print(wd.search("b.."))    # True ('.' matches 'at')
    print(wd.search("bad"))    # True
    print(wd.search("ba."))    # True
    print(wd.search("..d"))    # True (matches 'dad' or 'bad')
    print(wd.search("..."))    # True (matches any 3-letter word like 'bat', 'bad', or 'dad')
    print(wd.search("...."))   # False (no 4-letter word added)
    print(wd.search("."))      # False (no 1-letter word added)
