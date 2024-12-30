"""
    Given a binary tree root, a node X in the tree is named good if in the path from 
    root to X there are no nodes with a value greater than X.
    Return the number of good nodes in the binary tree.
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, currMax):
            if not node:
                return 0
            
            isGood = 1 if node.val >= currMax else 0
            newMax = max(currMax, node.val)

            return isGood + dfs(node.left, newMax) + dfs(node.right, newMax)
        return dfs(root, root.val)
    
# Test cases for goodNodes function
def test_goodNodes():
    # Helper function to build a binary tree from a list
    def build_tree(values):
        if not values:
            return None
        nodes = [TreeNode(val) if val is not None else None for val in values]
        for i in range(len(nodes)):
            if nodes[i] is not None:
                if 2 * i + 1 < len(nodes):
                    nodes[i].left = nodes[2 * i + 1]
                if 2 * i + 2 < len(nodes):
                    nodes[i].right = nodes[2 * i + 2]
        return nodes[0]
    
    sol = Solution()

    # Test case 1: A single-node tree
    root1 = build_tree([3])
    assert sol.goodNodes(root1) == 1, "Test case 1 failed"

    # Test case 2: Mixed good and bad nodes
    root2 = build_tree([3, 2, 4, 1, None, None, 5])
    assert sol.goodNodes(root2) == 3, "Test case 2 failed"

    # Test case 3: No "good" nodes except the root
    root3 = build_tree([3, 1, 2, 0, None, None, None])
    assert sol.goodNodes(root3) == 1, "Test case 3 failed"

    print("All test cases passed!")

# Run the tests
test_goodNodes()



if __name__ == "__main__":
    test_goodNodes()
