1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
9        def get_leaves(node):
10            if not node:
11                return []
12            if not node.left and not node.right:
13                return [node.val]
14            return get_leaves(node.left) + get_leaves(node.right)
15        
16        return get_leaves(root1) == get_leaves(root2)
17
18        