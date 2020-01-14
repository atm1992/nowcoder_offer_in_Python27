# -*- coding: UTF-8 -*-
"""
对称的二叉树。
请实现一个函数，用来判断一颗二叉树是不是对称的。注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。

解题思路：递归
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

    def isSymmetrical(self, pRoot):
        return self.isEqual(pRoot, pRoot)

    def isEqual(self, root1, root2):
        if root1 and root2:
            # 若两节点的值不等，则可以直接返回False
            if root1.val != root2.val:
                return False
            # 若相等，则继续下一层递归，直到节点为None
        # 两个节点都为None，说明该子树遍历完毕，则退出当前这层递归，返回至上一层
        elif not root1 and not root2:
            return True
        # 两个节点中一个为None，一个不为None，则可以直接返回False
        else:
            return False
        # 最后左右子树的返回结果做 与运算
        return self.isEqual(root1.left, root2.right) and self.isEqual(root1.right, root2.left)


if __name__ == '__main__':
    s = Solution()
    bfs_li = [8, 6, 6, 5, 7, 7, 5]
    root = s.bfs_build_tree(bfs_li)
    print(s.isSymmetrical(root))
