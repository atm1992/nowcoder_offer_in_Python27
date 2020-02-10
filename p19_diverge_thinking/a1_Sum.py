# -*- coding: UTF-8 -*-
"""
求1+2+3+……+n。
求1+2+3+...+n，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。

解题思路：递归。由于不能直接使用if，因此可利用逻辑与and的短路原则

and 的说明：
0 and 1+2   返回0
1 and 2+3   返回5
第一个条件语句的计算结果为True时，返回第二个条件语句的计算结果；第一个条件语句的计算结果为False时，将不会执行第二个条件语句，而是直接返回第一个条件语句的计算结果
"""


class Solution:
    def Sum_Solution(self, n):
        # 当n减到了0时，就不会向下递归了，return 0
        return n and self.Sum_Solution(n - 1) + n

