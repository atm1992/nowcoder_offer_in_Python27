# -*- coding: UTF-8 -*-
"""
平衡二叉树。
输入一棵二叉树，判断该二叉树是否是平衡二叉树。
平衡二叉树（AVL树）：对于树中的任意节点，它的两棵子树之间的高度差不大于1

解题思路：递归求解左右子树的高度，然后判断高度差是否大于1
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.flag = True

    def IsBalanced_Solution(self, pRoot):
        self.getDepth(pRoot)
        return self.flag

    def getDepth(self, root):
        if not root:
            return 0
        left = self.getDepth(root.left) + 1
        right = self.getDepth(root.right) + 1
        if abs(left - right) > 1:
            self.flag = False
        return left if left > right else right
