1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def goodNodes(self, root: TreeNode) -> int:
9        def dfs(node, max_so_far):
10            if node is None:
11                return 0
12            
13            count = 1 if node.val >= max_so_far else 0
14            new_max = max(max_so_far, node.val)
15            
16            count += dfs(node.left, new_max)
17            count += dfs(node.right, new_max)
18            
19            return count
20        
21        return dfs(root, root.val)
22
23
24        
25        