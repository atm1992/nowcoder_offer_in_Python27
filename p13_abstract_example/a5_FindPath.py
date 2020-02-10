# -*- coding: UTF-8 -*-
"""
二叉树中和为某一值的路径。
输入一颗二叉树的根节点和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。(注意: 在返回值的list中，数组长度大的数组靠前)

解题思路：使用深度优先搜索。递归
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        if not root or root.val > expectNumber:
            return []
        # 当前节点为叶节点（左右子树均为空，才是叶节点）
        if root.val == expectNumber and not root.left and not root.right:
            return [[root.val]]
        expectNumber -= root.val
        # 查找左子树方向，返回[] 或 二维数组
        left = self.FindPath(root.left, expectNumber)
        # 查找右子树方向，返回[] 或 二维数组
        right = self.FindPath(root.right, expectNumber)
        result = []
        for i in left:
            result.append([root.val] + i)
        for i in right:
            result.append([root.val] + i)
        # reverse = True 降序 ， reverse = False 升序（默认）
        return sorted(result, key=lambda x: len(x), reverse=True)
