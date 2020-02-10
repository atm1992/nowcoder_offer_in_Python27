# -*- coding: UTF-8 -*-
"""
剪绳子。
给你一根长度为n的绳子，请把绳子剪成整数长的m段（m、n都是整数，n>1并且m>1），每段绳子的长度记为k[0],k[1],...,k[m]。
请问k[0]xk[1]x...xk[m]可能的最大乘积是多少？例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。
输入：输入一个数n，意义见题面。（2 <= n <= 60）
输出：输出答案。
例如：输入8，输出18

解题思路：动态规划。自底向上解决问题。
"""


class Solution:
    def cutRope(self, number):
        if not number or number < 2:
            return 0
        if number == 2:
            return 1
        if number == 3:
            return 2
        # 最优解数组。数组中的前4个元素分别对应的是剪断绳子后的部分长度为0，1，2，3时的最优解。
        # 例如：绳子剪断后分成若干部分，其中某部分的长度为3，则该部分的最优解为3，也就是该部分无需继续剪断了
        li = [0, 1, 2, 3]
        # 上面的if条件判断到了绳子长度为3的情况，因此下面从绳子长度为4开始计算
        for i in range(4, number + 1):
            max = 0
            # j表示剪断绳子后的部分长度，取值范围从1到i//2
            for j in range(1, i // 2 + 1):
                temp = li[j] * li[i - j]
                if temp > max:
                    max = temp
            li.append(max)
        return li[number]
