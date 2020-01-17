#-*- coding: UTF-8 -*-

"""
按之字形顺序打印二叉树。
请实现一个函数按照之字形打印二叉树，即第一行按照从左到右的顺序打印，
第二层按照从右至左的顺序打印，第三行按照从左到右的顺序打印，其他行以此类推。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def bfs_build_tree(self, bfs_li):
        """使用层次序列构建二叉树。所输入的层次序列任意，可以有None，可以重复"""
        if not bfs_li or len(bfs_li) < 1:
            return None
        root = TreeNode(bfs_li.pop(0))
        nodes = [root]
        while bfs_li:
            cur = nodes.pop(0)
            node = TreeNode(bfs_li.pop(0))
            cur.left = node
            nodes.append(node)
            if bfs_li:
                node = TreeNode(bfs_li.pop(0))
                cur.right = node
                nodes.append(node)
        return root

    def Print(self, pRoot):
        if not pRoot:
            return []
        # 最后返回一个二维数组，二维数组的长度为二叉树的高度
        result = []
        # 当前层的节点数组，下一层的节点数组。层次遍历序列
        cur_nodes, next_nodes = [pRoot], []
        # 当前层的节点数组中的各个节点的值
        cur_val = []
        # 是否需要逆序。刚开始第一层不需要逆序
        rever = False
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
                if rever:
                    cur_val.reverse()
                result.append(cur_val)
                rever = not rever
                cur_val = []
        return result


if __name__ == '__main__':
    s = Solution()
    bfs_li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    root = s.bfs_build_tree(bfs_li)
    print(s.Print(root))
