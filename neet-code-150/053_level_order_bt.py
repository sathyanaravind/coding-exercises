# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        que = collections.deque()
        if root:
            que.append(root)

        while que:
            level = []
            level_len = len(que)
            for i in range(level_len):
                node = que.popleft()
                if node:
                     level.append(node.val)
                     if node.left:
                         que.append(node.left)
                     if node.right:
                        que.append(node.right)
            res.append(level)

        return res
        
