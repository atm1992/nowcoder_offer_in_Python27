# -*- coding: UTF-8 -*-
"""
二叉树的镜像。
操作给定的二叉树，将其变换为源二叉树的镜像。
二叉树的镜像定义：
    源二叉树：
    	    8
    	   /  \
    	  6   10
    	 / \  / \
    	5  7 9 11
    镜像二叉树：
    	    8
    	   /  \
    	  10   6
    	 / \  / \
    	11 9 7  5

解题思路：涉及到二叉树，优先想到用递归。
先交换根节点的两个子节点，然后交换这两个节点的左右子节点。
如上图：第二层的6、10交换后，第三层变成了9、11、5、7，因此只需交换6的左右子节点以及10的左右子节点即可，其它层同理
"""
from __future__ import print_function


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # 递归终止条件
        if not root:
            return None
        if not root.left and not root.right:
            return root
        root.left, root.right = root.right, root.left
        self.Mirror(root.left)
        self.Mirror(root.right)

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

    def breadth_travel(self, root):
        """广度优先遍历（即 层次遍历）"""
        if not root:
            return None
        queue = [root]
        while queue:
            cur = queue.pop(0)
            print(cur.val, end=" ")
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)


if __name__ == '__main__':
    s = Solution()
    bfs_li = [8, 6, 10, 5, 7, 9, 11]
    root = s.bfs_build_tree(bfs_li)
    print("镜像前：")
    s.breadth_travel(root)
    s.Mirror(root)
    print("\n镜像后：")
    s.breadth_travel(root)
