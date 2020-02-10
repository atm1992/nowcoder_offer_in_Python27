# -*- coding: UTF-8 -*-
"""
二叉搜索树与双向链表。
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求不能创建任何新的结点，只能调整树中结点指针的指向。

解题思路：二叉搜索树的中序遍历结果就是有序的
二叉搜索树 —— 对于树中的任意节点，其左边的所有子孙节点值都小于等于它，而右边的所有子孙节点值都大于等于它
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution1:
    # 非递归版本。使用栈
    def Convert(self, pRootOfTree):
        if not pRootOfTree:
            return None
        # 使用一个栈来保存遍历过程中遇到的节点
        stack = []
        # 指向当前处理节点
        cur = pRootOfTree
        # 指向当前节点的前一个节点
        pre = None
        # 标识是否为双向链表的头结点（即 二叉搜索树的最左节点）
        isFirst = True
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            if isFirst:
                root = cur
                pre = cur
                isFirst = False
            else:
                pre.right = cur
                cur.left = pre
                pre = cur
            cur = cur.right
        return root


class Solution2:
    # 递归版本
    def Convert(self, pRootOfTree):
        if not pRootOfTree:
            return None
        if not pRootOfTree.left and not pRootOfTree.right:
            return pRootOfTree
        # 将左子树构建成双链表，返回链表头。递归
        left = self.Convert(pRootOfTree.left)
        cur = left
        # 定位至左子树中的最右节点，也就是左子树双链表中的最后一个节点
        while cur and cur.right:
            cur = cur.right
        # 若左子树不为空，则将二叉树的根节点加到左子树双链表中的最后一个节点的后面
        if left:
            cur.right = pRootOfTree
            pRootOfTree.left = cur
        # 将右子树也构建成双链表，返回链表头。递归
        right = self.Convert(pRootOfTree.right)
        # 若右子树不为空，则将右子树双链表的头结点加到二叉树根节点的后面
        if right:
            right.left = pRootOfTree
            pRootOfTree.right = right
        return left if left else pRootOfTree
