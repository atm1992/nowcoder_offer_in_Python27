#-*- coding: UTF-8 -*-
"""
八皇后问题：在一个8x8的国际象棋棋盘上，需要放置8个皇后，其中任意两个皇后都不在同一条横线、竖线、斜线方向上。
即 以一个皇后所在的位置为中心，写一个"米"字，"米"字的4条线上不允许出现其它皇后。

解题思路（二维数组）：在一个8行8列的二维数组中，放置8个皇后，放置了皇后所在的点置为1。因此这8个皇后分别在不同的行以及不同的列，
并且每行或每列上必有一个皇后，下面以行为例。从第一行开始，每行放置一个皇后，放置完以后，才放置下一行的皇后，因此，
在检查皇后放置点的合规性时，只需检查当前行之上的（竖线、左斜线、右斜线），因为当前行及以下部分还未放置皇后，因此无需检查。
另外在放置过程中，需要使用递归回溯来确定皇后的放置点，放置好当前行的位置后，还需确定下一行是否有位置可以放，若下一行没有可放置位置，
则重新选择当前行的位置。若当前行没有其它可选位置，则回溯到上一行，以此类推……

解题思路（一维数组）：其实还可以只使用一个长度为8的一维数组，一维数组中的第i个元素代表第i行，第i个元素的值y（0~7）表示第i行的第y列。
在检查皇后放置点的合规性时，需要检查当前行之上的（竖线、左斜线、右斜线）,转换为代码的思路为：
竖线：前面的i-1个元素，它们的元素值都不等于y
左斜线、右斜线：对于前面的i-1行中的任一行j，j行的元素值与y之间的差的绝对值不能等于行号差i-j
"""


class Solution2D:
    """使用二维数组，找出一种布局方案"""
    def __init__(self):
        # 指定行列数分别为8
        self.MAX_NUM = 8
        # 初始化一个8行8列的二维数组，所有值均为0
        self.arr = [[0] * self.MAX_NUM] * self.MAX_NUM

    # 检查当前放置点(x,y)是否合规，索引下标从0开始
    # x行y列，逐行向下放
    def check(self, x, y):
        for i in range(x):
            # 检查当前行之上的竖线
            if self.arr[i][y] == 1:
                return False
            # 检查当前行之上的左斜线
            if y - 1 - i >= 0 and self.arr[x - 1 - i][y - 1 - i] == 1:
                return False
            # 检查当前行之上的右斜线
            if y + 1 + i < self.MAX_NUM and self.arr[x - 1 - i][y + 1 + i] == 1:
                return False
        return True

    # x为行
    def settle_queue(self, x):
        # 表示从上到下的所有行都放置完毕。递归终止条件
        if x == self.MAX_NUM:
            print(self.arr)
            return True
        # 遍历当前行的各列，逐一检查各个位置是否合规
        for i in range(self.MAX_NUM):
            # 先将当前行的所有位置都清零，以避免回溯时出现脏数据
            self.arr[x] = [0] * self.MAX_NUM
            if self.check(x, i):
                self.arr[x][i] = 1
                # 若下一行也能找到合适位置，则表示当前行的位置可行。
                # 若下一行没有找到合适位置（return False），则当前行for循环到下一列
                if self.settle_queue(x + 1):
                    return True
        # 表示当前行没有找到合适位置，因此需要回溯至上一行
        return False


class Solution1D:
    """使用一维数组，找出一种布局方案"""
    def __init__(self):
        # 指定行列数分别为8
        self.MAX_NUM = 8
        # 初始化一个长度为8的一维数组，初始值均为8
        self.arr = [self.MAX_NUM] * self.MAX_NUM

    # 检查当前放置点(x,y)是否合规，索引下标从0开始
    # 一维数组中的第x个元素，该元素的值为y
    def check(self, x, y):
        for i in range(x):
            # 检查当前行之上的竖线 以及 左斜线和右斜线
            if self.arr[i] == y or abs(self.arr[i] - y) == (x - i):
                return False
        return True

    # x为行，即 一维数组中的第x个元素
    def settle_queue(self, x):
        # 表示从上到下的所有行都放置完毕。递归终止条件
        if x == self.MAX_NUM:
            print(self.arr)
            return True
        # 遍历当前行的各列，逐一检查各个位置是否合规
        for i in range(self.MAX_NUM):
            # 相比二维数组，这里无需提前将当前行的元素值复位
            if self.check(x, i):
                self.arr[x] = i
                # 若下一行也能找到合适位置，则表示当前行的位置可行。
                # 若下一行没有找到合适位置（return False），则当前行for循环到下一列
                if self.settle_queue(x + 1):
                    return True
        # 表示当前行没有找到合适位置，因此需要回溯至上一行
        return False


class Solution1DAll:
    """使用一维数组，找出所有布局方案"""
    def __init__(self):
        # 指定最大行数为8
        self.MAX_NUM = 8
        # 初始化一个长度为8的一维数组，初始值均为8
        self.arr = [self.MAX_NUM] * self.MAX_NUM
        # 统计总共有多少种布局方案
        self.count = 0

    # 检查当前放置点(x,y)是否合规，索引下标从0开始
    # 一维数组中的第x个元素，该元素的值为y
    def check(self, x, y):
        for i in range(x):
            # 检查当前行之上的竖线 以及 左斜线和右斜线
            # 等价于：abs(self.arr[i] - y) in (0,(x - i))，即abs(self.arr[i] - y)等于0或等于(x - i)
            if self.arr[i] == y or abs(self.arr[i] - y) == (x - i):
                return False
        return True

    # x为行，即 一维数组中的第x个元素
    def settle_queue(self, x):
        # 表示从上到下的所有行都放置完毕。每一条递归路径的终止条件
        if x == self.MAX_NUM:
            print(self.arr)
            self.count += 1
            return True
        # 遍历当前行的各列，逐一检查各个位置是否合规
        for i in range(self.MAX_NUM):
            # 相比二维数组，这里无需提前将当前行的元素值复位
            if self.check(x, i):
                self.arr[x] = i
                # # 若下一行也能找到合适位置，则表示当前行的位置可行。
                # # 若下一行没有找到合适位置（return False），则当前行for循环到下一列
                # if self.settle_queue(x + 1):
                #     return True

                # 只需修改这里即可。下一行即使找到了合适位置，当前行也继续for循环到下一列。
                # 对于每条递归路径都穷尽所有可能
                self.settle_queue(x + 1)
        # 表示当前行没有找到合适位置，因此需要回溯至上一行
        return False


if __name__ == '__main__':
    s2d = Solution2D()
    # 从第0行开始递归向下找
    s2d.settle_queue(0)

    s1d = Solution1D()
    s1d.settle_queue(0)

    s1d_all = Solution1DAll()
    print("所有布局方案：")
    import time
    start = time.time()
    s1d_all.settle_queue(0)
    end = time.time()
    print("execution time /seconds:", end - start)
    print("Total:", s1d_all.count)
