# -*- coding: UTF-8 -*-
"""
二叉树中和为某一值的路径。
输入一颗二叉树的根节点和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。
注意：二叉树节点中的值既可以是正数，也可以是负数，还可以是0

解题思路：使用深度优先搜索。递归
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回一个二维数组，内部每个数组表示一条路径
    def FindPath(self, root, expectNumber):
        if not root:
            return []
        res = []

        def dfs(node, cur_sum, cur_res):
            if not node:
                return
            if cur_sum == node.val and not node.left and not node.right:
                # 这里也可直接写 res.append(cur_res + [node.val])，
                # 但不能写成 res.append(cur_res.append(node.val))，因为cur_res.append(node.val)返回的是None
                cur_res.append(node.val)
                res.append(cur_res)
                return
            # cur_sum - node.val表示将计算结果传给形参cur_sum，cur_sum本身的值没有被修改
            # cur_res + [node.val]会返回一个新的数组，然后将新数组传给形参cur_res，cur_res数组本身没有被修改
            # 这样做是为了回溯
            dfs(node.left, cur_sum - node.val, cur_res + [node.val])
            dfs(node.right, cur_sum - node.val, cur_res + [node.val])

        dfs(root, expectNumber, [])
        return res
