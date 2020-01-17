#-*- coding: UTF-8 -*-
"""
二叉搜索树的第K个节点。
给定一棵二叉搜索树，请找出其中第k小的结点。
例如，（5，3，7，2，4，6，8）中，按结点数值大小顺序第三小的结点值为4。

二叉搜索树 —— 对于树中的任意节点，其左边的所有子孙节点值都小于等于它，而右边的所有子孙节点值都大于等于它
解题思路：给出的是层次序列。使用中序遍历即可获得升序序列，使用一个计数器来判断是否遍历到了第k个节点
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # not k 表示没有传入参数k
        if not pRoot or not k:
            return None
        res = []

        def inorder(node):
            if len(res) >= k or not node:
                return
            # 递归到最左节点开始返回，因为最左节点不会再有左孩子了
            inorder(node.left)
            res.append(node)
            inorder(node.right)

        inorder(pRoot)
        if len(res) < k:
            return None
        return res[k - 1]
