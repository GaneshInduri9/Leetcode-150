"""
    A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently
    store and retrieve keys in a dataset of strings. There are various applications of this 
    data structure, such as autocomplete and spellchecker.
"""

class TrieNode:
    def __init__(self):
        self.child = [None] * 26
        self.endOfString = False
class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root

        for c in word:
            index = ord(c)-ord('a')
            node = curr.child[index]

            if node == None:
                node = TrieNode()
                curr.child[index] = node
            curr = node
        
        curr.endOfString = True

    def search(self, word: str) -> bool:
        curr = self.root

        for c in word:

            index = ord(c)-ord('a')
            node = curr.child[index]

            if node == None:
                return False
            
            curr = node

        return curr.endOfString
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            index = ord(c) - ord('a')
            node = curr.child[index]

            if node == None:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)