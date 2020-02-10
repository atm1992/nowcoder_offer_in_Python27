# -*- coding: UTF-8 -*-
"""
从上往下打印二叉树。
从上往下打印出二叉树的每个节点，同层节点从左至右打印。

解题思路：二叉树的层次遍历。使用队列
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        if not root:
            return []
        queue = [root]
        result = []
        while queue:
            cur = queue.pop(0)
            result.append(cur.val)
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
        return result
