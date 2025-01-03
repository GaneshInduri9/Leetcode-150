"""
    Implement an algorithm to serialize and deserialize a binary tree.
    Serialization is the process of converting an in-memory structure into
    a sequence of bits so that it can be stored or sent across a network to be 
    reconstructed later in another computer environment. You just need to ensure 
    that a binary tree can be serialized to a string and this string can be 
    deserialized to the original tree structure. There is no additional restriction 
    on how your serialization/deserialization algorithm should work.
    Note: The input/output format in the examples is the same as how NeetCode serializes 
    a binary tree. You do not necessarily need to follow this format.
"""
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []

        def dfs(node):
            if not node:
                res.append("N")
                return
            
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)

        return "#".join(res)
        
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        values = data.split("#")
        self.i = 0

        def dfs():
            if values[self.i] == "N":
                self.i += 1
                return None
            
            root = TreeNode(int(values[self.i]))
            self.i += 1
            root.left = dfs()
            root.right = dfs()

            return root

        return dfs()

def test_serialize_deserialize():
    codec = Codec()

    # Test 1: Empty Tree
    tree = None
    serialized = codec.serialize(tree)
    assert serialized == "N", f"Test 1 Failed: {serialized}"
    deserialized = codec.deserialize(serialized)
    assert deserialized is None, "Test 1 Failed: Deserialized tree is not None"

    # Test 2: Single Node Tree
    tree = TreeNode(1)
    serialized = codec.serialize(tree)
    assert serialized == "1#N#N", f"Test 2 Failed: {serialized}"
    deserialized = codec.deserialize(serialized)
    assert deserialized.val == 1 and deserialized.left is None and deserialized.right is None, "Test 2 Failed"

    # Test 3: Full Binary Tree
    # Tree:
    #     1
    #    / \
    #   2   3
    tree = TreeNode(1, TreeNode(2), TreeNode(3))
    serialized = codec.serialize(tree)
    assert serialized == "1#2#N#N#3#N#N", f"Test 3 Failed: {serialized}"
    deserialized = codec.deserialize(serialized)
    assert deserialized.val == 1 and deserialized.left.val == 2 and deserialized.right.val == 3, "Test 3 Failed"

    # Test 4: Tree with Null Nodes
    # Tree:
    #     1
    #    / \
    #   2   3
    #  /     \
    # N       4
    tree = TreeNode(1, TreeNode(2, None, None), TreeNode(3, None, TreeNode(4)))
    serialized = codec.serialize(tree)
    assert serialized == "1#2#N#N#3#N#4#N#N", f"Test 4 Failed: {serialized}"
    deserialized = codec.deserialize(serialized)
    assert deserialized.val == 1, "Test 4 Failed: Root mismatch"
    assert deserialized.left.val == 2 and deserialized.left.left is None and deserialized.left.right is None, "Test 4 Failed: Left subtree mismatch"
    assert deserialized.right.val == 3 and deserialized.right.left is None and deserialized.right.right.val == 4, "Test 4 Failed: Right subtree mismatch"

    # Test 5: Larger Tree
    # Tree:
    #         1
    #        / \
    #       2   3
    #      /   / \
    #     4   5   6
    #    /
    #   7
    tree = TreeNode(1,
                    TreeNode(2,
                             TreeNode(4,
                                      TreeNode(7))),
                    TreeNode(3,
                             TreeNode(5),
                             TreeNode(6)))
    serialized = codec.serialize(tree)
    assert serialized == "1#2#4#7#N#N#N#N#3#5#N#N#6#N#N", f"Test 5 Failed: {serialized}"
    deserialized = codec.deserialize(serialized)
    assert deserialized.val == 1, "Test 5 Failed: Root mismatch"
    assert deserialized.left.val == 2 and deserialized.right.val == 3, "Test 5 Failed: Children mismatch"
    assert deserialized.left.left.val == 4 and deserialized.left.left.left.val == 7, "Test 5 Failed: Left subtree mismatch"
    assert deserialized.right.left.val == 5 and deserialized.right.right.val == 6, "Test 5 Failed: Right subtree mismatch"

    print("All tests passed!")


# Run tests
test_serialize_deserialize()

