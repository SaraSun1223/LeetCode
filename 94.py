# 94. 二叉树的中序遍历

# 给定一个二叉树的根节点 root ，返回 它的 中序 遍历 。
# 示例 1：
# 输入：root = [1,null,2,3]
# 输出：[1,3,2]
# 示例 2：
# 输入：root = []
# 输出：[]
# 示例 3：
# 输入：root = [1]
# 输出：[1]

# 1 递归
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        res.extend(self.inorderTraversal(root.left))
        res.append(root.val)
        res.extend(self.inorderTraversal(root.right))

        return res
