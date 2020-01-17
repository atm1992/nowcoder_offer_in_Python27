#-*- coding: UTF-8 -*-

"""
把二叉树打印成多行。
从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        if not pRoot:
            return []
        # 最后返回一个二维数组，二维数组的长度为二叉树的高度
        result = []
        # 当前层的节点数组，下一层的节点数组。层次遍历序列
        cur_nodes, next_nodes = [pRoot], []
        # 当前层的节点数组中的各个节点的值
        cur_val = []
        # 一定要加上判断cur_val是否为空，因为当cur_nodes遍历完最后一层时，cur_nodes、next_nodes都为空，
        # 此时的cur_val保存着最后一层的值，还没有append到result中
        while cur_nodes or next_nodes or cur_val:
            if cur_nodes:
                cur = cur_nodes.pop(0)
                cur_val.append(cur.val)
                if cur.left:
                    next_nodes.append(cur.left)
                if cur.right:
                    next_nodes.append(cur.right)
            else:
                cur_nodes = next_nodes
                next_nodes = []
                result.append(cur_val)
                cur_val = []
        return result
